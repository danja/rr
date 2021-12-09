drug-drugsfda-0001-of-0001.json

a list, "results"

each of which may contain dictionaries

submissions
application_number
sponsor_name
openfda
products

application_number appears to be a unique ID, eg. ANDA076008
sponsor_name, eg. HERITAGE PHARMA

openfda contains a dictionary of shortish refs/IDs, the values of which are lists, eg.

"product_ndc": [
"51672-4085",
"51672-4086",
"51672-4087"
],

submissions contains a dictionary which _may_ contain :

['submission_type', 'submission_number', 'submission_status', 'submission_status_date', 'submission_class_code', 'submission_class_code_description', 'application_docs', 'review_priority', 'submission_public_notes', 'submission_property_type']

products contains a dictionary which _may_ contain :

['product_number', 'reference_drug', 'brand_name', 'active_ingredients', 'reference_standard', 'dosage_form', 'route', 'marketing_status', 'te_code']
