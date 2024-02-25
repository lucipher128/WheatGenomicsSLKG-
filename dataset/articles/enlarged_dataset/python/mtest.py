import json

def gen_authors_ttl(): 
    file = open('../json/authors_correction_lki.json')
    test_output = open('../output/authors/out.ttl','w')
    namespaces = ['''
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd:     <http://www.w3.org/2001/XMLSchema#> .
@prefix bibo:   <http://purl.org/ontology/bibo/> .
@prefix fabio: <http://purl.org/spar/fabio/> .
@prefix dc: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix schema: <http://schema.org/> .\n\n
''']

    test_output.writelines(namespaces)

    buffer = [""]
    archi = [""]
    for line in file:
        x = json.loads(line)

        idt = ""
        orcid = ""

        if x['last_known_institution'] is not None:

            if  x['last_known_institution']['id'] is not  None :
                idt = x['last_known_institution']['id']

            archi = ["<" + x['ids']['openalex'] + ">" + " a schema:Person ;\n foaf:name \"" + x['display_name'] + "\"" + 
                     ";\n d2kab:lastKnownAffiliation  <" + idt + ">;\n"]
            try :
                orcid =  x['ids']['orcid']
                archi = archi + [" schema:identifier <" + orcid + "> .\n\n"]
            except:
                archi = archi + ["\n"]



        buffer = buffer + archi

    test_output.writelines(buffer);
    test_output.close()

def gen_institutions_ttl():
    file = open('../json/institutions.json')
    test_output = open('../output/organizations/out.ttl','w')
    namespaces = ['''
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd:     <http://www.w3.org/2001/XMLSchema#> .
@prefix bibo:   <http://purl.org/ontology/bibo/> .
@prefix fabio: <http://purl.org/spar/fabio/> .
@prefix dc: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix schema: <http://schema.org/> .\n\n
''']
    test_output.writelines(namespaces)
    buffer = [""]
    archi = [""]

    idi = ""
    ror = ""
    for line in file:
        x = json.loads(line)
        try:
            idt = x['id']
            archi = ["<" + idt + ">" + " a schema:Organization ;\n"]
            buffer = buffer + archi
            try:
                ror = x['ror']
                archi = ["schema:identifier <" + ror + "> ;\n"]
                buffer = buffer + archi
            except NoneType:
                print("found no  ror for institution ",x['id'])
                print(x['id'])
            else:
                archi = ["foaf:name \"" + x['display_name'] + "\" ;\n" + 
                          "schema:addressCountry \"" + x['country_code'] + "\" ;\n" +
                          "schema:category \"" + x['type'] +"\" .\n\n"]
                buffer = buffer + archi
            
        except:
            print(":")
            continue

    test_output.writelines(buffer);
    test_output.close()

#gen_institutions_ttl()
gen_authors_ttl()
