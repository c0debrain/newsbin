import requests
from lxml import html
from lxml import etree
from lxml.cssselect import CSSSelector
from unidecode import unidecode

class Filter:

    def __init__( self, *args, **kwargs ):
        """Filter article text from news websites.

        This class should be initialized with a string containing a comma separated
        series of valid CSS3 selectors that represent the top-level blocks from which
        to capture plain text.

        Keyword arguments:
            (str)   css:            CSS3 selector   (required)
            (tuple) whitelist:      HTML tags       (optional)
            (tuple) attr_whitelist: Attribute names (optional)

        """

        # we need css selectors in order to parse articles
        self.css = CSSSelector( kwargs['css'] )

        # the whitelist is for child elements we want to retain
        # html for
        self.whitelist = kwargs.get('whitelist',('a','b','i','em','cite','br'))

        # attribute whitelist- other attributes on whitelisted
        # elements are discarded by __process
        self.attr_whitelist = kwargs.get('attr_whitelist',('href'))

    def __call__( self, document, url ):
        """Filter article content from raw html"""
        # turn the raw html into an etree
        root = html.fromstring(document)
        root.make_links_absolute(url)

        content = []

        # if we have a selector and a whitelist
        # then we can work.
        if self.css and self.whitelist:

            # get each matching block that we want
            # the text from
            for block in self.css(root):

                # parse out the text and whitelisted html
                para = self.__parse(block)

                # if we got something, keep it
                if para: content.append( para )

        # return a list of paragraphs
        return content

    def __parse( self, block ):
        """Parse a single top-level block"""

        # if there is leading text, get it, otherwise empty
        if block.text:
            result = unidecode(block.text)
        else:
            result = ''

        # for each child element in the block-
        for child in block:

            # if we want to keep the html, then strip the attributes (__process)
            # and convert to a string.
            if child.tag in self.whitelist:
                result += unidecode( etree.tostring( self.__process(child), with_tail=False, encoding='unicode', method='html' ) )
            else:
                result += child.text_content()

            # if there is trailing text, decode and append it
            if child.tail and child.tail.strip():
                result += unidecode( child.tail )

        return result.strip()

    def __subparse( self, element ):
        pass

    def __process( self, element ):
        """Process attributes of a link"""

        # if we haven't determined that we want
        # the attribute, get rid of it.
        for attr in element.attrib:
            if attr not in self.attr_whitelist:
                element.attrib.pop(attr)

        # return the element
        return element

cnn = Filter(css='.zn-body__paragraph, #storytext p')
cnbc = Filter(css='div[itemprop=articleBody]>p, .article-body>p')
nytimes = Filter(css='.story-body-text.story-content')
washpo = Filter(css='article[itemprop=articleBody]>p, .row .span8>p:not(.interstitial-link), article.pg-article>p:not(.interstitial-link)')
reuters = Filter(css='#article-text>p, #article-text>.article-prime')
foxnews = Filter(css='.article-text>p')

if __name__=='__main__':
    url = 'http://feeds.reuters.com/~r/reuters/technologyNews/~3/wNCD-j_Snc0/us-facebook-television-idUSKBN19H0GJ'
    doc = requests.get(url).text
    f = reuters(doc,url=url)
    print('<style>p{ width:500px; }</style>')
    for p in f:
        print('<p>{}</p>\n'.format(p))
