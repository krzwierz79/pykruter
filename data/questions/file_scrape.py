import requests
from bs4 import BeautifulSoup

# coś tu jest nie tak z kodowaniem
with open('DataFlair.html', 'r') as f:
    soup = BeautifulSoup(f.read().decode('utf-8', 'ignore'), 'html.parser')

p_tags = soup.find_all("p")

for tag in p_tags:
    tag_c = tag.get_text()
    print(tag_c)

# scrape.py >> plik.txt
