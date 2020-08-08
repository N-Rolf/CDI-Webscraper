import re
import requests, bs4, webbrowser
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import *

#CITY OF BROOKINGS
brookingsBaseUrl = 'https://cityofbrookings.org/'

#import City of Brookings Bid Page
brkngsUrl = 'https://cityofbrookings.org/Bids.aspx?CatID=All&txtSort=Category&showAllBids=&Status='
brkngsPage = requests.get(brkngsUrl)

#beautifulSoup
brkngsSoup = BeautifulSoup(brkngsPage.content, 'html5lib')
brookingsActive = brkngsSoup.select('a[href*="bids.aspx"]')

brookTitles = []
brookSites = []
if len(brookingsActive) != 0:
	for element in brookingsActive:
		brookTitles.append(element.text)
		brookSites.append(brookingsBaseUrl + element.get('href'))	
		unwanted = [i for i, s in enumerate(brookingsActive) if 'Read\xa0on' in s]
	for ele in sorted(unwanted, reverse = True):
		del brookTitles[ele]
		del brookSites[ele]
else:
	brookTitles.append('none')
	brookSites.append('none')

#console progress
print("Brookings Done!" , len(brookTitles))
#tkinter
root = tk.Tk()
#root.geometry("900x400")

scroll_bar = Scrollbar(root, orient="vertical")
scroll_bar.grid(row=0, column=3, sticky='ns')

def openbrowser(val):
	webbrowser.open(val)

brookHeader = tk.Label(text="Brookings Open Projects")
brookHeader.grid(row=0, column=0)

for idx, val in enumerate(brookTitles):
	siteLabels = val
	siteLabels = tk.Label(text=val)
	siteLabels.grid(row=(idx), column=1)

for idx, val in enumerate(brookSites):
		siteButtons = tk.Button(text=val, command=lambda x=val: openbrowser(x))
		siteButtons.grid(row=(idx), column=2)

#CITY OF SIOUX FALLS
sfbaseUrl = 'siouxfalls.org'

#import Bid Page
siouxfallsUrl = 'https://www.siouxfalls.org/business/ntb'
siouxfallsPage = requests.get(siouxfallsUrl)

#beautifulSoup
siouxfallsSoup = BeautifulSoup(siouxfallsPage.content, 'html5lib')
sfactive = siouxfallsSoup.table.findAll("a")

sfTitles = []
sfSites = []
if len(sfactive) != 0:
	for element in sfactive:
		sfTitles.append(element.text)
		sfSites.append(sfbaseUrl + element.get('href'))
else:
	sfTitles.append('none')
	sfSites.append('none')

#console progress
print("Sioux Falls Done!" , len(sfTitles))
#ui counter
sfCount = (len(brookTitles))
runningcount = len(brookTitles)
print("sf count",sfCount, "running count", runningcount)
#tkinter
sfHeader = tk.Label(text="Sioux Falls Open Projects")
sfHeader.grid(row=runningcount, column=0)

for idx, val in enumerate(sfTitles):
	siteLabels = tk.Label(text=val)
	siteLabels.grid(row=(idx + runningcount), column=1)

for idx, val in enumerate(sfSites):
	siteButtons = tk.Button(text=val, command=lambda x=val: openbrowser(x))
	siteButtons.grid(row=(idx + runningcount), column=2)

#CITY OF WATERTOWN
watertownBaseUrl = 'https://watertown.us'

#import Bid Page
watertownUrl = 'https://www.watertownsd.us/Bids.aspx'
watertownPage = requests.get(watertownUrl)

#beautifulSoup
watertownSoup = BeautifulSoup(watertownPage.content, 'html5lib')
watertownActive = watertownSoup.select('a[href*="bids.aspx"]')

waterTitles = []
waterSites = []
if len(watertownActive) != 0:
	for element in watertownActive:
		waterTitles.append(element.text)
		waterSites.append(watertownBaseUrl + element.get('href'))
		unwanted = [i for i, s in enumerate(watertownActive) if 'Read\xa0on' in s]
	for ele in sorted(unwanted, reverse = True):
		del waterTitles[ele]
		del waterSites[ele]
else:
	waterTitles.append('none')
	waterSites.append('none')

#console progress
print("Watertown Done!" , len(waterTitles))
#ui counter
waterCount = \
(len(brookTitles) \
+ len(sfTitles))

runningcount += len(sfTitles)
print("water count",waterCount,  "running count", runningcount)
#tkinter
waterHeader = tk.Label(text="Watertown Open Projects")
waterHeader.grid(row=runningcount, column=0)

for idx, val in enumerate(waterTitles):
	siteLabels = tk.Label(text=val)
	siteLabels.grid(row=(idx + runningcount), column=1)

for idx, val in enumerate(waterSites):
	siteButtons = tk.Button(text=val, command=lambda x=val: openbrowser(x))
	siteButtons.grid(row=(idx + runningcount), column=2)

#CITY OF ABERDEEN
aberdeenBaseUrl = 'https://aberdeen.sd.us/'

#import Bid Page
aberdeenUrl = 'https://www.aberdeen.sd.us/Bids.aspx'
aberdeenPage = requests.get(aberdeenUrl)

#beautifulSoup
aberdeenSoup = BeautifulSoup(aberdeenPage.content, 'html5lib')
aberdeenActive = aberdeenSoup.select('a[href*="bids.aspx"]')

aberTitles = []
aberSites = []
if len(aberdeenActive) != 0:
	for element in aberdeenActive:
		aberTitles.append(element.text)
		aberSites.append(aberdeenBaseUrl + element.get('href'))
		unwanted = [i for i, s in enumerate(aberdeenActive) if 'Read\xa0on' in s]
	for ele in sorted(unwanted, reverse = True):
		del aberTitles[ele]
		del aberSites[ele]
else:
	aberTitles.append('none')
	aberSites.append('none')

#console progress
print("Aberdeen Done!" , len(aberTitles))
#ui counter
aberCount = \
(len(brookTitles) \
+ len(sfTitles) \
+ len(waterTitles))

runningcount += len(waterTitles)
print("aber count",aberCount, "running count", runningcount)
#tkinter
aberHeader = tk.Label(text="Aberdeen Open Projects")
aberHeader.grid(row=runningcount, column=0)

for idx, val in enumerate(aberTitles):
	siteLabels = tk.Label(text=val)
	siteLabels.grid(row=(idx + runningcount), column=1)

for idx, val in enumerate(aberSites):
	siteButtons = tk.Button(text=val, command=lambda x=val: openbrowser(x))
	siteButtons.grid(row=(idx + runningcount), column=2)

#CITY OF HURON
huronBaseUrl = 'https://huronsd.com'

#import Bid Page
huronUrl = 'https://www.huronsd.com/bids'
huronPage = requests.get(huronUrl)

#beautifulSoup
huronSoup = BeautifulSoup(huronPage.content, 'html5lib')
huronActive = huronSoup.select('a[href*="bids/view/id"]')

huronTitles = []
huronSites = []
huronList = []

yearNumRegex = re.compile(r'\d{4}-\d{2}') #wtf huron

if len(huronActive) != 0:
	for element in huronActive:
		huronList.append(element.text + ", " + huronBaseUrl + element.get('href'))
		huronTitles.append(element.text)
		huronSites.append(huronBaseUrl + element.get('href'))
		unwanted = [i for i, word in enumerate(huronList) if re.search(yearNumRegex, word)] #idk why this works
	for ele in sorted(unwanted, reverse = True):
		del huronTitles[ele]
		del huronSites[ele]
else:
	huronTitles.append('none')
	huronSites.append('none')

#console progress
print("Huron Done!" , len(huronTitles))
#ui counter
huronCount = \
(len(brookTitles) \
+ len(sfTitles) \
+ len(waterTitles) \
+ len(aberTitles))
#tkinter
huronHeader = tk.Label(text="Huron Open Projects")
huronHeader.grid(row=huronCount, column=0)

for idx, val in enumerate(huronTitles):
	siteLabels = tk.Label(text=val)
	siteLabels.grid(row=(idx + huronCount), column=1)

for idx, val in enumerate(huronSites):
	siteButtons = tk.Button(text=val, command=lambda x=val: openbrowser(x))
	siteButtons.grid(row=(idx + huronCount), column=2)

#CITY OF PIERRE
pierreBaseUrl = 'https://cityofpierre.org/'

#import Bid Page
pierreUrl = 'https://www.cityofpierre.org/Bids.aspx'
pierrePage = requests.get(pierreUrl)

#beautifulSoup
pierreSoup = BeautifulSoup(pierrePage.content, 'html5lib')

pierreActive = pierreSoup.select('a[href*="bids.aspx"]')

pierreTitles = []
pierreSites = []

if len(pierreActive) != 0:
	for element in pierreActive:
		pierreTitles.append(element.text)
		pierreSites.append(pierreBaseUrl + element.get('href'))
		unwanted = [i for i, s in enumerate(pierreActive) if 'Read\xa0on' in s]
	for ele in sorted(unwanted, reverse = True):
		del pierreTitles[ele]
		del pierreSites[ele]
else:
	pierreTitles.append('none')
	pierreSites.append('none')

#console progress
print("Peirre Done!" , len(pierreTitles))
#ui counter
pierreCount = \
(len(brookTitles) \
+ len(sfTitles) \
+ len(waterTitles) \
+ len(aberTitles) \
+ len(huronTitles))
#tkinter
pierreHeader = tk.Label(text="Pierre Open Projects")
pierreHeader.grid(row=pierreCount, column=0)

for idx, val in enumerate(pierreTitles):
	siteLabels = tk.Label(text=val)
	siteLabels.grid(row=(idx + pierreCount), column=1)

for idx, val in enumerate(pierreSites):
	siteButtons = tk.Button(text=val, command=lambda x=val: openbrowser(x))
	siteButtons.grid(row=(idx + pierreCount), column=2)

#CITY OF MITCHELL
mitchellBaseUrl = 'https://www.cityofmitchell.org/'

#import Bid Page
mitchellUrl = 'https://www.cityofmitchell.org/Bids.aspx'
mitchellPage = requests.get(mitchellUrl)

#beautifulSoup
mitchellSoup = BeautifulSoup(mitchellPage.content, 'html5lib')

mitchellActive = mitchellSoup.select('a[href*="bids.aspx"]')

mitchellTitles = []
mitchellSites = []
if len(mitchellActive) != 0:
	for element in mitchellActive:
		mitchellTitles.append(element.text)
		mitchellSites.append(mitchellBaseUrl + element.get('href'))
		unwanted = [i for i, s in enumerate(mitchellActive) if 'Read\xa0on' in s]
	for ele in sorted(unwanted, reverse = True):
		del mitchellTitles[ele]
		del mitchellSites[ele]
else:
	mitchellTitles.append('none')
	mitchellSites.append('none')

#console progress
print("Mitchell Done!" , len(mitchellTitles))
#ui counter
mitchellCount = \
(len(brookTitles) \
+ len(sfTitles) \
+ len(waterTitles) \
+ len(aberTitles) \
+ len(huronTitles) \
+ len(pierreTitles))
#tkinter
mitchellHeader = tk.Label(text="Mitchell Open Projects")
mitchellHeader.grid(row=mitchellCount, column=0)

for idx, val in enumerate(mitchellTitles):
	siteLabels = tk.Label(text=val)
	siteLabels.grid(row=(idx + mitchellCount), column=1)

for idx, val in enumerate(mitchellSites):
	siteButtons = tk.Button(text=val, command=lambda x=val: openbrowser(x))
	siteButtons.grid(row=(idx + mitchellCount), column=2)

#CITY OF YANKTON
yanktonBaseUrl = 'https://www.cityofyankton.org/'

#import Bid Page
yanktonUrl = 'http://www.cityofyankton.org/how-do-i/bid-rfp-posts-list/-selsta-4'
yanktonPage = requests.get(yanktonUrl)

#beautifulSoup
yanktonSoup = BeautifulSoup(yanktonPage.content, 'html5lib')

yanktonActive = yanktonSoup.select('a[href*="Components/RFP"]')

yanktonTitles = []
yanktonSites = []
if len(yanktonActive) != 0:
	for element in yanktonActive:
		yanktonTitles.append(element.text)
		yanktonSites.append(yanktonBaseUrl + element.get('href'))
else:
	yanktonTitles.append('none')
	yanktonSites.append('none')

#console progress
print("Yankton Done!" , len(yanktonTitles))
#ui counter
yanktonCount = \
(len(brookTitles) \
+ len(sfTitles) \
+ len(waterTitles) \
+ len(aberTitles) \
+ len(huronTitles) \
+ len(pierreTitles) \
+ len(mitchellTitles))
#tkinter
yanktonHeader = tk.Label(text="Yankton Open Projects")
yanktonHeader.grid(row=yanktonCount, column=0)

for idx, val in enumerate(yanktonTitles):
	siteLabels = tk.Label(text=val)
	siteLabels.grid(row=(idx + yanktonCount), column=1)

for idx, val in enumerate(yanktonSites):
	siteButtons = tk.Button(text=val, command=lambda x=val: openbrowser(x))
	siteButtons.grid(row=(idx + yanktonCount), column=2)

#CITY OF SPEARFISH
spearfishBaseUrl = 'https://www.cityofspearfish.com/'

#import Bid Page
spearfishUrl = 'https://www.cityofspearfish.com/Bids.aspx'
spearfishPage = requests.get(spearfishUrl)

#beautifulSoup
spearfishSoup = BeautifulSoup(spearfishPage.content, 'html5lib')

spearfishActive = spearfishSoup.select('a[href*="bids.aspx"]')

spearfishTitles = []
spearfishSites = []
if len(spearfishActive) != 0:
	for element in spearfishActive:
		spearfishTitles.append(element.text)
		spearfishSites.append(spearfishBaseUrl + element.get('href'))
		unwanted = [i for i, s in enumerate(spearfishActive) if 'Read\xa0on' in s]
	for ele in sorted(unwanted, reverse = True):
		del spearfishTitles[ele]
		del spearfishSites[ele]
else:
	spearfishTitles.append('none')
	spearfishSites.append('none')

#console progress
print("Spearfish Done!" , len(spearfishTitles))
#ui counter
spearfishCount = \
(len(brookTitles) \
+ len(sfTitles) \
+ len(waterTitles) \
+ len(aberTitles) \
+ len(huronTitles) \
+ len(pierreTitles) \
+ len(mitchellTitles) \
+ len(yanktonTitles))
#tkinter
spearfishHeader = tk.Label(text="Spearfish Open Projects")
spearfishHeader.grid(row=spearfishCount, column=0)

for idx, val in enumerate(spearfishTitles):
	siteLabels = tk.Label(text=val)
	siteLabels.grid(row=(idx + spearfishCount), column=1)

for idx, val in enumerate(spearfishSites):
	siteButtons = tk.Button(text=val, command=lambda x=val: openbrowser(x))
	siteButtons.grid(row=(idx + spearfishCount), column=2)

#CITY OF VERMILLION
vermillionBaseUrl = 'https://www.vermillion.us/'

#import Bid Page
vermillionUrl = 'https://www.vermillion.us/Bids.aspx'
vermillionPage = requests.get(vermillionUrl)

#beautifulSoup
vermillionSoup = BeautifulSoup(vermillionPage.content, 'html5lib')

vermillionActive = vermillionSoup.select('a[href*="bids.aspx"]')

vermillionTitles = []
vermillionSites = []
if len(vermillionActive) != 0:
	for element in vermillionActive:
		vermillionTitles.append(element.text)
		vermillionSites.append(vermillionBaseUrl + element.get('href'))
		unwanted = [i for i, s in enumerate(vermillionActive) if 'Read\xa0on' in s]
	for ele in sorted(unwanted, reverse = True):
		del vermillionTitles[ele]
		del vermillionSites[ele]
else:
	vermillionTitles.append('none')
	vermillionSites.append('none')

#console progress
print("Vermillion Done!" , len(vermillionTitles))
#ui counter
vermillionCount = \
(len(brookTitles) \
+ len(sfTitles) \
+ len(waterTitles) \
+ len(aberTitles) \
+ len(huronTitles) \
+ len(pierreTitles) \
+ len(mitchellTitles) \
+ len(yanktonTitles) \
+ len(spearfishTitles))
#tkinter
vermillionHeader = tk.Label(text="Vermillion Open Projects")
vermillionHeader.grid(row=vermillionCount, column=0)

for idx, val in enumerate(vermillionTitles):
	siteLabels = tk.Label(text=val)
	siteLabels.grid(row=(idx + vermillionCount), column=1)

for idx, val in enumerate(vermillionSites):
	siteButtons = tk.Button(text=val, command=lambda x=val: openbrowser(x))
	siteButtons.grid(row=(idx + vermillionCount), column=2)

#CITY OF MADISON
madisonBaseUrl = 'https://www.cityofmadisonsd.com/'

#import Bid Page
madisonUrl = 'https://cityofmadisonsd.com/resources/bids'
madisonPage = requests.get(madisonUrl)

#beautifulSoup
madisonSoup = BeautifulSoup(madisonPage.content, 'html5lib')
madisonActive = madisonSoup.table.findAll("a")

madisonTitles = []
madisonSites = []

if len(madisonActive) != 0:
	for element in madisonActive:
		madisonTitles.append(element.text)
		madisonSites.append(madisonBaseUrl + element.get('href'))
else:
	madisonTitles.append('none')
	madisonSites.append('none')

#console progress
print("Madison Done!" , len(madisonTitles))
#ui counter
madisonCount = \
(len(brookTitles) \
+ len(sfTitles) \
+ len(waterTitles) \
+ len(aberTitles) \
+ len(huronTitles) \
+ len(pierreTitles) \
+ len(mitchellTitles) \
+ len(yanktonTitles) \
+ len(spearfishTitles) \
+ len(vermillionTitles))
#tkinter
madisonHeader = tk.Label(text="Madison Open Projects")
madisonHeader.grid(row=madisonCount, column=0)

for idx, val in enumerate(madisonTitles):
	siteLabels = tk.Label(text=val)
	siteLabels.grid(row=(idx + madisonCount), column=1)

for idx, val in enumerate(madisonSites):
	siteButtons = tk.Button(text=val, command=lambda x=val: openbrowser(x))
	siteButtons.grid(row=(idx + madisonCount), column=2)

#South Dakota Game Fish & Parks
sdgfpBaseUrl = 'https://gfp.sd.gov/'

#import Bid Page
sdgfpUrl = 'https://gfp.sd.gov/bids-contracts/'
sdgfpPage = requests.get(sdgfpUrl)

#beautifulSoup
sdgfpSoup = BeautifulSoup(sdgfpPage.content, 'html5lib')
sdgfpActive = sdgfpSoup.table.findAll("a")

sdgfpTitles = []
sdgfpSites = []
if len(sdgfpActive) != 0:
	for element in sdgfpActive:
		sdgfpTitles.append(element.text)
		sdgfpSites.append(sdgfpBaseUrl + element.get('href'))
		unwanted = [i for i, s in enumerate(sdgfpActive) if 'Yes' in s]
	for ele in sorted(unwanted, reverse = True):
		del sdgfpTitles[ele]
		del sdgfpSites[ele]
else:
	sdgfpTitles.append('none')
	sdgfpSites.append('none')

#console progress
print("SD Game Fish & Parks Done!" , len(sdgfpTitles))
#ui counter
sdgfpCount = \
(len(brookTitles) \
+ len(sfTitles) \
+ len(waterTitles) \
+ len(aberTitles) \
+ len(huronTitles) \
+ len(pierreTitles) \
+ len(mitchellTitles) \
+ len(yanktonTitles) \
+ len(spearfishTitles) \
+ len(vermillionTitles) \
+ len(madisonTitles))
#tkinter
sdgfpHeader = tk.Label(text="SD Game Fish & Parks Open Projects")
sdgfpHeader.grid(row=sdgfpCount, column=0)

for idx, val in enumerate(sdgfpTitles):
	siteLabels = tk.Label(text=val)
	siteLabels.grid(row=(idx + sdgfpCount), column=1)

for idx, val in enumerate(sdgfpSites):
	siteButtons = tk.Button(text=val, command=lambda x=val: openbrowser(x))
	siteButtons.grid(row=(idx + sdgfpCount), column=2)


root.mainloop()

