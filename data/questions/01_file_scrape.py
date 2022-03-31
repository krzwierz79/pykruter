from bs4 import BeautifulSoup

# coś tu jest nie tak z kodowaniem
with open('dataflair2.html', 'r') as f:
    # for count, line in enumerate(f):
    #     try:
    #         soup = []
    #         soup = BeautifulSoup(f.readline(), 'html.parser')
    #         print(soup)
    #     except:
    #         print(count)
    soup = BeautifulSoup(f.read(), 'html.parser')


# # get all <p>
# p_tags = soup.find_all("p")
# for tag in p_tags:
#     tag_c = tag.get_text()
#     print(tag_c)

# get all text
text = soup.get_text()
print(text)


# scrape.py >> plik.txt
