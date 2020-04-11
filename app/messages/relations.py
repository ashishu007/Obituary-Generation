import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import re

def relations_component(features):
    # relations_string = ""
    relations_strings = []

    df = pd.read_csv('./app/messages/data/101_relations_component.csv')
    key_vals = list(df)
    key_vals.remove('text')
    # print(key_vals)
    # print(features.keys())
    
    scores = []
    
    for i in range(len(df)):
        # print(df["text"][i])
        score = 0
        for j in key_vals:
            # print(j)
            if df[j][i] != str(0) and (j in features.keys()):
                score += 1

            # Now check if there are some features which are present in train but not in test, then reduce the score
            # for those train samples
            if df[j][i] != str(0) and (j not in features.keys()):
                score -= 1

        scores.append(score)
    
    tops = sorted(range(len(scores)), key=lambda i: scores[i])[-4:]

    for rank in tops:
        # top_ind = tops[0]
        top_ind = rank
        
        top_val = (df["text"][top_ind])
        
        top_val_soup = BeautifulSoup(top_val, features="lxml")
        
        top_str = (top_val_soup.text)

        top_str = ' '.join(top_str.split())
            
        # print(top_str)
        
        for i in top_val_soup.find_all():
            # print(i.name, i.string)
            if i.name in features.keys():
                # print("features[i]", features[i.name])
                # if i.name == "age":
                #     i.string = str(features[i.name]) + " years"
                # else:
                i.string = features[i.name]
    
        gen_str = top_val_soup.text
        gen_str = ' '.join(gen_str.split())

        # relations_string = gen_str
        relations_strings.append(gen_str)

    return relations_strings