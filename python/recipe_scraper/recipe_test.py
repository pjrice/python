#try to make a recipe scraper

import urllib
import re
from bs4 import BeautifulSoup

#url = "http://allrecipes.com/Recipe/Slow-Cooker-Pork-Chops-II"
url = "http://allrecipes.com/recipe/87805/slow-cooker-pork-chops-ii/print/?recipeType=Recipe&servings=4"
data = urllib.request.urlopen(url).read()
soup = BeautifulSoup(data, "lxml")

#get recipe title


#get ingredients
#make this work for the multiple ingredient lists
#aka soup.find(... list-ingredients-2'}), etc
rawtext = soup.find('ul', {'class': 'checklist dropdownwrapper list-ingredients-1'})
rawtext = [s.getText().strip() for s in rawtext.findAll('li')]
rawtext = [re.split(r'[;,\n]\n*', rawtext[i]) for i in range(len(rawtext))]
           
ingreds = [rawtext[i][0] for i in range(len(rawtext))]
           
#get directions







#def main():
#    url = "http://allrecipes.com/Recipe/Slow-Cooker-Pork-Chops-II/Detail.aspx"
#    data = urllib.request.urlopen(url).read()
#    bs = BeautifulSoup(data, "lxml")
#    
#    ingreds = bs.find('div', {'class': 'ingredients'})
#    ingreds = [s.getText().strip() for s in ingreds.findAll('li')]
#    
#    return (bs)
               
