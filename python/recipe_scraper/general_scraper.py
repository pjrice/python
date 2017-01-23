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

#split these up into html "object" groups (span, div, li, ul, etc),
#each group searching for some common itemprop/class labels
#try the re.compile stuff as well
#have groups of commands for what we know "works" for common websites,
#then have array  of queries for other sites as outlined above

#this works for myrecipes.com
#get recipe ingredients
rawtext4 = soup.find_all('div', {'itemprop': 'recipeIngredient'})
rawtext4 = [s.getText().strip() for s in rawtext4]
#get directions
rt5 = soup.find_all('div', {'itemprop': 'recipeInstructions'})
rt5 = [s.getText().strip() for s in rt5]
