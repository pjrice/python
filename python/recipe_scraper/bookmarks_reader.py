#read recipes bookmarks from html

import urllib
from bs4 import BeautifulSoup

url = "C:\\Users\\ausma_000\\Dropbox\\Documents\\recipe_scraper\\recipes\\bookmarks_1_8_17.html"
file = open(url,'r')