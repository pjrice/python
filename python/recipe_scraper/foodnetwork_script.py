#small script to scrape foodnetwork page

import urllib
import re
from bs4 import BeautifulSoup

url = "http://www.foodnetwork.com/recipes/food-network-kitchens/cajun-shrimp-and-rice-recipe.html"
data = urllib.request.urlopen(url).read()
soup = BeautifulSoup(data, "lxml")

rawtext = soup.find('section', {'class': re.compile("ingredient")})



rawtext = [s.getText().strip() for s in rawtext.findAll('li')]

           
           
