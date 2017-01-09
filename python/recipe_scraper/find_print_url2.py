from lxml import html
import requests

url = "http://allrecipes.com/recipe/87805/slow-cooker-pork-chops-ii/"
page = requests.get(url)
webpage = html.fromstring(page.content)

test = webpage.xpath('//*[@id="print-recipe"]')



#print-recipe