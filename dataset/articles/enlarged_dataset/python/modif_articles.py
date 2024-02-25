import re
import json

x = open("../article_complete_2.ttl","r")
references_OA = open("w","r")

for line in x :
    y = re.search("^dc:creator",line)
    if(y):
        name_tmp = re.search("\".*\"",line)
        if(name_tmp):
            name = name_tmp.group().replace("\"","")
        res = re.sub("\".*\"","test",line)
