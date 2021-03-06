from flask import Flask, request, render_template, make_response, abort

import regex
import os
import json
import datetime
import logging

from sqlalchemy import literal

from package import filters, utilities
from package import models, session_scope
from package import politifact
from package import defaults

log = logging.getLogger('newsbin.site')
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	options = request.values.to_dict()
	sources = filters.sources.keys()

	# count defaults to 100 if empty or not given
	count = int(options.get('count',100) or 100)

	# if there are no sources in arguments, all sources are set
	if set(sources).isdisjoint(set(options)):
		options.update({ key:'on' for key in sources })

	with session_scope() as session:
		category = options.get('category','all')
		search, pattern = options.get('search',''), None
		if search.startswith('re:'): pattern = regex.compile( search.split(':',1)[1] )

		# the base query is just a filter to make sure the sources are
		# what was requested and orders them by date. Note that we don't
		# care about the 'all' option- it's just a javascript hook to set
		# the other values in the search form.
		articles = session.query( models.Article )\
			.filter( models.Article.source.in_(options) )\
			.order_by( models.Article.fetched.desc() )

		# if they have selected a category, add a filter that tests to make sure that category is
		# in the results.
		if category != 'all':
			articles = articles.filter( models.Article.category.contains(category) )

		# if there is a regular expression, we have to fetch all of the articles and then apply the pattern
		# this is probably really slow, but it won't happen often. A regular search term will use the sqlalchemy
		# query api, which is probably a lot faster.
		if pattern:
			articles = [ a for a in articles.all() if pattern.search(a.title) or pattern.search(a.content) ][:count]
		else:
			articles = articles.filter( models.Article.title.contains(search) | models.Article.content.contains(search))\
				.slice(0,count)\
				.all()

		return render_template('index.html', articles=articles, categories=defaults.default_categories(), date=datetime.datetime.now())


	# couldn't get a session for some reason
	return abort(404)

@app.route('/article/<int:pk>', methods=['GET','POST'])
def article( pk ):
	if request.method == 'GET':
		with session_scope() as session:
			try:
				article = session.query( models.Article ).get( pk )
				if article.blacklist:
					blacklist = article.blacklist.replace(';',', ')
				else:
					blacklist = ''
				return render_template('article.html', article=article, blacklist=blacklist, date=datetime.datetime.now())
			except Exception as e:
				log.exception(e)
				raise

	elif request.method == 'POST':
		name = request.form.get('annotation',None)
		add = 'add' in request.form
		if pk:
			try:
				with session_scope() as session:
					article = session.query( models.Article ).get( pk )

					if add:
						utilities.summarize(name)
						article.unblacklist_name( name )
					else:
						article.blacklist_name(name)
					return render_template('article.html', article=article, blacklist=article.blacklist.replace(';',','), date=datetime.datetime.now())
			except Exception as e:
				log.exception(e)
		else:
			log.warning('pk missing from request: pk:{} name:{} add:{}'.format(pk,name,add))
			return abort(404)
	else:
		return abort(404)

@app.route('/article/<int:pk>/annotate', methods=['GET'])
def annotate( pk ):
	try:
		with session_scope() as session:
			article = session.query( models.Article ).get( pk )
			annotations = session.query( models.Annotation ).filter( literal(article.content).contains(models.Annotation.name)).all()
			data = {
				'annotations':[ a.name for a in annotations if a.name not in article.get_blacklist() ],
				'blacklist':article.get_blacklist(),
			}
			return make_response( json.dumps(data) )
	except Exception as e:
		log.exception('at /article/<int:pk>/annotate: '.format(e))
		return abort(404)



@app.route('/annotations', methods=['GET'])
def annotations():
	name = request.values.get('name',None)
	with session_scope() as session:
		try:
			annotation = session.query( models.Annotation ).filter( models.Annotation.name==name ).first()
			slug = annotation.slug
			if not slug:
				rating, slug = politifact.get_rating(name=annotation.name)
				if slug: annotation.update(slug=slug)
			else:
				rating, slug = politifact.get_rating(name=annotation.name,slug=slug)
		except Exception as e:
			try:
				annotation = utilities.summarize(name)
				if annotation.name:
					rating, slug = politifact.get_rating(name=annotation.name)
					if slug: annotation.update(slug=slug)
			except Exception as e:
				log.exception(e)
				return abort(404)

		table_items = []
		if rating: table_items.append({'key':'Truth Score','value':str(rating)+'%','tooltip':'from last five statements rated by politifact.com'})

		data = annotation.serialize(data_table=table_items,slug=slug)
		return make_response(data)

@app.route('/about', methods=['GET'])
def about():
	return render_template('about.html', categories=defaults.default_categories(), date=datetime.datetime.now())

# ------------------------------------------------------------------------------
# Error Pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html', e=e), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('errors/500.html', e=e), 500

if __name__ == "__main__":
	app.run(host='0.0.0.0')
