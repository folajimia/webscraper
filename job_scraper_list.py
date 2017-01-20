
#!

#the script searches for phrases you put in a and opens the top 5 results in your default tab
#to use enter  'python testJobScraper.py <search phrase>'

import requests, sys, webbrowser, bs4

#todo remove all unrequired text

print('seraching job index.....') #display text while downloading google text

#https://it.jobindex.dk/jobsoegning?page=1&subid=1&regionid=20


  # append  ('&tbs=qdr:w') to search for available results in the past 1 week. replace w with m for month 
#res.raise_for_status()

#print res
def job_pages(max_pages):
	page =1
	while page < max_pages:
		#add some other danish job sites
		res = requests.get ('https://it.jobindex.dk/jobsoegning?page='+ str(page) + '&subid=1&regionid=20')
# retrieve top search results links.
		soup = bs4.BeautifulSoup(res.text, "html.parser")
#linkElems = soup.select('.PaidJob a')
#open a browser tab for each result
#numOpen = min(5, len(linkElems))  #open in tab
		for link in soup.select('.PaidJob a'):
			if link.find('b'):
				href = "https://it.jobindex.dk/jobsoegning"+ str(link.get('href')) 
				title = link.string
				console_screen(href)
				open_tab(href)

				#todo - add options print to screen
				#- save to doc
				#- save to spreadsheet
				#- open in tab
	page +=1





def console_screen():
	print (href)
	print (title)


#funcion for tab opening
def open_tab(links):
	listLink=[]
	listLink.append(links)

	#store all links, but open the first 5

#	numOpen = min(5, len(links))

		


#todo- number of pages should be via input screen
print("How many pages do you want to scrape jobs from ?")
print("Please enter an integer:")	
noOfPages=input()
job_pages(int(noOfPages))

# add exception handling for nonintegers and all other undesirable input
#result_list_box > div > div.results.component--default > div:nth-child(1) > a:nth-child(2)
	
#	test = (linkElems[i].get('href'))
#	webbrowser.open('http://it.jobindex.dk' + linkElems[i].get('href'))
#print (test)


#TypeError: 'NoneType' object is not callable
