import json

import base64
import hashlib

from rdflib import Graph, Namespace, URIRef, Literal, BNode, RDF
from rdflib.namespace import DC, DCTERMS, DOAP, FOAF, SKOS, OWL, RDF, RDFS, VOID, XMLNS, XSD

# downloaded/unzipped https://open.fda.gov/apis/drug/drugsfda/download/
f = open('big-data/drug-drugsfda-0001-of-0001.json')

DRUGS = Namespace('https://open.fda.gov/drugs#')

INSTANCE_BASE = "https://open.fda.gov/drugs/instance#"

g = Graph()
g.bind("drugs", DRUGS)

# g.add((
#    URIRef("http://example.org/thing"),
#    DRUGS['test'],
#    Literal("Aspirin")
# ))


def add_literal(graph, subject_id, drugs_term, object_string):
    graph.add((
        URIRef(INSTANCE_BASE+subject_id),
        DRUGS[drugs_term],
        Literal(object_string)
    ))

# add_literal(g, "this", "test", "literal test")
# print(g.serialize(format="turtle"))
# exit()


def hash_string(content):
    hasher = hashlib.sha1(content.encode('utf-8'))
    bytes = base64.urlsafe_b64encode(hasher.digest())
    return bytes.hex()


def id_from_object(object):
    string = json.dumps(object)  # gives a string that is also valid JSON
    hashed = hash_string(string)
    return hashed  # [:8]  # truncate

# test = [{"one": "two", "three": "four"}]
# print(id_from_object(test))
# exit()


data = json.load(f)

results = data['results']

for result in results:

    if 'products' in result:
        products = result['products']  # list of objects
        for product in products:  # list of dictionaries
            product_id = "product_"+id_from_object(product)
            for name, value in product.items():
                if type(value) is str:  # some are lists
                    #print(name + " : "+value)
                    add_literal(g, product_id, name, value)

    if 'openfda' in result:
        openfdas = result['openfda']  # list of dictionaries
        for name, values in openfdas.items():
            openfda_id = "openfda_"+id_from_object(name)
            for value in values:
                add_literal(g, openfda_id, name, value)

print(g.serialize(format="ntriples"))

f.close()
