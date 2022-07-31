# prepare with :
#              python3 -m spacy download en_core_web_trf

import spacy
from spacy import displacy


filename = 'data/nike.txt'

with open(filename) as f:
    lines = f.readlines()

text = ''.join(lines)
# print(text)

nlp = spacy.load("en_core_web_trf")
doc = nlp(text)

# quick skim of the tokens
for token in doc:
    if token.like_num:  # there are a few other markers like this
        print('vvvvvvvvvvvvvvvvvvvvvvvvvvvv')
    print(token.text)

displacy.serve(doc, style="ent")
