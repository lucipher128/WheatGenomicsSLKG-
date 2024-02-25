import json 
import re 
import requests

def add_authors():
    file = open("../../article_complete_0.ttl","r")

    buffer = "" 
    sch_auth = "schema:author "
    ans = None
    print("@prefix cito: <http://purl.org/spar/cito> .")
    for line in file:
        line = line.strip()
        if(not line) : 
            continue
        elif(re.search("^<https://",line)):
                print('\n')
                pmid = re.search("<.*>",line)
                if(pmid): 
                    pmid = re.search("\d+$",re.sub("(<|>)","",pmid.group())).group()
                    ans = requests.get("https://api.openalex.org/works/pmid:" + pmid + "?select=authorships,id")
                    if(ans.ok):
                        citations = requests.get("https://api.openalex.org/works?filter=cites:" + re.search("W\d*",ans.json()["id"]).group() + "&select=ids")
                        pp = json.loads(ans.text)
                        tmp = sch_auth +"<"+pp["authorships"][0]["author"]["id"]+">;\n"
                        buffer = re.sub("dc:creator\s\".+\s.*\s*.*\"\s;$",tmp ,line)
                        for author in ans.json()["authorships"][1:]:
                            tmp = sch_auth + "<" + author["author"]["id"] + ">;\n"
                            buffer = buffer + tmp
                        if(citations.ok):
                            for article in citations.json()["results"]:
                                try:
                                    buffer = buffer + "cito:cites " +"<"+article["ids"]["pmid"] + ">;\n"
                                except:
                                    try:
                                        buffer = buffer + "cito:cites " +"<"+article["ids"]["openalex"] + ">;\n"
                                    except:
                                        continue
                    else:
                        buffer = buffer + line

        elif(re.search("^dc:creator", line)):
            continue
        else :
            buffer = buffer + line
        print(buffer.strip())
        buffer  = ""

def gen_article_ttl():
    file = open("../original/united_articles.ttl","r")
    output = open('../output/enlarged_articles/united_out.ttl','w')

    buffer = "" 
    sch_auth = "schema:author "
    buffer = buffer + "@prefix cito: <http://purl.org/spar/cito> .\n"
    articles = open("../json/all_articles_fullOA.json","r")
    citations = open("../json/citations_all_articles.json","r")
    count = 0
    for line in file : 
        try:
            if (re.search("^<https",line)):
                count = count + 1
                print(count)
                json_article = json.loads(articles.readline())
                json_citation = json.loads(citations.readline())
                try:
                    tmp = sch_auth +"<"+json_article["authorships"][0]["author"]["id"]+">;"
                    new_line_id = re.sub("dc:creator\s\".+\s.*\s*.*\"\s;$",tmp,line)
                    buffer = buffer + new_line_id
                except:
                    buffer = buffer + line
                for author in json_article['authorships'][1:] : 
                    tmp = sch_auth +"<"+author['author']['id']+">;\n"
                    buffer = buffer + tmp
                for citation in json_citation[list(json_citation.keys())[0]] :
                    try : 
                        buffer = buffer + "cito:cites " +"<"+citation["ids"]["pmid"] + ">;\n"
                    except:
                        buffer = buffer + "cito:cites " +"<"+citation["ids"]["openalex"] + ">;\n"

            elif (re.search("^dc:creator",line)):
                continue
            else:
                buffer = buffer + line
        except: 
            buffer = buffer + line
    
    output.writelines(buffer);
    output.close()







#add_authors()
gen_article_ttl()
