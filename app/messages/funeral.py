# generate the funeral component text
# input: dictionary of features
# output: four generated messages

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import re

def funeral_component(features):
    funeral_strings = []
    # print(features)

    # load the case-base for funeral component
    df = pd.read_csv('./app/messages/data/funeral_component.csv')
    key_vals = list(df)
    key_vals.remove('text')
    # print(key_vals)
    # print(features.keys())
    
    # apply the similarity measure and rank the samples in case-base 
    # according to decreasing order of their similarity with the input features
    scores = []    
    for i in range(len(df)):
        # print(df["text"][i])
        score = 0
        for j in key_vals:
            # If the feature is present in the sample from case-base as well as the target case
            # increase the score
            if df[j][i] != str(0) and (j in features.keys()):
                score += 1
            # Now check if there are some features which are present in sample from case-base but not in target case
            # then reduce the score for those samples
            if df[j][i] != str(0) and (j not in features.keys()):
                score -= 1

        scores.append(score)
    
    # select top four similar cases 
    tops = sorted(range(len(scores)), key=lambda i: scores[i])[-4:]
    
    # for each case in the top 4 
    for rank in tops:
        top_ind = rank
        # top_ind = tops[0]
        
        top_val = (df["text"][top_ind])
        
        top_val_soup = BeautifulSoup(top_val, features="lxml")
        
        top_str = (top_val_soup.text)

        top_str = ' '.join(top_str.split())
            
        # print(top_str)
        
        # generate the texts
        for i in top_val_soup.find_all():
            # print(i.name, i.string)
            if i.name in features.keys():
                i.string = features[i.name]
            # Remove the tags/features from generated text which are not in input
            elif i.name == "funeral_component" or i.name == "html" or i.name == "body":
                pass
            elif i.name not in features.keys():
                i.string = ""
        
        gen_str = top_val_soup.text
        gen_str = ' '.join(gen_str.split())

        # funeral_string = gen_str
        funeral_strings.append(gen_str)

    return funeral_strings