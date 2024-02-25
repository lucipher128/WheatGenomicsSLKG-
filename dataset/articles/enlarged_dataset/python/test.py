from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, XSD

# Créer un graph RDF
g = Graph()

# Définir les préfixes
ex = Namespace("http://example.org/authors/")
schema = Namespace("http://schema.org/")
dct = Namespace("http://purl.org/dc/terms/")
bibo = Namespace("http://purl.org/ontology/bibo/")
ror = Namespace("https://ror.org/")

# Données JSON
data = {
  "id": "https://openalex.org/A5000007038",
  "orcid": None,
  "display_name": "L Marosi",
  "display_name_alternatives": ["Leo Marosi", "L. Marosi"],
  "works_count": 76,
  "cited_by_count": 426,
  "summary_stats": {
    "2yr_mean_citedness": 0,
    "h_index": 10,
    "i10_index": 11
  },
  "ids": {
    "openalex": "https://openalex.org/A5000007038"
  },
  "affiliations": [
    {
      "institution": {
        "id": "https://openalex.org/I38523324",
        "ror": "https://ror.org/03k7r0z51",
        "display_name": "Fachhochschule Wiener Neustadt",
        "country_code": "AT",
        "type": "education",
        "lineage": ["https://openalex.org/I38523324"]
      },
      "years": [2000]
    },
    {
      "institution": {
        "id": "https://openalex.org/I129774422",
        "ror": "https://ror.org/03prydq77",
        "display_name": "University of Vienna",
        "country_code": "AT",
        "type": "education",
        "lineage": ["https://openalex.org/I129774422"]
      },
      "years": [1992, 1989, 1988, 1984, 1983]
    },
    {
      "institution": {
        "id": "https://openalex.org/I4210122765",
        "ror": "https://ror.org/02p47pe37",
        "display_name": "Kaiser-Franz-Josef-Spital",
        "country_code": "AT",
        "type": "healthcare",
        "lineage": ["https://openalex.org/I4210117134", "https://openalex.org/I4210122765"]
      },
      "years": [1992]
    },
    {
      "institution": {
        "id": "https://openalex.org/I4210090358",
        "ror": "https://ror.org/00adn8q67",
        "display_name": "Universitätsklinik für Neurologie",
        "country_code": "AT",
        "type": "healthcare",
        "lineage": ["https://openalex.org/I2802328216", "https://openalex.org/I4210090358"]
      },
      "years": [1991]
    },
    {
      "institution": {
        "id": "https://openalex.org/I4210152163",
        "ror": "https://ror.org/04zvdfd56",
        "display_name": "Universitätszahnklinik Wien",
        "country_code": "AT",
        "type": "healthcare",
        "lineage": ["https://openalex.org/I4210152163"]
      },
      "years": [1989, 1988, 1987, 1986, 1985, 1984]
    },
    {
      "institution": {
        "id": "https://openalex.org/I4210102963",
        "ror": "https://ror.org/011ygts35",
        "display_name": "University Clinic of Traumatology",
        "country_code": "AT",
        "type": "healthcare",
        "lineage": ["https://openalex.org/I4210102963"]
      },
      "years": [1984]
    },
    {
      "institution": {
        "id": "https://openalex.org/I76134821",
        "ror": "https://ror.org/05n3x4p02",
        "display_name": "Medical University of Vienna",
        "country_code": "AT",
        "type": "education",
        "lineage": ["https://openalex.org/I76134821"]
      },
      "years": [1983, 1981, 1979]
    }
  ],
  "last_known_institution": {
    "id": "https://openalex.org/I129774422",
    "ror": "https://ror.org/03prydq77",
    "display_name": "University of Vienna",
    "country_code": "AT",
    "type": "education",
    "lineage": ["https://openalex.org/I129774422"]
  },
  "last_known_institutions": [
    {
      "id": "https://openalex.org/I38523324",
      "ror": "https://ror.org/03k7r0z51",
      "display_name": "Fachhochschule Wiener Neustadt",
      "country_code": "AT",
      "type": "education",
      "lineage": ["https://openalex.org/I38523324"]
    }
  ],
  "x_concepts": [
    {
      "id": "https://openalex.org/C71924100",
      "wikidata": "https://www.wikidata.org/wiki/Q11190",
      "display_name": "Medicine",
      "level": 0,
      "score": 101.3
    },
    {
      "id": "https://openalex.org/C126322002",
      "wikidata": "https://www.wikidata.org/wiki/Q11180",
      "display_name": "Internal medicine",
      "level": 1,
      "score": 88.2
    },
    {
      "id": "https://openalex.org/C141071460",
      "wikidata": "https://www.wikidata.org/wiki/Q40821",
      "display_name": "Surgery",
      "level": 1,
      "score": 76.3
    },
    {
      "id": "https://openalex.org/C86803240",
      "wikidata": "https://www.wikidata.org/wiki/Q420",
      "display_name": "Biology",
      "level": 0,
      "score": 68.4
    },
    {
      "id": "https://openalex.org/C15744967",
      "wikidata": "https://www.wikidata.org/wiki/Q9418",
      "display_name": "Psychology",
      "level": 0,
      "score": 48.7
    },
    {
      "id": "https://openalex.org/C118552586",
      "wikidata": "https://www.wikidata.org/wiki/Q7867",
      "display_name": "Psychiatry",
      "level": 1,
      "score": 47.4
    },
    {
      "id": "https://openalex.org/C54355233",
      "wikidata": "https://www.wikidata.org/wiki/Q7162",
      "display_name": "Genetics",
      "level": 1,
      "score": 44.7
    },
    {
      "id": "https://openalex.org/C142724271",
      "wikidata": "https://www.wikidata.org/wiki/Q7208",
      "display_name": "Pathology",
      "level": 1,
      "score": 38.2
    },
    {
      "id": "https://openalex.org/C164705383",
      "wikidata": "https://www.wikidata.org/wiki/Q10379",
      "display_name": "Cardiology",
      "level": 1,
      "score": 38.2
    },
    {
      "id": "https://openalex.org/C126838900",
      "wikidata": "https://www.wikidata.org/wiki/Q77604",
      "display_name": "Radiology",
      "level": 1,
      "score": 36.8
    },
    {
      "id": "https://openalex.org/C185592680",
      "wikidata": "https://www.wikidata.org/wiki/Q2329",
      "display_name": "Chemistry",
      "level": 0,
      "score": 34.2
    },
    {
      "id": "https://openalex.org/C134018914",
      "wikidata": "https://www.wikidata.org/wiki/Q162606",
      "display_name": "Endocrinology",
      "level": 1,
      "score": 31.6
    },
    {
      "id": "https://openalex.org/C121332964",
      "wikidata": "https://www.wikidata.org/wiki/Q413",
      "display_name": "Physics",
      "level": 0,
      "score": 25
    },
    {
      "id": "https://openalex.org/C55493867",
      "wikidata": "https://www.wikidata.org/wiki/Q7094",
      "display_name": "Biochemistry",
      "level": 1,
      "score": 23.7
    },
    {
      "id": "https://openalex.org/C90924648",
      "wikidata": "https://www.wikidata.org/wiki/Q120569",
      "display_name": "Gastroenterology",
      "level": 1,
      "score": 22.4
    },
    {
      "id": "https://openalex.org/C203014093",
      "wikidata": "https://www.wikidata.org/wiki/Q101929",
      "display_name": "Immunology",
      "level": 1,
      "score": 22.4
    }
  ],
  "counts_by_year": [
    {"year": 2023, "works_count": 0, "cited_by_count": 3},
    {"year": 2022, "works_count": 0, "cited_by_count": 1},
    {"year": 2021, "works_count": 0, "cited_by_count": 3},
    {"year": 2020, "works_count": 0, "cited_by_count": 3},
    {"year": 2019, "works_count": 0, "cited_by_count": 3},
    {"year": 2018, "works_count": 0, "cited_by_count": 5},
    {"year": 2017, "works_count": 0, "cited_by_count": 2},
    {"year": 2016, "works_count": 0, "cited_by_count": 1},
    {"year": 2015, "works_count": 0, "cited_by_count": 2},
    {"year": 2014, "works_count": 0, "cited_by_count": 8},
    {"year": 2013, "works_count": 0, "cited_by_count": 6},
    {"year": 2012, "works_count": 0, "cited_by_count": 6}
  ],
  "works_api_url": "https://api.openalex.org/works?filter=author.id:A5000007038",
  "updated_date": "2024-01-22T05:52:41.745080",
  "created_date": "2023-07-21"
}

# Ajouter les triplets RDF
g.add((ex.A5000007038, RDF.type, schema.Person))
g.add((ex.A5000007038, schema.name, Literal(data['display_name'])))
g.add((ex.A5000007038, dct.worksCount, Literal(data['works_count'], datatype=XSD.integer)))
g.add((ex.A5000007038, dct.citedByCount, Literal(data['cited_by_count'], datatype=XSD.integer)))

# Ajouter les auteurs alternatifs
for alt_name in data['display_name_alternatives']:
    g.add((ex.A5000007038, schema.author, Literal(alt_name)))

# Ajouter les statistiques de résumé
summary_stats = data['summary_stats']
summary_stats_node = ex.A5000007038 + "_summary_stats"
g.add((ex.A5000007038, schema.summaryStats, summary_stats_node))
g.add((summary_stats_node, schema.meanCitedness, Literal(summary_stats['2yr_mean_citedness'], datatype=XSD.integer)))
g.add((summary_stats_node, schema.hIndex, Literal(summary_stats['h_index'], datatype=XSD.integer)))
g.add((summary_stats_node, schema.i10Index, Literal(summary_stats['i10_index'], datatype=XSD.integer)))

# Ajouter les identifiants
ids = data['ids']
for key, value in ids.items():
    g.add((ex.A5000007038, schema.ids, Literal(value)))

# Ajouter les affiliations
affiliations = data['affiliations']
for affiliation in affiliations:
    institution = affiliation['institution']
    institution_node = Namespace(institution['id'])
    #g.add((ex.A5000007038, schema.affiliation, institution_node))
    #g.add((institution_node, RDF.type, schema.Organization))
    #g.add((institution_node, schema.name, Literal(institution['display_name'])))
    #g.add((institution_node, schema.identifier, Literal(institution['id'])))
    #g.add((institution_node, schema.locationCountry, Literal(institution['country_code'])))
    #g.add((institution_node, schema.type, Literal(institution['type'])))
    lineage = institution['lineage']
    for l in lineage:
        g.add((institution_node, schema.lineage, Namespace(l)))
    years = affiliation['years']
    for year in years:
        g.add((institution_node, schema.years, Literal(year, datatype=XSD.integer)))

# Ajouter la dernière institution connue
last_known_institution = data['last_known_institution']
last_known_institution_node = Namespace(last_known_institution['id'])
g.add((ex.A5000007038, schema.lastKnownInstitution, last_known_institution_node))
g.add((last_known_institution_node, RDF.type, schema.Organization))
g.add((last_known_institution_node, schema.name, Literal(last_known_institution['display_name'])))
g.add((last_known_institution_node, schema.identifier, Literal(last_known_institution['id'])))
g.add((last_known_institution_node, schema.locationCountry, Literal(last_known_institution['country_code'])))
g.add((last_known_institution_node, schema.type, Literal(last_known_institution['type'])))
lineage = last_known_institution['lineage']
for l in lineage:
    g.add((last_known_institution_node, schema.lineage, Namespace(l)))

# Ajouter les institutions connues précédentes
last_known_institutions = data['last_known_institutions']
for last_known_inst in last_known_institutions:
    last_known_inst_node = Namespace(last_known_inst['id'])
    g.add((ex.A5000007038, schema.lastKnownInstitutions, last_known_inst_node))
    g.add((last_known_inst_node, RDF.type, schema.Organization))
    g.add((last_known_inst_node, schema.name, Literal(last_known_inst['display_name'])))
    g.add((last_known_inst_node, schema.identifier, Literal(last_known_inst['id'])))
    g.add((last_known_inst_node, schema.locationCountry, Literal(last_known_inst['country_code'])))
    g.add((last_known_inst_node, schema.type, Literal(last_known_inst['type'])))
    lineage = last_known_inst['lineage']
    for l in lineage:
        g.add((last_known_inst_node, schema.lineage, Namespace(l)))

# Ajouter les concepts X
x_concepts = data['x_concepts']
for concept in x_concepts:
    concept_node = Namespace(concept['id'])
    g.add((ex.A5000007038, schema.xConcepts, concept_node))
    g.add((concept_node, RDF.type, schema.Concept))
    g.add((concept_node, schema.name, Literal(concept['display_name'])))
    g.add((concept_node, schema.wikidata, Literal(concept['wikidata'])))
    g.add((concept_node, schema.level, Literal(concept['level'], datatype=XSD.integer)))
    g.add((concept_node, schema.score, Literal(concept['score'], datatype=XSD.float)))

# Ajouter les comptes par année
counts_by_year = data['counts_by_year']
for count in counts_by_year:
    count_node = ex.A5000007038 + "_counts_" + str(count['year'])
    g.add((ex.A5000007038, schema.countsByYear, count_node))
    g.add((count_node, RDF.type, schema.YearCount))
    g.add((count_node, schema.year, Literal(count['year'], datatype=XSD.integer)))
    g.add((count_node, schema.worksCount, Literal(count['works_count'], datatype=XSD.integer)))
    g.add((count_node, schema.citedByCount, Literal(count['cited_by_count'], datatype=XSD.integer)))

# Ajouter l'URL de l'API des travaux
g.add((ex.A5000007038, schema.worksApiUrl, Literal(data['works_api_url'])))

# Ajouter la date de mise à jour et la date de création
g.add((ex.A5000007038, dct.created, Literal(data['created_date'], datatype=XSD.date)))
g.add((ex.A5000007038, dct.modified, Literal(data['updated_date'], datatype=XSD.date)))

# Afficher le graph RDF
print(g.serialize(format="turtle").decode())
