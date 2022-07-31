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

# for token in doc:
#    if token.like_num:
#        print('vvvvvvvvvvvvvvvvvvvvvvvvvvvv')
#    print(token.text)

displacy.serve(doc, style="ent")
