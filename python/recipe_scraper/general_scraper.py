#general script to scrape recipes

import urllib
import re
from bs4 import BeautifulSoup

#easily traverses nested lists
#thanks to Jeremy Banks @ http://stackoverflow.com/questions/6340351/python-iterating-through-list-of-list
def traverse(o, tree_types=(list, tuple)):
    if isinstance(o, tree_types):
        for value in o:
            for subvalue in traverse(value, tree_types):
                yield subvalue
    else:
        yield o

#get the url, then get the html
url = input('Enter the recipe\'s url: ')
data = urllib.request.urlopen(url).read()
soup = BeautifulSoup(data, "lxml")

#look for ingredients

ingreds = list()

#works for foodnetwork
ingreds.append(soup.find_all('li', {'itemprop': 'ingredients'}))

#works for allrecipes
ingreds.append(soup.find_all('span', {'itemprop': 'ingredients'}))

#works for myrecipes
ingreds.append(soup.find_all('div', {'itemprop': 'recipeIngredient'}))

#strip html out          
ingreds = [s.getText().strip() for s in traverse(ingreds)]

# look for directions

recipe = list()
  
#look for directions - works for foodnetwork
recipe.append(soup.find_all('ul', {'class': re.compile("recipe")}))
            
#look for directions - kinda works for allrecipes
recipe.append(soup.find_all('span', {'class': "recipe-directions__list--item"}))

#works for myrecipes
recipe.append(soup.find_all('div', {'itemprop': 'recipeInstructions'}))

#strip html out
recipe = [s.getText().strip() for s in traverse(recipe)]


#print lists and choose what to keep

for i in range(len(ingreds)):
    success = False
    print('\n')
    print(ingreds[i])
    print('\n')
    keep = input("Keep this item? [y/n]")
    while not success:
        if keep is 'y' or keep is 'Y':
            success = True
        elif keep is 'n' or keep is 'N':
            ingreds.remove(ingreds[i])
            success = True
        else:
            print("Cannot interpret answer, try again [y/n]")
            

for i in range(len(recipe)):
    success = False
    print('\n')
    print(recipe[i])
    print('\n')
    keep = input("Keep this item? [y/n]")
    while not success:
        if keep is'y' or keep is 'Y':
            success = True
        elif keep is 'n' or keep is 'N':
            recipe.remove(recipe[i])
            success = True
        else:
            print("Cannot interpret answer, try again [y/n]")
            
#remove any newline characters from resultant text
[s.replace('\n','') for s in ingreds]
[s.replace('\n','') for s in recipe]

    





#ToDos:
    
#remove newlines

#split these up into html "object" groups (span, div, li, ul, etc),
#each group searching for some common itemprop/class labels
#try the re.compile stuff as well
#have groups of commands for what we know "works" for common websites,
#then have array  of queries for other sites as outlined above

