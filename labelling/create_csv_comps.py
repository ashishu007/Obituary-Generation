# Script for the automated conversion of tagged xml obituaries into 
# tabular format stored in csv file.

import pandas as pd
import numpy as np
import jsonlines, re
from bs4 import BeautifulSoup

# Load the xml file
infile = open("./resources/xml-tagged-comps.xml","r")
contents = infile.read()
soup = BeautifulSoup(contents,'lxml')

# Extract the three components into three different lists
g1 = soup.find_all('personal_info_component')
g2 = soup.find_all('relations_component')
g3 = soup.find_all('funeral_component')

# For every component 
for comp in [g1, g2, g3]:
    
    # Get all the unique tags
    tags = []
    for i in comp:
        for tag in i.find_all():
            tags.append(tag.name)
    all_tags = list(set(tags))

    # Create a dictionary with each tag name as the key
    d = {}
    for i in all_tags:
        d[i] = []
    
    # Add an extra key for the whole text for that sample
    d["text"] = []

    # For each sample
    for i in range(len(comp)):
        # For each tag in the tag_list
        for j in all_tags:
            # get the value for each tag
            val = comp[i].find_all(j)
            # if tag is present the text add the value of tag in the table otherwise 0
            if len(val) != 0:
                d[j].append(val[0].text)
            else:
                d[j].append(0)    
        d["text"].append(comp[i])

    # convert into dataframe
    df = pd.DataFrame(d)

    # save the dataframe into csv file
    if comp == g1:
        df.to_csv("./data/personal_info_component.csv", index=0)
    elif comp == g2:
        df.to_csv("./data/relations_component.csv", index=0)
    else:
        df.to_csv("./data/funeral_component.csv", index=0)