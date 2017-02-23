#file to loop through bballref links and get player stats

import csv
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

#a list of the stats we're grabbing
statList = ['ranker','game_season','age','team_id','game_location',
        'opp_id','game_result','gs','mp','fg','fga','fg_pct','fg3','fg3a',
        'fg3_pct','ft','fta','ft_pct','orb','drb','trb','ast','stl','blk',
        'tov','pf','pts','game_score','plus_minus']

#loop through links
#check if link exists first

import httplib2
c = httplib.HTTPConnection('www.example.com')
c.request("HEAD", '')
if c.getresponse().status == 200:
   print('web site exists')

for i in range(len(plyrLink)):
    
    data = urllib.request.urlopen(plyrLink[i]).read()
    soup = BeautifulSoup(data, 'lxml')
    
    #check to see if the link 404'd; if so, mark and skip
    badlink = soup.find_all(attrs={'role': 'main'})

    #check the raw html for data-stat attrs with our stat names
    statsHTML = [soup.find_all(attrs={'data-stat': statList[s]}) for s in range(statList.__len__())]

    #try to have stats returned as a nested list - a list for each stat.
    stats = list()
    for s in range(statsHTML.__len__()):
    
        stats.append([ss.getText().strip() for ss in statsHTML[s]])
    
    #got eem
    
    #remove "repeated header" rows
    #get index of rows to remove
    idx = list()
    count = 0
    for x in stats[0]:
        if not(x.isnumeric()) and count!=0:
            idx.append(count)
            count += 1
            else:
                count +=1
                
                #"remove" the rows (dissatisfied)  
                stats1 = list()
                for x in stats:
                    stats1.append([i for j, i in enumerate(x) if j not in idx])

