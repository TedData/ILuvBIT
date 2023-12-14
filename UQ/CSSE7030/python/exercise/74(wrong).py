from html.parser import HTMLParser
import urllib
import urllib.request

class LinkParser(HTMLParser):
	def __init__(self):
		self._urls=[]
	def handle_starttag(self,tag,attrs):
		if tag=='a':
			for key, value in attrs:
				if key == 'href':
					print(value)
			print(tag, attrs)
def find_links(url):
	fd = urllib.request.urlopen(url)
	text = fd.read()
	fd.close()
	parser = LinkParser()
	parser.feed(str(text))
	return None

find_links('https://google.com')