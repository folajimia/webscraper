
#!

#the script searches for phrases you put in a and opens the top 5 results in your default tab
#to use enter  'python testJobScraper.py <search phrase>'

import requests, sys, webbrowser, bs4

print('seraching job index.....') #display text while downloading google text
res = requests.get ('https://it.jobindex.dk/jobsoegning?q='+ ''.join(sys.argv[1:])+ '&subid=1&regionid=20')
#https://it.jobindex.dk/jobsoegning?page=1&subid=1&regionid=20


  # append  ('&tbs=qdr:w') to search for available results in the past 1 week. replace w with m for month 
res.raise_for_status()

#print res

# retrieve top search results links.
soup = bs4.BeautifulSoup(res.text,"html.parser")
linkElems = soup.select('.PaidJob a')
#open a browser tab for each result
numOpen = min(5, len(linkElems))
#for link in soup.findall('a','class':'item-name'):
for i in range(numOpen):
	
	test = (linkElems[i].get('href'))
	webbrowser.open('http://it.jobindex.dk' + linkElems[i].get('href'))
	print (test)


