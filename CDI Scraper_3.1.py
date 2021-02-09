import re
import requests, bs4, webbrowser
from multiprocessing import Pool
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk

#function definitions_________________________________________

def _stringScraper(url, query, soupstring):
	try:
		page = requests.get(url + query)
	except ConnectionError:
		pass

	soup = BeautifulSoup(page.content, 'html5lib')
	active = soup.select(r'a[href*="' + soupstring + '"]')               #searches for string within <a hyperlink tag

	titles = []
	sites = []
	if len(active) > 0:
		for elem in active:
			if 'Read\xa0on' not in elem:
				titles.append(elem.text)
				sites.append(url + elem.get('href'))
	else:
		titles.append('none')
		sites.append('none')
	count = len(sites)
	return titles, sites, count

def _otherScraper(url, query):		#sioux falls
	try:
		page = requests.get(url + query)
	except ConnectionError:
		pass

	soup = BeautifulSoup(page.content, 'html5lib')
	active = soup.table.findAll("a")                                 #searches for all <a hyperlink tags

	titles = []
	sites = []
	if len(active) > 0:
		for elem in active:
			titles.append(elem.text)
			sites.append(url + elem.get('href'))
	else:
		titles.append('none')
		sites.append('none')
	count = len(sites)
	return titles, sites, count

def _sdgfpScraper(url, query):		#sd game fish parks
	try:
		page = requests.get(url + query)
	except ConnectionError:
		pass

	soup = BeautifulSoup(page.content, 'html5lib')
	active = soup.table.findAll("a")                                 #searches for all <a hyperlink tags

	titles = []
	sites = []
	if len(active) > 0:
		for elem in active:
			titles.append(elem.text)
			sites.append(url + elem.get('href'))
			unwanted = [i for i, s in enumerate(active) if 'Yes' in s]
		for ele in sorted(unwanted, reverse = True):
			del titles[ele]
			del sites[ele]
	else:
		titles.append('none')
		sites.append('none')
	count = len(sites)
	return titles, sites, count

def _huronScraper(url, query):		#unique regex filter
	try:
		page = requests.get(url + query)
	except ConnectionError:
		pass

	soup = BeautifulSoup(page.content, 'html5lib')
	active = soup.select('a[href*="bids/view/id"]')

	titles = []
	sites = []
	sitelist = []

	yearNumRegex = re.compile(r'\d{4}-\d{2}')		#finds yyyy-mm date format 

	if len(active) > 0:
		for element in active:
			sitelist.append(element.text + ", " + (url + element.get('href')))
	
			unwanted = [i for i, word in enumerate(sitelist) if re.search(yearNumRegex, word)] #if yyyy-mm in element, add to index
		for ele in sorted(unwanted, reverse = True):
			del sitelist[ele]
		#print(*sitelist, sep = "\n")
	else:
		titles.append('none')
		sites.append('none')
	count = len(sites)
	return titles, sites, count

#tkinter____________________________________________

root = tk.Tk()
container = ttk.Frame(root)
canvas = tk.Canvas(container, width=920, height=920)
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

#tells canvas how large frame will be, triggers when scrollable_frame changes size
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)
#tells canvas to draw scrollable_frame inside itself
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
#when y position changes, scrollbar moves
canvas.configure(yscrollcommand=scrollbar.set)

#tk functions
def openbrowser(val):
	webbrowser.open(val)

def _publish(titles,sites,count):
	for idx, val in enumerate(titles):
		siteLabels = val
		siteLabels = ttk.Label(scrollable_frame, text=val, width=100, justify='left')
		siteLabels.grid(row=(idx + count), column=1, padx=(4,4))

	for idx, val in enumerate(sites):
		siteButtons = ttk.Button(scrollable_frame, text="Open", command=lambda x=val: openbrowser(x))
		siteButtons.grid(row=(idx + count), column=2)

def _header(city, count):
	header = ttk.Label(scrollable_frame, text= city)
	header.grid(row=count, column=0)

container.pack()
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

#"main"____________________________________________

if __name__ == '__main__':
	brookingsURL = 'https://cityofbrookings.org/'
	brookingsQuery = 'Bids.aspx?CatID=All&txtSort=Category&showAllBids=&Status='

	siouxfallsURL = 'https://www.siouxfalls.org/'
	siouxfallsQuery = 'business/ntb'

	aberdeenURL = 'https://aberdeen.sd.us/'
	aberdeenQuery = 'Bids.aspx'

	watertownURL = 'https://watertownsd.us/'
	watertownQuery = 'Bids.aspx'

	huronURL = 'https://huronsd.com/'
	huronQuery = 'bids'

	pierreURL = 'https://cityofpierre.org/'
	pierreQuery = 'Bids.aspx'

	mitchellURL = 'https://www.cityofmitchell.org/'
	mitchellQuery = 'Bids.aspx'

	yanktonURL = 'https://www.cityofyankton.org/'
	yanktonQuery = 'how-do-i/bid-rfp-posts-list/-selsta-4'

	spearfishURL = 'https://www.cityofspearfish.com/'
	spearfishQuery = 'Bids.aspx'

	vermillionURL = 'https://www.vermillion.us/'
	vermillionQuery = 'Bids.aspx'

	madisonURL = 'https://www.cityofmadisonsd.com/'
	madisonQuery = 'resources/bids'

	sdgfpURL = 'https://gfp.sd.gov/'
	sdgfpQuery = 'bids-contracts/'

	uicount = 0

	print('--- Brookings ---')
	name = "City of Brookings, SD"
	aspxString = "bids.aspx"
	t, s, c = _stringScraper(brookingsURL, brookingsQuery, aspxString)
	_header(name, uicount)
	_publish(t,s,uicount)
	uicount += c

	print('--- Sioux Falls ---')	#uses .findAll('a') , no unwanted
	name = "City of Sioux Falls, SD"
	t, s, c = _otherScraper(siouxfallsURL, siouxfallsQuery)
	_header(name, uicount)
	_publish(t,s,uicount)
	uicount += c

	print('--- Aberdeen ---')
	name = "City of Aberdeen, SD"
	t, s, c = _stringScraper(aberdeenURL, aberdeenQuery, aspxString)
	_header(name, uicount)
	_publish(t,s,uicount)
	uicount += c

	print('--- Watertown ---')
	name = "City of Watertown, SD"
	t, s, c = _stringScraper(watertownURL, watertownQuery, aspxString)
	_header(name, uicount)
	_publish(t,s,uicount)
	uicount += c

	print('--- Huron ---')		#uses .select('a[href*='bids/view/id']') , some regex to filter out redundant year links
	name = "City of Huron, SD"
	t, s, c = _huronScraper(huronURL, huronQuery)
	_header(name, uicount)
	_publish(t,s,uicount)
	uicount += c

	print('--- Pierre ---')
	name = "City of Pierre, SD"
	t, s, c = _stringScraper(pierreURL, pierreQuery, aspxString)
	_header(name, uicount)
	_publish(t,s,uicount)
	uicount += c

	print('--- Mitchell ---')
	name = "City of Mitchell, SD"
	t, s, c = _stringScraper(mitchellURL, mitchellQuery, aspxString)
	_header(name, uicount)
	_publish(t,s,uicount)
	uicount += c

	print('--- Yankton ---')	#uses .select('a[href*="Components/RFP"]') , no unwanted
	name = "City of Yankton, SD"
	yanktonString = "Components/RFP"
	t, s, c = _stringScraper(yanktonURL, yanktonQuery, yanktonString)
	_header(name, uicount)
	_publish(t,s,uicount)
	uicount += c

	print('--- Spearfish ---')
	name = "City of Spearfish, SD"
	t, s, c = _stringScraper(spearfishURL, spearfishQuery, aspxString)
	_header(name, uicount)
	_publish(t,s,uicount)
	uicount += c

	print('--- Vermillion ---')
	name = "City of Vermillion, SD"
	t, s, c = _stringScraper(vermillionURL, vermillionQuery, aspxString)
	_header(name, uicount)
	_publish(t,s,uicount)
	uicount += c

	print('--- Madison ---')	#uses .findAll('a') , no unwanted
	name = "City of Madison, SD"
	t, s, c = _otherScraper(madisonURL, madisonQuery)
	_header(name, uicount)
	_publish(t,s,uicount)
	uicount += c

	print('--- SD Game Fish & Parks ---')	#uses .findAll('a') , 'Yes'
	name = "SD Game Fish & Parks"
	t, s, c = _sdgfpScraper(sdgfpURL, sdgfpQuery)
	_header(name, uicount)
	_publish(t,s,uicount)
	uicount += c

root.mainloop()

