#scrape basketball-reference.com player "per game" stats

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
#statList = ['season','age','team_id','lg_id','pos','g','gs','mp_per_g',
#            'fg_per_g','fga_per_g','fg_pct','fg3_per_g','fg3a_per_g','fg3_pct',
#            'fg2_per_g','fg2a_per_g','fg2_pct','efg_pct','ft_per_g',
#            'fta_per_g','ft_pct','orb_per_g','drb_per_g','trb_per_g',
#            'ast_per_g','stl_per_g','blk_per_g','tov_per_g','pf_per_g',
#            'pts_per_g']

statList = ['age','team_id']

#check the raw html for data-stat attrs with our stat names
statsHTML = [soup.find_all(attrs={"data-stat": statList[s]}) for s in range(statList.__len__())]

#try to have stats returned as a nested list - a list for each stat.
stats = list()
for s in range(statsHTML.__len__()):
    
    stats.append([ss.getText().strip() for ss in statsHTML[s]])
    
#got eem

#get player name and add a new column
playerHTML = soup.find_all('h1',{'itemprop': 'name'})
#replicates by number of rows
playerName = [playerHTML[0].getText().strip()]*stats[0].__len__()
playerName[0] = 'Player Name'
#adds to first position in stats list
stats.insert(0,playerName)
    
#print stats to csv
zipStats = zip(*stats) #needs the * to work properly

if os.path.isdir(linuxPath):
    fname = linuxPath+'python/python/bball_scraper/stats.csv'
else:
    fname = winPath+'python/python/bball_scraper/stats.csv'
                          
with open(fname,'w') as statsFile:
    wr = csv.writer(statsFile)
    for row in zipStats:
        wr.writerow(row)


#todo:
    #do the same for the per-game logs! example: http://www.basketball-reference.com/players/w/westbru01/gamelog/2009
    
    