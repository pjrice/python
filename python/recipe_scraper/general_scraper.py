#general script to scrape recipes

import urllib
import re
from bs4 import BeautifulSoup

#get the url, then get the html
url = input('Enter the recipe\'s url: ')
data = urllib.request.urlopen(url).read()
soup = BeautifulSoup(data, "lxml")

#look for ingredients

#look for li items that are ingredients - works for foodnetwork
rawtext = soup.find_all('li', {'itemprop': 'ingredients'})
rawtext = [s.getText().strip() for s in rawtext]


#look for span items that are ingredients - works for allrecipes
rawtext1 = soup.find_all('span', {'itemprop': 'ingredients'})
rawtext1 = [s.getText().strip() for s in rawtext1]

            
#look for directions - works for foodnetwork
rawtext2 = soup.find_all('ul', {'class': re.compile("recipe")})
rawtext2 = [s.getText().strip() for s in rawtext2]
            
#look for directions - kinda works for allrecipes
rawtext3 = soup.find_all('span', {'class': re.compile("recipe-directions")})
rawtext3 = [s.getText().strip() for s in rawtext3]

