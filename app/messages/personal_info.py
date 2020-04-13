# generate the personal_info component text
# input: dictionary of features
# output: four generated messages

# other comments similar as funeral.py

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import re, os

def personal_info_component(features):
    # personal_info_string = ""
    personal_info_strings = []

    # print(os.getcwd())

    df = pd.read_csv('./app/messages/data/personal_component.csv')
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
            if j != "age":
                if df[j][i] != str(0) and (j in features.keys()):
                    score += 1
            if j == "age":
                if df[j][i] != str(0) and (j in features.keys()):
                    # print(df["age"][i])
                    int_val_age = int(re.findall(r'\d+', df["age"][i])[0])
                    age_val = 1 - (np.sqrt(np.square(int_val_age - features["age"]))/110)
                    score += age_val

            # Now check if there are some features which are present in train but not in test, then reduce the score
            # for those train samples
            if df[j][i] != str(0) and (j not in features.keys()):
                score -= 1

        scores.append(score)
    
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
                # print("features[i]", features[i.name])
                if i.name == "age":
                    i.string = str(features[i.name]) + " years"
                else:
                    i.string = features[i.name]
            # Remove the tags/features from generated text which are not in input
            elif i.name == "personal_info_component" or i.name == "html" or i.name == "body":
                pass
            elif i.name not in features.keys():
                i.string = ""
        
        gen_str = top_val_soup.text
        gen_str = ' '.join(gen_str.split())

        # personal_info_string = gen_str
        personal_info_strings.append(gen_str)

    return personal_info_strings