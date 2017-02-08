#scrape basketball-reference.com player "per game" stats

import urllib.request
from bs4 import BeautifulSoup

data = urllib.request.urlopen(url).read()
soup = BeautifulSoup(data, "lxml")


#a list of the stats we're grabbing
statlist = ['season','age','team_id','lg_id','pos','g','gs','mp_per_g',
            'fg_per_g','fga_per_g','fg_pct','fg3_per_g','fg3a_per_g','fg3_pct',
            'fg2_per_g','fg2a_per_g','fg2_pct','efg_pct','ft_per_g',
            'fta_per_g','ft_pct','orb_per_g','drb_per_g','trb_per_g',
            'ast_per_g','stl_per_g','blk_per_g','tov_per_g','pf_per_g',
            'pts_per_g']

#check the raw html for data-stat attrs with our stat names
stats_html = [soup.find_all(attrs={"data-stat": statlist[s]}) for s in range(statlist.__len__())]

#try to have stats returned as a nested list - a list for each stat.
stats = list()
for s in range(stats_html.__len__()):
    
    stats.append([ss.getText().strip() for ss in stats_html[s]])
    
#got eem
    
    
#todo:
    #get player name!
    #format stats to be exported to csv
    #do the same for the per-game logs! example: http://www.basketball-reference.com/players/w/westbru01/gamelog/2009