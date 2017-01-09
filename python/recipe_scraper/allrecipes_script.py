#small script to scrape allrecipes page

import urllib
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


#from url determine if it's one of the big websites (maybe)

#use "section" to filter (both allrecipes and foodnetwork have "section" tags
#with classes that indicate that the recipe is there)

#get recipe from filtered text
