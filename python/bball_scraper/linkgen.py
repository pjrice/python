
#autogenerate links for bball-reference data

#http://www.foxsports.com/nba/players
#seems like a good link to grab names from

import os
import csv
import urllib.request
import itertools
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
        
plyrNames = list(itertools.chain.from_iterable(plyrNames))

for i in range(len(plyrNames)):
    for ii in range(len(plyrNames[i])):
        plyrNames[i][ii] = plyrNames[i][ii].encode('utf-8').strip()
    
###############################################################################
    
#save names
linuxPath = '/home/ausmanpa/Documents/gp/'
winPath = 'C:/Users/ausma_000/Documents/'


if os.path.isdir(linuxPath):
    fname = linuxPath+'python/python/bball_scraper/plyrNames.csv'
else:
    fname = winPath+'python/python/bball_scraper/plyrNames.csv'
    
with open(fname,'w') as nameFile:
    wr = csv.writer(nameFile)
    for row in plyrNames:
        wr.writerow(row)
        
###############################################################################

#read names file      
plyrNames = list()
with open('plyrNames.csv', 'r') as csvfile:
    plyrNamescsv = csv.reader(csvfile)
    for row in plyrNamescsv:
        plyrNames.append(row)


for i in range(len(plyrNames)):
    for ii in range(len(plyrNames[i])):
        plyrNames[i][ii] = plyrNames[i][ii][2:]
        plyrNames[i][ii] = plyrNames[i][ii][:-1]

###############################################################################

#make gamelog links    
linkPre = 'http://www.basketball-reference.com/players/'
linkPost = '/gamelog/2017'

plyrLink = list()
[plyrLink.append(plyrNames[i][0][0]+'/'+plyrNames[i][0][0:5]+plyrNames[i][1][0:2]+'01') for i in range(len(plyrNames))]    

for i in range(len(plyrLink)):
    plyrLink[i] = linkPre+plyrLink[i]+linkPost
    
#save links
linuxPath = '/home/ausmanpa/Documents/gp/'
winPath = 'C:/Users/ausma_000/Documents/'

if os.path.isdir(linuxPath):
    fname = linuxPath+'python/python/bball_scraper/plyrLink2017.csv'
else:
    fname = winPath+'python/python/bball_scraper/plyrLink2017.csv'
    
with open(fname,'w') as nameFile:
    wr = csv.writer(nameFile)
    for row in plyrLink:
        wr.writerow(row)
        
#read links file
ph = list()
with open('plyrLink2017.csv', 'r') as csvfile:
    plyrLinkcsv = csv.reader(csvfile)
    for row in plyrLinkcsv:
        ph.append(row)
        
plyrLink = list()
[plyrLink.append(''.join(ph[i])) for i in range(len(ph))]



#fucking alex abrines has unicode in his name, fucks the link, check for unicode
#characters and replace with ascii

#that doesn't work, will just check manually, hopefully won't be too many



        


        
                                                                                            
                                                                                              
                                                                        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
    
