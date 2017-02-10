
#autogenerate links for bball-reference data

#http://www.foxsports.com/nba/players
#seems like a good link to grab names from

import os
import csv
import urllib.request
from bs4 import BeautifulSoup

#generate name code and paste between these, then add year at end
#example:
#http://www.basketball-reference.com/players/w/westbru01/gamelog/2009
linkPre = 'http://www.basketball-reference.com/players/'
linkPost = '/gamelog/'

data = urllib.request.urlopen(url).read()
soup = BeautifulSoup(data, "lxml")

test = soup.find_all('a', {'class': 'wisbb_fullPlayer'})

test1 = [s.getText().strip() for s in test]

#removes the double name
test2 = [s.split('\n')[0] for s in test1]

#splits into first and last name
test3 = [s.split(', ') for s in test2]


#todo:
    #cycle through pages
    #use http://www.foxsports.com/nba/players first
    #use http://www.foxsports.com/nba/players?teamId=0&season=2016&position=0&page=2&country=0&grouping=0&weightclass=0 
    #and change page numbers after
    
    #cat all the names together
    
    #generate the links from the names