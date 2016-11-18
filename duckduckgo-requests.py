from bs4 import BeautifulSoup
import requests, unicodedata #, pyperclip

def searchDuckDuckGoFor(searchTerm):
	resultsText = []

	req = requests.get('https://www.duckduckgo.com/', params={'q': searchTerm})
	data = req.text

	soup = BeautifulSoup(data, 'lxml')
	# pyperclip.copy(soup)
	print soup

	# sts = soup.select(".st")

	# for st in sts:
	# 	text = unicodedata.normalize('NFKD', st.text).encode('ascii', 'ignore')
	# 	resultsText.append(text)

	# return resultsText

searchDuckDuckGoFor('waddap')