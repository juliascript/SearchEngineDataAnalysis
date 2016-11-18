from watson_developer_cloud import ToneAnalyzerV3
from bs4 import BeautifulSoup
import requests, unicodedata, json

def searchGoogleFor(searchTerm):
	# routing through sweden 
	proxies = { 'http': 'socks5://<USERNAME/>:<PASSWORD/>@184.75.221.138:1085',
				'https': 'socks5://<USERNAME/>:<PASSWORD/>@184.75.221.138:1090'}

	req = requests.get('https://www.google.com/search', params={'q': searchTerm}, proxies=proxies)

	data = req.text

	soup = BeautifulSoup(data, 'lxml')
	
	summaries = soup.select(".st")

	resultsText = []
	for t in summaries:
		# encode text from unicode to ascii
		text = unicodedata.normalize('NFKD', t.text).encode('ascii', 'ignore')
		resultsText.append(text)

	return resultsText

def getToneAnalysisFor(textArray):
	tone_analyzer = ToneAnalyzerV3(
	   username='<USERNAME/>',
	   password='<PASSWORD/>',
	   version='2016-05-19 ')
	analysis = []
	for text in textArray:
		analysis.append(tone_analyzer.tone(text=text))
	return analysis
	# if you want json ... 
	# return (json.dumps(analysis, indent=2))

results = searchGoogleFor('make school')
print getToneAnalysisFor(results), '\n'



