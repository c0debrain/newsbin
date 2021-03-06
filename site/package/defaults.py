
# sources to fetch articles from
sources = [
	('cnn','http://rss.cnn.com/rss/edition.rss','top'),
	('cnn','http://rss.cnn.com/rss/cnn_world.rss','world'),
	('cnn','http://rss.cnn.com/rss/cnn_us.rss','us'),
	('cnn','http://rss.cnn.com/rss/money_latest.rss','finance'),
	('cnn','http://rss.cnn.com/rss/cnn_allpolitics.rss','politics'),
	('cnn','http://rss.cnn.com/rss/cnn_tech.rss','technology'),
	('cnn','http://rss.cnn.com/rss/cnn_health.rss','health'),
	('cnn','http://rss.cnn.com/rss/cnn_showbiz.rss','entertainment'),
	('cnn','http://rss.cnn.com/rss/cnn_travel.rss','travel'),
	('cnn','http://rss.cnn.com/rss/cnn_living.rss','life'),
	('cnn','http://rss.cnn.com/rss/cnn_latest.rss','top'),
	('cnbc','http://www.cnbc.com/id/100003114/device/rss/rss.html','top'),
	('cnbc','http://www.cnbc.com/id/100727362/device/rss/rss.html','world'),
	('cnbc','http://www.cnbc.com/id/15837362/device/rss/rss.html','us'),
	('cnbc','http://www.cnbc.com/id/19832390/device/rss/rss.html','world'),
	('cnbc','http://www.cnbc.com/id/19794221/device/rss/rss.html','world'),
	('cnbc','http://www.cnbc.com/id/10001147/device/rss/rss.html','finance'),
	('cnbc','http://www.cnbc.com/id/15839135/device/rss/rss.html','finance'),
	('cnbc','http://www.cnbc.com/id/100370673/device/rss/rss.html','opinion,politics,economy'),
	('cnbc','http://www.cnbc.com/id/20910258/device/rss/rss.html','finance'),
	('cnbc','http://www.cnbc.com/id/10000664/device/rss/rss.html','finance,technology'),
	('cnbc','http://www.cnbc.com/id/19854910/device/rss/rss.html','technology'),
	('cnbc','http://www.cnbc.com/id/10000113/device/rss/rss.html','politics'),
	('cnbc','http://www.cnbc.com/id/10000108/device/rss/rss.html','health'),
	('cnbc','http://www.cnbc.com/id/10000115/device/rss/rss.html','life'),
	('cnbc','http://www.cnbc.com/id/10001054/device/rss/rss.html','finance'),
	('cnbc','http://www.cnbc.com/id/10000101/device/rss/rss.html','life'),
	('cnbc','http://www.cnbc.com/id/19836768/device/rss/rss.html','finance,technology'),
	('cnbc','http://www.cnbc.com/id/10000110/device/rss/rss.html','entertainment'),
	('cnbc','http://www.cnbc.com/id/10000116/device/rss/rss.html','life,finance'),
	('cnbc','http://www.cnbc.com/id/10000739/device/rss/rss.html','life'),
	('cnbc','http://www.cnbc.com/id/44877279/device/rss/rss.html','finance,business'),
	('cnbc','http://www.cnbc.com/id/15839069/device/rss/rss.html','finance,business'),
	('cnbc','http://www.cnbc.com/id/100646281/device/rss/rss.html','finance'),
	('cnbc','http://www.cnbc.com/id/21324812/device/rss/rss.html','life,finance'),
	('cnbc','http://www.cnbc.com/id/23103686/device/rss/rss.html','opinion,finance'),
	('cnbc','http://www.cnbc.com/id/20409666/device/rss/rss.html','investing,business'),
	('cnbc','http://www.cnbc.com/id/38818154/device/rss/rss.html','business,opinion'),
	('nytimes','http://rss.nytimes.com/services/xml/rss/nyt/World.xml','world'),
	('nytimes','http://rss.nytimes.com/services/xml/rss/nyt/Africa.xml','world'),
	('nytimes','http://rss.nytimes.com/services/xml/rss/nyt/Americas.xml','us'),
	('nytimes','http://rss.nytimes.com/services/xml/rss/nyt/AsiaPacific.xml','world'),
	('nytimes','http://rss.nytimes.com/services/xml/rss/nyt/Europe.xml','world'),
	('nytimes','http://rss.nytimes.com/services/xml/rss/nyt/MiddleEast.xml','world'),
	('nytimes','http://rss.nytimes.com/services/xml/rss/nyt/US.xml','us'),
	('nytimes','http://rss.nytimes.com/services/xml/rss/nyt/Education.xml','politics,education'),
	('nytimes','http://rss.nytimes.com/services/xml/rss/nyt/Politics.xml','politics'),
	('nytimes','http://rss.nytimes.com/services/xml/rss/nyt/Business.xml','business'),
	('nytimes','http://rss.nytimes.com/services/xml/rss/nyt/EnergyEnvironment.xml','technology'),
	('nytimes','http://rss.nytimes.com/services/xml/rss/nyt/SmallBusiness.xml','business,finance'),
	('nytimes','http://rss.nytimes.com/services/xml/rss/nyt/Economy.xml','finance'),
	('nytimes','http://rss.nytimes.com/services/xml/rss/nyt/Technology.xml','technology'),
	('nytimes','http://rss.nytimes.com/services/xml/rss/nyt/PersonalTech.xml','technology'),
	('nytimes','http://rss.nytimes.com/services/xml/rss/nyt/Sports.xml','sports'),
	('nytimes','http://rss.nytimes.com/services/xml/rss/nyt/Science.xml','science,technology'),
	('nytimes','http://rss.nytimes.com/services/xml/rss/nyt/Environment.xml','science,technology'),
	('nytimes','http://rss.nytimes.com/services/xml/rss/nyt/Space.xml','science,technology'),
	('nytimes','http://rss.nytimes.com/services/xml/rss/nyt/Health.xml','health'),
	('nytimes','http://rss.nytimes.com/services/xml/rss/nyt/Travel.xml','life'),
	('nytimes','http://rss.nytimes.com/services/xml/rss/nyt/FashionandStyle.xml','life'),
	('nytimes','http://rss.nytimes.com/services/xml/rss/nyt/Arts.xml','life'),
	('nytimes','http://rss.nytimes.com/services/xml/rss/nyt/Movies.xml','entertainment'),
	('nytimes','http://topics.nytimes.com/top/opinion/editorialsandoped/oped/contributors/index.html?rss=1','opinion'),
	('washpo','http://feeds.washingtonpost.com/rss/rss_election-2012','politics'),
	('washpo','http://feeds.washingtonpost.com/rss/rss_powerpost','politics'),
	('washpo','http://feeds.washingtonpost.com/rss/rss_fact-checker','politics'),
	('washpo','http://feeds.washingtonpost.com/rss/rss_the-fix','opinion,politics'),
	('washpo','http://feeds.washingtonpost.com/rss/rss_monkey-cage','opinion,politics'),
	('washpo','http://feeds.washingtonpost.com/rss/rss_act-four','entertainment'),
	('washpo','http://feeds.washingtonpost.com/rss/rss_achenblog','science,technology'),
	('washpo','http://feeds.washingtonpost.com/rss/rss_checkpoint','politics'),
	('washpo','http://feeds.washingtonpost.com/rss/rss_innovations','technology,future'),
	('washpo','http://feeds.washingtonpost.com/rss/rss_morning-mix','politics,us'),
	('washpo','http://feeds.washingtonpost.com/rss/rss_post-nation','politics,us'),
	('washpo','http://feeds.washingtonpost.com/rss/rss_speaking-of-science','science'),
	('washpo','http://feeds.washingtonpost.com/rss/rss_to-your-health','health'),
	('washpo','http://feeds.washingtonpost.com/rss/rss_blogpost','opinion,blog,politics'),
	('washpo','http://feeds.washingtonpost.com/rss/rss_digger','technology,future,politics'),
	('washpo','http://feeds.washingtonpost.com/rss/national/energy-environment','technology,science'),
	('washpo','http://feeds.washingtonpost.com/rss/rss_on-leadership','business,technology,politics'),
	('washpo','http://feeds.washingtonpost.com/rss/blogs/rss_the-switch','technology,politics'),
	('washpo','http://feeds.washingtonpost.com/rss/rss_wonkblog','politics,business'),
	('reuters','http://feeds.reuters.com/news/artsculture','life'),
	('reuters','http://feeds.reuters.com/reuters/businessNews','business'),
	('reuters','http://feeds.reuters.com/reuters/companyNews','business'),
	('reuters','http://feeds.reuters.com/reuters/entertainment','entertainment'),
	('reuters','http://feeds.reuters.com/reuters/environment','science'),
	('reuters','http://feeds.reuters.com/reuters/healthNews','health'),
	('reuters','http://feeds.reuters.com/reuters/lifestyle','life'),
	('reuters','http://feeds.reuters.com/news/wealth','finance'),
	('reuters','http://feeds.reuters.com/reuters/MostRead','top'),
	('reuters','http://feeds.reuters.com/reuters/peopleNews','life'),
	('reuters','http://feeds.reuters.com/Reuters/PoliticsNews','politics'),
	('reuters','http://feeds.reuters.com/reuters/scienceNews','science'),
	('reuters','http://feeds.reuters.com/reuters/sportsNews','sports'),
	('reuters','http://feeds.reuters.com/reuters/technologyNews','technology'),
	('reuters','http://feeds.reuters.com/reuters/topNews','top'),
	('reuters','http://feeds.reuters.com/Reuters/domesticNews','us'),
	('reuters','http://feeds.reuters.com/Reuters/worldNews','world'),
	('foxnews','http://feeds.foxnews.com/foxnews/latest','top'),
	('foxnews','http://feeds.foxnews.com/foxnews/most-popular','top'),
	('foxnews','http://feeds.foxnews.com/foxnews/entertainment','entertainment'),
	('foxnews','http://feeds.foxnews.com/foxnews/health','health'),
	('foxnews','http://feeds.foxnews.com/foxnews/section/lifestyle','life'),
	('foxnews','http://feeds.foxnews.com/foxnews/opinion','opinion'),
	('foxnews','http://feeds.foxnews.com/foxnews/politics','politics'),
	('foxnews','http://feeds.foxnews.com/foxnews/science','science'),
	('foxnews','http://feeds.foxnews.com/foxnews/sports','sports'),
	('foxnews','http://feeds.foxnews.com/foxnews/tech','technology'),
	('foxnews','http://feeds.foxnews.com/foxnews/national','us'),
	('foxnews','http://feeds.foxnews.com/foxnews/world','world'),
]

labels = {
	'cnn':'CNN',
	'cnbc':'CNBC',
	'nytimes':'New York Times',
	'washpo':'Washington Post',
	'reuters':'Reuters',
	'foxnews':'Fox News',
}

def default_categories():
	results = []
	for source, feed, categories in sources:
		for category in categories.split(','):
			if category not in results:
				results.append(category)
	results = sorted(results)
	return results

def default_feeds():
	for source, feed, categories in sources:
		yield feed

def default_sources():
	results = []
	for source, feed, categories in sources:
		result = ( source, labels[source] )
		if result not in results:
			results.append(result)
	results = sorted(results,key=lambda x: x[1])
	return results
