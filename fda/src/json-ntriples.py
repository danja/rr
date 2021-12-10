import json

f = open('big-data/drug-drugsfda-0001-of-0001.json')

data = json.load(f)

results = data['results']

top_terms = []
submissions_terms = []
product_terms = []
openfda_terms = []

for result in results:
    for top_term in result:
        if top_term not in top_terms:
            top_terms.append(top_term)

    if 'submissions' in result:
        submissions = result['submissions']
        for sub in submissions:
            for s_term in sub:
                if s_term not in submissions_terms:
                    submissions_terms.append(s_term)

    if 'products' in result:
        products = result['products']
        for prod in products:
            for p_term in prod:
                if p_term not in product_terms:
                    product_terms.append(p_term)

    if 'openfda' in result:
        openfda = result['openfda'].items()
        for f_term, value in openfda:
            if f_term not in openfda_terms:
                openfda_terms.append(f_term)
        # for fda in openfda:

           # for f_term in fda:
            #    if f_term not in openfda_terms:
             #       openfda_terms.append(f_term)

print('\nTop terms')
print(top_terms)
print('\nSubmissions terms')
print(submissions_terms)
print('\nProducts terms ')
print(product_terms)
print('\nopenfda terms')
print(openfda_terms)


f.close()
