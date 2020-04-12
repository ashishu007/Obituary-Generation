import pandas as pd
import numpy as np
import jsonlines, re, string
from bs4 import BeautifulSoup

objs = []
with jsonlines.open('./data/tagged.json1') as reader:
    for obj in reader:
        objs.append(obj)

li = []
for i in objs:
    di = {
        "text": i["text"],
        "labels": sorted(i["labels"])
    }
    li.append(di)

new_list = []
for i in li:
    t = i
    ctr = 0
    s = t["text"]
    for i in t["labels"]:
        s = s[:i[0] + ctr] + "<" + i[2] + ">" + s[i[0] + ctr:]
        s = s[:i[1] + len(i[2]) + 2 + ctr] + "</" + i[2] + ">" + s[i[1] + len(i[2]) + ctr + 2:]
        ctr = ctr + ((2 * len(i[2])) + 5)
    s = s.replace("\"", "")
    s = s.replace("\\", "")
    new_list.append(s)

# Save as basic retrieval method
for i in new_list:
    sn = "<obit>\n" + i + "\n" + "</obit>\n"
    with open("./data/xml-tagged.xml", "a+") as f:
        f.write(sn)
    f.close()