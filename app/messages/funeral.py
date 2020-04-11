import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import re

def funeral_component(features):
    funeral_strings = []
    # funeral_string = ""

    print(features)

    df = pd.read_csv('./app/messages/data/101_funeral_component.csv')
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
            # if j == "flower_score" or j == "guest_score":
            #     if df[j][i] != str(0) and (j in features.keys()):
            #         if df[j][i] == features[j]:
            #             score += 1
            # else:
            if df[j][i] != str(0) and (j in features.keys()):
                score += 1

            # Now check if there are some features which are present in train but not in test, then reduce the score
            # for those train samples
            if df[j][i] != str(0) and (j not in features.keys()):
                score -= 1

        scores.append(score)
    
    tops = sorted(range(len(scores)), key=lambda i: scores[i])[-4:]
    
    for rank in tops:
        top_ind = rank
        # top_ind = tops[0]
        
        top_val = (df["text"][top_ind])
        
        top_val_soup = BeautifulSoup(top_val, features="lxml")
        
        top_str = (top_val_soup.text)

        top_str = ' '.join(top_str.split())
            
        # print(top_str)
        
        for i in top_val_soup.find_all():
            # print(i.name, i.string)
            if i.name in features.keys():
                # print("features[i]", features[i.name])
                # if i.name == "flowers" or i.name == "guests_list":
                    # i.string = i.string
                # else:
                i.string = features[i.name]
        
        gen_str = top_val_soup.text
        gen_str = ' '.join(gen_str.split())

        # funeral_string = gen_str
        funeral_strings.append(gen_str)

    return funeral_strings