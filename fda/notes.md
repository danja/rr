Ronald, 2021-12-04

can you program something that parses JSON and makes it into RDF SKOS?

https://open.fda.gov/apis/drug/drugsfda/download/

https://www.fda.gov/media/81904/download

i wish i knew the exact elements (i think there are 30) that deal with MEDRA

basically i need a list of ones I will replace with a MedDra IRI

...

if so when do you think you might have something to show, i am interested in the model and of course the data

---

- First thoughts :

A totally custom JSON -> SKOS is one approach, some kind of mapping/templating. But it might be easier (and no less flexible) to use JSON-LD as an intermediate step, specifying mappings via JSN-LD context stuff, then parsing as JSON-LD, spit out Turtle or whatever if necessary for use elsewhere.

https://www.w3.org/TR/json-ld/#the-context

Once in Turtle, more fine-grained mappings could be done by putting the stuff on a SPARQL server and using CONSTRUCT queries.

I'm not really sure what JSON-LD tools are available, but I would expect this to be doable.

(I am very rusty on JSON-LD)

- check existing work openfda -> RDF

found some discussion (and even some rough bits of code) but this appears to have stalled around 2015. There is this :

https://github.com/westurner/openfda-jsonld-testing

https://github.com/westurner/openfda-jsonld-testing/tree/gh-pages/schemas

includes faers_mapping.json

---

https://open.fda.gov/apis/drug/drugsfda/download/

There are 1 files, last updated on 2021-12-07.

/drug/drugsfda data7.66 mb

there are other datasets - in scope?

Drug Adverse Events [/drug/event]

https://open.fda.gov/apis/drug/event/download/

There are 1211 files, last updated on 2021-12-07.
(zipped)

openfda JSON schemas are at : https://github.com/FDA/openfda/tree/master/schemas

https://github.com/FDA/openfda/blob/master/schemas/drugsfda_schema.json

for quick visualization I used : https://dadroit.com/

the data is pretty straightforward, for JSON-LD

https://w3c.github.io/json-ld-syntax/#nested-properties

I believe will be needed.

application_number

Ok, CODE TIME

\$ python --version
Python 3.8.5

// \$ pip install rdflib

in vscode had to do :

python3 -m venv .venv
source .venv/bin/activate

Select your new environment by using the Python: Select Interpreter command from the Command Palette.

python3 -m pip install --upgrade pip

(had to fiddle a bit - had forgotten I had Anaconda installed)

python3 -m pip install rdflib-jsonld

// note to self - use the items() method to iterate over a dictionary
