#Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this website:
#http://www.washingtonpost.com/wp-dyn/content/article/2010/08/29/AR2010082902749.html?noredirect=on
#The article is long, so it is split up between 4 pages.
#Your task is to print out the text to the screen so that you can read the full article without having to click any buttons.

import requests

from bs4 import BeautifulSoup



url = 'http://www.washingtonpost.com/wp-dyn/content/article/2010/08/29/AR2010082902749.html?noredirect=on'
flag = True

while flag:
    
    r = requests.get(url)
    r_html = r.text

    soup = BeautifulSoup(r_html, "lxml")

    n = 0
    for tag in soup.find_all("a"):
        if tag.string == 'Next':
            url = tag.get('href')
            n = 1

    for tag in soup.find_all("p"):
        if tag.string != None:
            print(tag.string)
        
    if n == 0:
        flag = False
