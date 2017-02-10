
#autogenerate links for bball-reference data

#http://www.foxsports.com/nba/players
#seems like a good link to grab names from

import os
import csv
import urllib.request
from bs4 import BeautifulSoup

plyrNames = list()
plyrData = True
count = 1
while plyrData:
    url = ('http://www.foxsports.com/nba/players?teamId=0&season=2016&position=0&page='
           +str(count)
           +'&country=0&grouping=0&weightclass=0')
    
    data = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(data, "lxml")
    
    if len(soup.find_all('p', {'class': 'wisbb_noItems'}))>0:
        plyrData = False
    else:
        filteredHTML = soup.find_all('a', {'class': 'wisbb_fullPlayer'})
        pNames = [s.getText().strip() for s in filteredHTML]
        pNames = [s.split('\n')[0] for s in pNames]
        pNames = [s.split(', ') for s in pNames]
        plyrNames.append(pNames)
        print(count)
        count += 1
        
#fuuck 

#to save the names 
#linuxPath = '/media/storage/'
#winPath = 'C:/Users/ausma_000/Documents/'
#
#if os.path.isdir(linuxPath):
#    fname = linuxPath+'python/python/bball_scraper/plyrNames.csv'
#else:
#    fname = winPath+'python/python/bball_scraper/plyrNames.csv'
#    
#with open(fname,'w') as nameFile:
#    wr = csv.writer(nameFile)
#    for row in zipNames:
#        wr.writerow(row)

#generate name code and paste between these, then add year at end
#example:
#http://www.basketball-reference.com/players/w/westbru01/gamelog/2009
#need to make: 'w/westbru01'
#urls are case-insensitive so don't worry about that, just grab the letters
#and paste them together
linkPre = 'http://www.basketball-reference.com/players/'
linkPost = '/gamelog/'

chunk = plyrNames[0][0][0][0]+'/'+plyrNames[0][0][0][0:5]+plyrNames[0][0][1][0:2]+'01'

#fucking alex abrines has unicode in his name, fucks the link, check for unicode
#characters and replace with ascii



#todo:
    #cycle through pages
    #use http://www.foxsports.com/nba/players first
    #use http://www.foxsports.com/nba/players?teamId=0&season=2016&position=0&page=2&country=0&grouping=0&weightclass=0 
    #and change page numbers after
    #okay, so foxsports doesn't return a 404 for page numbers exceeding 26
    #(the last page with players), just the page with "no data available" in
    #the table field
    
    #so:
        #check that the "
    
    #cat all the names together
    
    #generate the links from the names
#    



        


        
                                                                                            
                                                                                              
                                                                        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
    
