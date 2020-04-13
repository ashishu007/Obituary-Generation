import pandas as pd
import numpy as np
import jsonlines, re
from bs4 import BeautifulSoup

infile = open("./resources/xml-tagged.xml","r")
contents = infile.read()
soup = BeautifulSoup(contents,'lxml')

g0 = soup.find_all('obit')

tags = []

for i in g0:
    for tag in i.find_all():
        tags.append(tag.name)
        
all_tags = list(set(tags))

d = {}

for i in all_tags:
    d[i] = []
    
d["text"] = []

for i in range(len(g0)):
    for j in all_tags:
        val = g0[i].find_all(j)
        if len(val) != 0:
            d[j].append(val[0].text)
        else:
            d[j].append(0)    
    d["text"].append(g0[i])

df = pd.DataFrame(d)
df.to_csv("./data/basic.csv", index=0)