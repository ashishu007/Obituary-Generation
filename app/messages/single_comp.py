import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import re

def single_component(features):
    # single_component_strings = ""
    single_component_strings = []

    df = pd.read_csv('./app/messages/data/101_single_component.csv')
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
            elif j == "spouse_gender":
                if df[j][i] != str(0) and (j in features.keys()):
                    if df[j][i] == features[j]:
                        score += 1
            # elif j == "flower_score" or j == "guest_score":
            #     if df[j][i] != str(0) and (j in features.keys()):
            #         if df[j][i] == features[j]:
            #             score += 1
            else:
                if df[j][i] != str(0) and (j in features.keys()):
                    score += 1


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
                # print("features[i]", features[i.name])
                # print("features[i]", features[i.name], i.string)
                # print("i.name", i.name)
                # print(i.name == "age")
                if i.name == "age":
                    i.string = str(features[i.name]) + " years"
                # elif i.name == "flowers" or i.name == "guests_list":
                #     i.string = i.string
                else:
                    # print("features[i]", features[i.name], i.string, i.name)
                    i.string = features[i.name]
        
        gen_str = top_val_soup.text
        gen_str = ' '.join(gen_str.split())

        # personal_info_string = gen_str
        single_component_strings.append(gen_str)

    return single_component_strings