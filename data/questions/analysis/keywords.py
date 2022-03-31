# https://pypi.org/project/rake-nltk/
from rake_nltk import Rake
# get all text
with open('data.txt', encoding='utf-8') as f:
    q_and_a = f.read()

# Uses stopwords for english from NLTK, and all punctuation characters by
# default

# r = Rake()
# może 2 do kolokacji
r = Rake(min_length=2, max_length=3, include_repeated_phrases=False)

# Extraction given the text.
r.extract_keywords_from_text(q_and_a)
ranked = r.get_ranked_phrases()
print(len(ranked))
print(ranked[:100])
by_dict = list(dict.fromkeys(ranked))


# add human-generated keywords

# use keywords to filter/search questions
