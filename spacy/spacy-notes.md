**remember to use python3**

_2022-07-31_

After looking at a few of the legal docs from https://github.com/applicaai/kleister-nda/ and playing with spacy a bit, my initial feeling is -

- a purely rule-based approach is likely to hit a fairly low ceiling on accuracy, there is a lot of variation in how the docs are organised
- a purely neural network-based approach could potentially do a lot better, **but**, on it's own would almost certainly need a big training set of manually annotated docs and probably a lot of processing power/time (I could only see 254 docs in kleister-nda with target extracted data)

(I'll say 'neural network' with handwaving, might end up being some other machine learningy bits)

So maybe try a combination.

First put together a rules pipeline that at least highlights the features of interest in each documents, ideally with candidate values, to give the neural net side a head start.
See if there's a neural net architecture that's known to work well with this kind of the task. (As ever, anything available off-the-shelf will be a timesaver).
Glue everything together.

There does seem to be a fair bit of existing material to skim through, check this abstract : https://arxiv.org/abs/2105.05796

### Rules

For example : naive approach, when just getting the signature date, grab the final 500? tokens, find any date in that.

Drawbacks :

- the first test document would work with this, but the 2nd document has the signature date in the first paragraph!
- the 3rd doc has 2 signing dates near the end (for "ANN TAYLOR" and "ASSOCIATE")

But rules can definitely be used to identify any dates, along with any other keywords that might provide a context through proximity ('PARTIES', 'EMPLOYEE'...).

Out of the box spacy has models that can do quite a bit of work, categorizing tokens as numbers, parts of speech (noun, verb...) etc. It should be straightforward to tweak/augment this with a bit of manual labeling. I don't know yet what is doable without excessive effort.

### Neural Network(s)

Target outputs are things like effective_date=2001-04-18 for each doc.

#### Inputs

From what I can gather it should be straightforward to pipeline this after any rules processing. Which suggests 3 inputs for training the nets :

1. the raw-ish (tokenized+) content of the original documents
2. the (suitably digested) target extracted data, ie. labels/annotation
3. a set of rule-derived 'hints' about the content (whatever form they might take)

For 1. I reckon just use a minimum of spacy built-ins, keep it simple.

For 2. the kleister-nda data (in /train) has 254 lines of target info, of the form :

effective_date=2001-04-18 jurisdiction=Oregon party=Eric_Dean_Sprunk party=NIKE_Inc.

I don't know yet how spacy likes to consume things like this, but it's bound to have something available to accept stuff of that general shape.

For 3. reading & experimenting needed.

#### Model

What shape any neural nets should take is an open question...bit of research & lots of experimentation needed.

But I reckon something that includes some kind of clustering would probably be useful, there's bound to be some association between particular sets of keywords and the material around them (eg. signature block).

### Playing with spacy tokenizer/entity recognizer

code currently in https://github.com/danja/rr/tree/main/spacy running from console(/VSCode), using spacy's displacy.serve to launch browser view of visualization

- try play.py

trying https://spacy.io/usage/models

the 'efficiency' model, '"en_core_web_sm" doesn't recognise 04/18/01 as a date

![oops](https://github.com/danja/rr/blob/main/spacy/images/nike-error.png)

trying 'accuracy', "en_core_web_trf"

Yay! that does recognise 04/18/01 as a date

![better](https://github.com/danja/rr/blob/main/spacy/images/nike-accuracy.png)

### Targets

- Contract Effective Date
  (is a Definition and as such can be referenced throughout the document)
- Contract End Date
  (if it exists)
- Contract Signature Date
  (usually part of the signature block near the end)
- Contract Name
  (is a Definition)
- Contract Party location
  (Contract Parties are uniquely identified organizations (LLCs or corporations) or named individuals with incorporation or address)

_2022-07-29_

### spaCy Setup

pip3 install -U pip setuptools wheel
pip3 install -U 'spacy[transformers,lookups]'
python3 -m spacy download en_core_web_sm

pip3 install jupyterlab
jupyter-lab

for now I think I'll code in VSCode, run in terminal - bit more obvious what's going on than in jupyter
