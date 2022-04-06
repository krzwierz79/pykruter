import pandas as pd
import glob
from openpyxl.workbook import Workbook


# df = pd.read_excel(r'dataflair.xls')
# print(len(df))


# path = r'..'  # use your path
all_files = glob.glob("*.xls")
print(len(all_files))

urls = [
    "https://data-flair.training/blogs/top-python-interview-questions-answer/",
    "https://docs.google.com/document/d/1SoGPPtYkiXC5AEnsNvqB41S72NjnUgk_4nPnqNQkRwY/edit?usp=sharing",
    "https://www.guru99.com/python-interview-questions-answers.html",
    "https://hackr.io/blog/python-interview-questions",
    "https://www.projectpro.io/article/100-data-science-in-python-interview-questions-and-answers-for-2021/188"
]

file_url = {
    "dataflair.xls": "https://data-flair.training/blogs/top-python-interview-questions-answer/",
    "docs_google.xls": "https://docs.google.com/document/d/1SoGPPtYkiXC5AEnsNvqB41S72NjnUgk_4nPnqNQkRwY/edit?usp=sharing",
    "guru99.xls": "https://www.guru99.com/python-interview-questions-answers.html",
    "hackr_io.xls": "https://hackr.io/blog/python-interview-questions",
    "projectpro.xls": "https://www.projectpro.io/article/100-data-science-in-python-interview-questions-and-answers-for-2021/188"
}

li = []

for filename in all_files:
    df = pd.read_excel(filename, index_col=None, header=0)
    url = file_url.get(filename)
    df.insert(loc=0,
              column='url',
              value=url)
    li.append(df)


# for count, filename in enumerate(all_files):
#     # df['url'] = filename
#     df = pd.read_excel(filename, index_col=None, header=0)
#     df.insert(loc=0,
#               column='url',
#               value=urls[count])
#     li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)
print(len(frame))

with pd.ExcelWriter("collected.xlsx") as writer:
    frame.to_excel(writer)
