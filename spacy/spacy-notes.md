**remember to use python3**

_2022-07-31_

When just getting the signature date, make a Span of the final 100? Tokens, find any date in that.

Drawbacks :

- the first test document would work with this, but the 2nd has the Agreement/signature date in the first paragraph!
- the 3rd doc has 2 dates near the end ("ANN TAYLOR" and "ASSOCIATE")

https://spacy.io/usage/models

the 'efficiency' model, '"en_core_web_sm" doesn't recognise 04/18/01 as a date

trying 'accuracy', "en_core_web_trf"

Yay! that does recognise 04/18/01 as a date

---

_2022-07-29_

pip3 install -U pip setuptools wheel
pip3 install -U 'spacy[transformers,lookups]'
python3 -m spacy download en_core_web_sm

pip3 install jupyterlab
jupyter-lab
