import requests
from bs4 import BeautifulSoup


URL = "https://data-flair.training/blogs/top-python-interview-questions-answer/"
# URL = "https://www.projectpro.io/article/100-data-science-in-python-interview-questions-and-answers-for-2021/188"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

p_tags = soup.find_all("p")
# p_tags = soup.find_all("p", {"style": "text-align: left;"})
for tag in p_tags:
    tag_c = tag.get_text()
    print(tag_c)

# scrape.py >> plik.txt
