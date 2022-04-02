import requests
from bs4 import BeautifulSoup

URL = "https://hackr.io/blog/python-interview-questions"
# URL = "https://www.projectpro.io/article/100-data-science-in-python-interview-questions-and-answers-for-2021/188"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# p_tags = soup.find_all("p")
# p_tags = soup.find_all("p", {"style": "text-align: left;"})
tags = soup.find_all(['h4', 'p'])  # wybiera tagi z html
for tag in tags:
    tag_t = tag.get_text()  # wyciąga sam tekst
    print(tag_t)

# uruchomiony z przekierowaniem 01_web_scrape.py > plik.txt zapisuje do pliku zamiast po prostu printować
