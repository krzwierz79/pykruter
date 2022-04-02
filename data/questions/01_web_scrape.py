import requests
from bs4 import BeautifulSoup

URL = "https://hackr.io/blog/python-interview-questions"
# URL = "https://www.projectpro.io/article/100-data-science-in-python-interview-questions-and-answers-for-2021/188"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# p_tags = soup.find_all("p")
# p_tags = soup.find_all("p", {"style": "text-align: left;"})
tags = soup.find_all(['h4', 'p'])  # list all needed tags
for tag in p_tags:
    tag_t = tag.get_text()
    print(tag_t)

# scrape.py >> plik.txt
