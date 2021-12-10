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
...

submissions contains a dictionary which _may_ contain :

['submission_type', 'submission_number', 'submission_status', 'submission_status_date', 'submission_class_code', 'submission_class_code_description', 'application_docs', 'review_priority', 'submission_public_notes', 'submission_property_type']

these are all name-value pairs, except 'application_docs' which is a list containing entries, eg :

"application_docs": [
{
"id": "31141",
"url": "http://www.accessdata.fda.gov/drugsatfda_docs/appletter/2004/76568,76569ltr.pdf",
"date": "20040730",
"type": "Letter"
},
...

products contains a dictionary which _may_ contain :

['product_number', 'reference_drug', 'brand_name', 'active_ingredients', 'reference_standard', 'dosage_form', 'route', 'marketing_status', 'te_code']

'active_ingredients' is a list, entries eg.

"brand_name": "ALENDRONATE SODIUM",
"active_ingredients": [
{
"name": "ALENDRONATE SODIUM",
"strength": "EQ 70MG BASE"
}

openfda contains a dictionary which _may_ contain :

['application_number', 'brand_name', 'generic_name', 'manufacturer_name', 'product_ndc', 'product_type', 'route', 'substance_name', 'rxcui', 'spl_id', 'spl_set_id', 'package_ndc', 'nui', 'pharm_class_pe', 'pharm_class_epc', 'pharm_class_cs', 'unii', 'pharm_class_moa']

these are all lists of strings, some with only one entry
