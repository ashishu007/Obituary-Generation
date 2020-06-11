# generate the texts for basic-retrieval method
# input: dictionary of features
# output: four generated messages

# other comments similar as funeral.py


import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import re

def basic_generation(features):
    # single_component_strings = ""
    basic_strings = []

    df = pd.read_csv('./app/messages/data/basic.csv')
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
            if j == "age":
                if df[j][i] != str(0) and (j in features.keys()):
                    # print(df["age"][i])
                    int_val_age = int(re.findall(r'\d+', df["age"][i])[0])
                    age_val = 1 - (np.sqrt(np.square(int_val_age - int(features["age"])))/110)
                    score += age_val
            elif j == "spouse_name":
                if df[j][i] != str(0) and (j in features.keys()):
                    score += 1
            # elif j == "spouse_gender":
            #     if df[j][i] != str(0) and (j in features.keys()):
            #         if df[j][i] == features[j]:
            #             score += 1
            # elif j == "flower_score" or j == "guest_score":
            #     if df[j][i] != str(0) and (j in features.keys()):
            #         if df[j][i] == features[j]:
            #             score += 1
            else:
                if df[j][i] != str(0) and (j in features.keys()):
                    score += 1

            # # Now check if there are some features which are present in train but not in test, then reduce the score
            # # for those train samples
            # if df[j][i] != str(0) and (j not in features.keys()):
            #     score -= 1

        scores.append(score)
    # print(scores)
    
    tops = sorted(range(len(scores)), key=lambda i: scores[i])[-4:]
    # print(tops)
    
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
                if i.name == "age":
                    i.string = str(features[i.name]) + " years"
                else:
                    i.string = features[i.name]
            # Remove the tags/features from generated text which are not in input
            elif i.name == "obit" or i.name == "html" or i.name == "body":
                pass
            elif i.name not in features.keys():
                i.string = ""
        
        gen_str = top_val_soup.text
        gen_str = ' '.join(gen_str.split())

        # personal_info_string = gen_str
        basic_strings.append(gen_str)

    return basic_strings