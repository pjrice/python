#find print url on recipe page and open it

import urllib
import re
from bs4 import BeautifulSoup

url = "http://allrecipes.com/recipe/87805/slow-cooker-pork-chops-ii/"
data = urllib.request.urlopen(url).read()
soup = BeautifulSoup(data, "lxml")



printurl = soup.findAll(id=re.compile("para$"))



printurl = soup.findAll(attrs={'href': re.compile("^http://")})




