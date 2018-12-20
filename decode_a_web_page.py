#Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.

import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, "lxml")
title = soup.find_all("h2")

for tag in soup.find_all("h2"):
    print(tag.string)

#Writing to the file
#with open('nytimes_titles.txt', 'w') as open_file:
#    for tag in soup.find_all("h2"):
#        open_file.write("{}\n".format(tag.string))
