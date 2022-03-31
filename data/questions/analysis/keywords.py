# https://pypi.org/project/rake-nltk/
from rake_nltk import Rake
# get all text

# Uses stopwords for english from NLTK, and all punctuation characters by
# default
# r = Rake()
r = Rake(max_length=1)  # może 2 do kolokacji

# Extraction given the text.
r.extract_keywords_from_text(q_and_a)

# add human-generated keywords

# use keywords to filter/search questions
