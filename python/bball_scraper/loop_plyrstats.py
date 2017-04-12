#file to loop through bballref links and get player stats

import csv
#import time
#import random
import urllib.request
from bs4 import BeautifulSoup



#read links file
ph = list()
with open('plyrLink2017.csv', 'r') as csvfile:
    plyrLinkcsv = csv.reader(csvfile)
    for row in plyrLinkcsv:
        ph.append(row)
        
plyrLink = list()
[plyrLink.append(''.join(ph[i])) for i in range(len(ph))]

#read player name file
plyrNames = list()
with open('plyrNames.csv', 'r') as csvfile:
    plyrNamescsv = csv.reader(csvfile)
    for row in plyrNamescsv:
        plyrNames.append(row)


#a list of the stats we're grabbing
statList = ['ranker','game_season','age','team_id','game_location',
        'opp_id','game_result','gs','mp','fg','fga','fg_pct','fg3','fg3a',
        'fg3_pct','ft','fta','ft_pct','orb','drb','trb','ast','stl','blk',
        'tov','pf','pts','game_score','plus_minus']

#loop through links
#check if link exists first
progress = 1
badlinks = list()
for link in range(len(plyrLink)):
    
    print(progress)
    progress += 1
    
    data = urllib.request.urlopen(plyrLink[link]).read()
    soup = BeautifulSoup(data, 'lxml')
    del(data)
    
    #check if the link has 404'd
    goodlink = soup.find_all(attrs={'data-stat': statList[0]})
    
    if not goodlink:
        badlinks.append(1)
        continue
    
    else:
        
        badlinks.append(0)
        #check the raw html for data-stat attrs with our stat names
        #statsHTML = [soup.find_all(attrs={'data-stat': statList[s]}) for s in range(statList.__len__())]
        statsHTML = [soup.findAll('tr')]
        
        #get the text from the HTML
        stats = list()
        try:
            for s in range(statsHTML[0].__len__()):
                stats.append([ss.getText().strip() for ss in statsHTML[0][s]])
        except:
            for q in range(len(statList)):
                stats3.append(soup.find_all(attrs={'data-stat': statList[q]}))
                #this results in a string
                
                
                
        
        
#        for s in range(len(statsHTML[0])):
#            for ss in statsHTML[0][s]:
#                stats.append(ss.getText().strip())
#            
#        test = list()
#        for zz in range(0,85):
#            test.append(statsHTML[0][zz].getText().strip())
#            
        #okay, so this works alright, but there are additional rows at the top
        #from another table, and the same repeated rows, but the data is 
        #organized a bit differently, so out previous solution won't work
        
        #we want to try:
            
        #'Rk' in stats[i]
        #will return true if it is there, false if not
        #want to store these and use as an index - slice list at the first
        #appearance of 'Rk' (because this is out table header row) and remove
        #all subsequent rows that contain 'Rk' (because these are our repeat
        #rows)
        
        #gets index of presence of 'Rk'
        rkIdx = list()
        for i in range(len(stats)):
            rkIdx.append('Rk' in stats[i])
         
        #slices stats list and rkIdx at first occurrence of 'Rk'
        stats = stats[rkIdx.index(True):]
        rkIdx = rkIdx[rkIdx.index(True):]
        
        #still need to remove remaining 'Rk'
        stats1 = list()
        count = 0
        for i in range(len(stats)):
            if (not rkIdx[i]) or count==0:
                stats1.append(stats[i])
                count += 1
            else:
                count += 1
    
###############################################################################        
#        #remove "repeated header" rows
#        #get index of rows to remove
#        idx = list()
#        count = 0
#        for x in stats:
#            if not(x.isnumeric()) and count!=0:
#                idx.append(count)
#                count += 1
#            else:
#                count +=1
#                
#        #"remove" the rows (dissatisfied)  
#        stats1 = list()
#        for x in stats:
#            stats1.append([i for j, i in enumerate(x) if j not in idx])
#        
###############################################################################        

        #save the stats somehow
        #pickled database?
        
        #still need name to save with data...
        #modify linkgen to save the player name alongside the links
        #then pull that in and add it to stats1
        
        nameList = [', '.join(plyrNames[link])]*(len(stats1)-1)
        nameList.insert(0,'Player')
        
        filenameName = ''.join(plyrNames[link])+'2017.csv'
        
        for i in range(len(stats1)):
            stats1[i].insert(0,nameList[i])
        
        #for testing:
        #print stats to csv
        #zipStats = zip(*stats1)
        fname = '/home/ausmanpa/Documents/gp/python/python/bball_scraper/plyrStats/'+filenameName
        with open(fname,'w') as statsFile:
            wr = csv.writer(statsFile)
            for row in stats3:
                wr.writerow(row)
                
        #tries to avoid problem where HTML doesn't import correctly, but doesn't work
        #time.sleep(random.uniform(5,15))

        






        
    