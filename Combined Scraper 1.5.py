import requests
import bs4
import csv
import urllib3
import re
from bs4 import BeautifulSoup

#CITY OF BROOKINGS
brookingsBaseUrl = 'https://cityofbrookings.org/'

#import City of Brookings Bid Page
brkngsUrl = 'https://cityofbrookings.org/Bids.aspx?CatID=All&txtSort=Category&showAllBids=&Status='
brkngsPage = requests.get(brkngsUrl)

#error checks
#print(type(brkngsPage))
#print(brkngsPage.status_code == requests.codes.ok)
#print(len(brkngsPage.text))

#beautifulSoup
brkngsSoup = BeautifulSoup(brkngsPage.content, 'html5lib')
brookingsActive = brkngsSoup.select('a[href*="bids.aspx"]')

print("Brookings Open Projects:")
brooklist = []
if len(brookingsActive) != 0:
	for element in brookingsActive:
		brooklist.append(element.text + ", " + (brookingsBaseUrl + element.get('href')))
	
		unwanted = [i for i, s in enumerate(brookingsActive) if 'Read\xa0on' in s]
	for ele in sorted(unwanted, reverse = True):
		del brooklist[ele]
	print(*brooklist, sep = "\n")
else:
	print('none')

print('\n')
#CITY OF SIOUX FALLS
sfbaseUrl = 'siouxfalls.org'

#import Bid Page
siouxfallsUrl = 'https://www.siouxfalls.org/business/ntb'
siouxfallsPage = requests.get(siouxfallsUrl)

#beautifulSoup
siouxfallsSoup = BeautifulSoup(siouxfallsPage.content, 'html5lib')
sfactive = siouxfallsSoup.table.findAll("a")

print("Sioux Falls Open Projects:")
if len(sfactive) != 0:
	for element in sfactive:
		print(element.text + ", " + (sfbaseUrl + element.get('href')))
else:
	print('none')

print('\n')
#CITY OF WATERTOWN
watertownBaseUrl = 'https://watertown.us'

#import Bid Page
watertownUrl = 'https://www.watertownsd.us/Bids.aspx'
watertownPage = requests.get(watertownUrl)

#beautifulSoup
watertownSoup = BeautifulSoup(watertownPage.content, 'html5lib')
watertownActive = watertownSoup.select('a[href*="bids.aspx"]')

print("Watertown Open Projects:")
waterlist = []
if len(watertownActive) != 0:
	for element in watertownActive:
		waterlist.append(element.text + ", " + (watertownBaseUrl + element.get('href')))
	
		unwanted = [i for i, s in enumerate(watertownActive) if 'Read\xa0on' in s]
	for ele in sorted(unwanted, reverse = True):
		del waterlist[ele]
	print(*waterlist, sep = "\n")
else:
	print('none')

print('\n')
#CITY OF ABERDEEN
aberdeenBaseUrl = 'https://aberdeen.sd.us/'

#import Bid Page
aberdeenUrl = 'https://www.aberdeen.sd.us/Bids.aspx'
aberdeenPage = requests.get(aberdeenUrl)

#beautifulSoup
aberdeenSoup = BeautifulSoup(aberdeenPage.content, 'html5lib')
aberdeenActive = aberdeenSoup.select('a[href*="bids.aspx"]')

print("Aberdeen Open Projects:")
aberlist = []
if len(aberdeenActive) != 0:
	for element in aberdeenActive:
		aberlist.append(element.text + ", " + (aberdeenBaseUrl + element.get('href')))
	
		unwanted = [i for i, s in enumerate(aberdeenActive) if 'Read\xa0on' in s]
	for ele in sorted(unwanted, reverse = True):
		del aberlist[ele]
	print(*aberlist, sep = "\n")
else:
	print('none')

print('\n')
#CITY OF HURON
huronBaseUrl = 'https://huronsd.com'

#import Bid Page
huronUrl = 'https://www.huronsd.com/bids'
huronPage = requests.get(huronUrl)

#beautifulSoup
huronSoup = BeautifulSoup(huronPage.content, 'html5lib')
huronActive = huronSoup.select('a[href*="bids/view/id"]')

huronlist = []

yearNumRegex = re.compile(r'\d{4}-\d{2}')

print("Huron Open Projects:")
if len(huronActive) != 0:
	for element in huronActive:
		huronlist.append(element.text + ", " + (huronBaseUrl + element.get('href')))
	
		unwanted = [i for i, word in enumerate(huronlist) if re.search(yearNumRegex, word)] #idk why this works
	for ele in sorted(unwanted, reverse = True):
		del huronlist[ele]
	print(*huronlist, sep = "\n")
else:
	print('none')

print('\n')
#CITY OF PIERRE
pierreBaseUrl = 'https://cityofpierre.org/'

#import Bid Page
pierreUrl = 'https://www.cityofpierre.org/Bids.aspx'
pierrePage = requests.get(pierreUrl)

#beautifulSoup
pierreSoup = BeautifulSoup(pierrePage.content, 'html5lib')

pierreActive = pierreSoup.select('a[href*="bids.aspx"]')

print("Pierre Open Projects:")
pierreList = []
if len(pierreActive) != 0:
	for element in pierreActive:
		pierreList.append(element.text + ", " + (pierreBaseUrl + element.get('href')))
	
		unwanted = [i for i, s in enumerate(pierreActive) if 'Read\xa0on' in s]
	for ele in sorted(unwanted, reverse = True):
		del pierreList[ele]
	print(*pierreList, sep = "\n")
else:
	print('none')

print('\n')
#CITY OF MITCHELL
mitchellBaseUrl = 'https://www.cityofmitchell.org/'

#import Bid Page
mitchellUrl = 'https://www.cityofmitchell.org/Bids.aspx'
mitchellPage = requests.get(mitchellUrl)

#beautifulSoup
mitchellSoup = BeautifulSoup(mitchellPage.content, 'html5lib')

mitchellActive = mitchellSoup.select('a[href*="bids.aspx"]')

print("Mitchell Open Projects:")
mitchellList = []
if len(mitchellActive) != 0:
	for element in mitchellActive:
		mitchellList.append(element.text + ", " + (mitchellBaseUrl + element.get('href')))
	
		unwanted = [i for i, s in enumerate(mitchellActive) if 'Read\xa0on' in s]
	for ele in sorted(unwanted, reverse = True):
		del mitchellList[ele]
	print(*mitchellList, sep = "\n")
else:
	print('none')

print('\n')
#CITY OF YANKTON
yanktonBaseUrl = 'https://www.cityofyankton.org/'

#import Bid Page
yanktonUrl = 'http://www.cityofyankton.org/how-do-i/bid-rfp-posts-list/-selsta-4'
yanktonPage = requests.get(yanktonUrl)

#beautifulSoup
yanktonSoup = BeautifulSoup(yanktonPage.content, 'html5lib')

yanktonActive = yanktonSoup.select('a[href*="Components/RFP"]')

print("Yankton Open Projects:")
if len(yanktonActive) != 0:
	for element in yanktonActive:
		print(element.text + ", " + (yanktonBaseUrl + element.get('href')))
else:
	print('none')

print('\n')
#CITY OF SPEARFISH
spearfishBaseUrl = 'https://www.cityofspearfish.com/'

#import Bid Page
spearfishUrl = 'https://www.cityofspearfish.com/Bids.aspx'
spearfishPage = requests.get(spearfishUrl)

#beautifulSoup
spearfishSoup = BeautifulSoup(spearfishPage.content, 'html5lib')

spearfishActive = spearfishSoup.select('a[href*="bids.aspx"]')

print("Spearfish Open Projects:")
spearfishList = []
if len(spearfishActive) != 0:
	for element in spearfishActive:
		spearfishList.append(element.text + ", " + (spearfishBaseUrl + element.get('href')))
	
		unwanted = [i for i, s in enumerate(spearfishActive) if 'Read\xa0on' in s]
	for ele in sorted(unwanted, reverse = True):
		del spearfishList[ele]
	print(*spearfishList, sep = "\n")
else:
	print('none')

print('\n')
#CITY OF VERMILLION
vermillionBaseUrl = 'https://www.vermillion.us/'

#import Bid Page
vermillionUrl = 'https://www.vermillion.us/Bids.aspx'
vermillionPage = requests.get(vermillionUrl)

#beautifulSoup
vermillionSoup = BeautifulSoup(vermillionPage.content, 'html5lib')

vermillionActive = vermillionSoup.select('a[href*="bids.aspx"]')

print("Vermillion Open Projects:")
vermillionList = []
if len(vermillionActive) != 0:
	for element in vermillionActive:
		vermillionList.append(element.text + ", " + (vermillionBaseUrl + element.get('href')))
	
		unwanted = [i for i, s in enumerate(vermillionActive) if 'Read\xa0on' in s]
	for ele in sorted(unwanted, reverse = True):
		del vermillionList[ele]
	print(*vermillionList, sep = "\n")
else:
	print('none')

print('\n')
#CITY OF MADISON
madisonBaseUrl = 'https://www.cityofmadisonsd.com/'

#import Bid Page
madisonUrl = 'https://cityofmadisonsd.com/resources/bids'
madisonPage = requests.get(madisonUrl)

#beautifulSoup
madisonSoup = BeautifulSoup(madisonPage.content, 'html5lib')
madisonActive = madisonSoup.table.findAll("a")

print("Madison Open Projects:")
if len(madisonActive) != 0:
	for element in madisonActive:
		print(element.text + ", " + (madisonBaseUrl + element.get('href')))
else:
	print('none')

print('\n')
#South Dakota Game Fish & Parks
sdgfpBaseUrl = 'https://gfp.sd.gov/'

#import Bid Page
sdgfpUrl = 'https://gfp.sd.gov/bids-contracts/'
sdgfpPage = requests.get(sdgfpUrl)

#beautifulSoup
sdgfpSoup = BeautifulSoup(sdgfpPage.content, 'html5lib')
sdgfpActive = sdgfpSoup.table.findAll("a")

print("South Dakota Game Fish & Parks Open Projects:")
sdgfpList = []
if len(sdgfpActive) != 0:
	for element in sdgfpActive:
		sdgfpList.append(element.text + ", " + (sdgfpBaseUrl + element.get('href')))
	
		unwanted = [i for i, s in enumerate(sdgfpActive) if 'Yes' in s]
	for ele in sorted(unwanted, reverse = True):
		del sdgfpList[ele]
	print(*sdgfpList, sep = "\n")
else:
	print('none')

#window stays open
input()

