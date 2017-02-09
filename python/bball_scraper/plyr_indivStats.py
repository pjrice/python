#scrape basketball-reference.com player stats from individual games

import os
import csv
import urllib.request
from bs4 import BeautifulSoup

data = urllib.request.urlopen(url).read()
soup = BeautifulSoup(data, "lxml")

linuxPath = '/media/storage/'
winPath = 'C:/Users/ausma_000/Documents/'

#a list of the stats we're grabbing - these are the data-stat attribute labels
#in the html

statList = ['ranker','game_season','age','team_id','game_location',
            'opp_id','game_result','gs','mp','fg','fga','fg_pct','fg3','fg3a',
            'fg3_pct','ft','fta','ft_pct','orb','drb','trb','ast','stl','blk',
            'tov','pf','pts','game_score','plus_minus']

#statList = ['age','team_id']

#check the raw html for data-stat attrs with our stat names
statsHTML = [soup.find_all(attrs={"data-stat": statList[s]}) for s in range(statList.__len__())]

#try to have stats returned as a nested list - a list for each stat.
stats = list()
for s in range(statsHTML.__len__()):
    
    stats.append([ss.getText().strip() for ss in statsHTML[s]])
    
#got eem

#print stats to csv
zipStats = zip(*stats)

if os.path.isdir(linuxPath):
    fname = linuxPath+'python/python/bball_scraper/plyr_indivStats.csv'
else:
    fname = winPath+'python/python/bball_scraper/plyr_indivStats.csv'
                          
with open(fname,'w') as statsFile:
    wr = csv.writer(statsFile)
    for row in zipStats:
        wr.writerow(row)


#todo:
    
    #currently returns a pretty good dataset, but with a couple of "repeated 
    #header" rows - find and remove those before saving to csv