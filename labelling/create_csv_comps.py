import pandas as pd
import numpy as np
import jsonlines, re
from bs4 import BeautifulSoup

infile = open("./resources/xml-tagged-comps.xml","r")
contents = infile.read()
soup = BeautifulSoup(contents,'lxml')

g1 = soup.find_all('personal_info_component')
g2 = soup.find_all('relations_component')
g3 = soup.find_all('funeral_component')

for comp in [g1, g2, g3]:
    tags = []

    for i in comp:
        for tag in i.find_all():
            tags.append(tag.name)
            
    all_tags = list(set(tags))

    d = {}

    for i in all_tags:
        d[i] = []
        
    d["text"] = []

    for i in range(len(comp)):
        for j in all_tags:
            val = comp[i].find_all(j)
            if len(val) != 0:
                d[j].append(val[0].text)
            else:
                d[j].append(0)    
        d["text"].append(comp[i])

    df = pd.DataFrame(d)
    if comp == g1:
        df.to_csv("./data/personal_info_component.csv", index=0)
    elif comp == g2:
        df.to_csv("./data/relations_component.csv", index=0)
    else:
        df.to_csv("./data/funeral_component.csv", index=0)