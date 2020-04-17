# Utility functions for CBR part
# Mainly feature and component related

import pandas as pd
from datetime import datetime

# add the gender specific relation values in features dictionary
def gender_features(ftrs):
    if ftrs["gender"] == "M":
        print("inside if M")
        if "spouse_name" in list(ftrs.keys()):
            ftrs["spouse_gender"] = "husband"
        if "children_name" in list(ftrs.keys()):
            ftrs["parent_gender"] = "father"
        if "grandchildren_name" in list(ftrs.keys()):
            ftrs["grandparent_gender"] = "papa"
        if "great_grandchildren_name" in list(ftrs.keys()):
            ftrs["great_grandparent_gender"] = "great papa"
        if "children_in_law_name" in list(ftrs.keys()):
            ftrs["parent_in_law_gender"] = "father in law"
        if "siblings_name" in list(ftrs.keys()):
            ftrs["siblings_gender"] = "brother"

    if ftrs["gender"] == "F":
        print("inside if F")
        if "spouse_name" in list(ftrs.keys()):
            ftrs["spouse_gender"] = "wife"
        if "children_name" in list(ftrs.keys()):
            ftrs["parent_gender"] = "mother"
        if "grandchildren_name" in list(ftrs.keys()):
            ftrs["grandparent_gender"] = "nana"
        if "great_grandchildren_name" in list(ftrs.keys()):
            ftrs["great_grandparent_gender"] = "great nana"
        if "children_in_law_name" in list(ftrs.keys()):
            ftrs["parent_in_law_gender"] = "mother in law"
        if "siblings_name" in list(ftrs.keys()):
            ftrs["siblings_gender"] = "sister"

    print("Feature list after adding gender specific relations features", ftrs)
    return ftrs

# function to create dictionary of basic features taking care of different data-types
def create_basic_ftrs(diction):

    ftrs = {}
    for k, v in diction.items():
        if v != '':
            if k == "demise_date" or k == "funeral_date":
                # dobj = datetime.strptime(v, "%Y-%m-%d")
                t = v.strftime("%d %B %Y")
                ftrs[k] = str(t)
            elif k == "age":
                ftrs[k] = int(v)
            else:
                ftrs[k] = v

    if "nick_name" not in list(ftrs.keys()):
        ftrs["nick_name"] = (ftrs["name"].split(" "))[0]

    return ftrs

# function to create dictionary of component features divided into three different entities
def create_comp_ftrs(diction):

    pinfo = {}
    relations = {}
    funeral = {}

    # load the feature list
    df = pd.read_csv("./app/messages/resources/feature_list.csv")

    p = []
    r = []
    f = []

    for id, row in df.iterrows():
        if row["Type"] == "Personal Info":
            p.append(row["Name"])
        elif row["Type"] == "Relations":
            r.append(row["Name"])
        else:
            f.append(row["Name"])

    # p = ["name", "age", "demise_place", "demise_date", "demise_how", "home_town", "gender", "nick_name"]
    # r = ["parent_gender", "spouse_name", "spouse_gender", "grandparent_gender", "children_name", "grandchildren_name", "great_grandchildren_name", "great_grandparent_gender",
    #         "siblings_name", "siblings_gender", "children_in_law_name", "parent_in_law_gender", "siblings_in_law_name", "siblings_in_law_gender", "other_relations_names",
    #         "other_relations_types", "friends_name"]
    # f = ["funeral_place", "funeral_date", "funeral_time", "cemetery_place", "cemetery_time", "flowers", "guests_list", "funeral_attire", "charity_name", "reception_place",
    #         "reception_time", "reception_date", "funeral_message"]

    for k, v in diction.items():
        
        # Personal Info
        if k in p:
            if k == "demise_date":
                t = v.strftime("%d %B %Y")
                pinfo[k] = str(t)
            elif k == "age":
                pinfo[k] = int(v)
            else:
                pinfo[k] = v

        # Relations 
        elif k in r:
            relations[k] = v

        # Funeral
        else:
            if k == "funeral_date":
                t = v.strftime("%d %B %Y")
                funeral[k] = t
            else:
                funeral[k] = v

    return pinfo, relations, funeral
