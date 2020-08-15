# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 09:26:19 2020

@author: Unknown
"""

from multiprocessing import Pool

import bs4
from bs4 import BeautifulSoup
import re
import requests
import webbrowser


class WebScraper:
    def __init__(self):
        pass

    def scrape(self):
        pass

    def getURLs(self):
        pass


def _singleScraper(url, query):
    try:
        page = requests.get(url + query)
    except ConnectionError:
        pass

    soup = BeautifulSoup(page.content, 'html5lib')
    active = soup.select(r'a[href*="bids.aspx"]')

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

    return titles, sites


if __name__ == '__main__':
    brookingsURL = 'https://cityofbrookings.org/'
    brookingsQuery = 'Bids.aspx?CatID=All&txtSort=Category&showAllBids=&Status='

    siouxfallsURL = 'https://www.siouxfalls.org/business/ntb'
    siouxfallsQuery = ''

    aberdeenURL = 'https://aberdeen.sd.us/'
    aberdeenQuery = 'Bids.aspx'

    print('--- Brookings ---')
    t, s = _singleScraper(brookingsURL, brookingsQuery)
    print(t)
    print(s)
    print('--- Sioux Falls ---')
    t, s = _singleScraper(siouxfallsURL, siouxfallsQuery)
    print(t)
    print(s)
    print('--- Aberdeen ---')
    t, s = _singleScraper(aberdeenURL, aberdeenQuery)
    print(t)
    print(s)
