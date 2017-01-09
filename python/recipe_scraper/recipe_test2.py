#try to make a recipe scraper

import urllib
import re
from bs4 import BeautifulSoup

#using print url because the page is cleaner
#find way to navigate to print url from main recipe page? - fucking annoying,
#at least on allrecipes.com
url = "http://allrecipes.com/recipe/87805/slow-cooker-pork-chops-ii/"
url = url + 'print/'
data = urllib.request.urlopen(url).read()
soup = BeautifulSoup(data, "lxml")

#get ingredients and directions
rawtext = soup.find('div', {'class': 'recipe-print__container2'})
rawtext = [s.getText().strip() for s in rawtext.findAll('li')]