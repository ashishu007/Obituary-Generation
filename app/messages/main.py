from app.messages.personal_info import personal_info_component
from app.messages.relations import relations_component
from app.messages.spouse import spouse_component
from app.messages.funeral import funeral_component
from app.messages.single_comp import single_component
from app.messages.errors import gender_errors
import numpy as np
from datetime import datetime

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

    # for k, v in ftrs.items():
    #     print(type(v))

    return ftrs

def create_comp_ftrs(diction):

    pinfo = {}
    relations = {}
    funeral = {}

    p = ["name", "age", "demise_place", "demise_date", "demise_how", "home_town", "gender", "nick_name"]
    r = ["parent_gender", "spouse_name", "spouse_gender", "grandparent_gender", "children_name", "grandchildren_name", "great_grandchildren_name", "great_grandparent_gender",
            "siblings_name", "siblings_gender", "children_in_law_name", "parent_in_law_gender", "siblings_in_law_name", "siblings_in_law_gender", "other_relations_names",
            "other_relations_types", "friends_name"]
    f = ["funeral_place", "funeral_date", "funeral_time", "cemetery_place", "cemetery_time", "flowers", "guests_list", "funeral_attire", "charity_name", "reception_place",
            "reception_time", "reception_date", "funeral_message"]

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

def return_comp_messages(response):
    """
    Component Retreival
    """
    personal_info_features, relations_features, funeral_features = create_comp_ftrs(response)
    info_str = personal_info_component(personal_info_features)
    funeral_str = funeral_component(funeral_features)
    rel_str = relations_component(relations_features)
    random_list = [0, 1, 2, 3]
    msg_lst = []

    deceased_geneder = personal_info_features["gender"]

    message1 = info_str[random_list[0]] + " " + ". " + rel_str[random_list[0]] + "\n\n" + funeral_str[random_list[0]]
    msg_lst.append(message1)
    message2 = info_str[random_list[1]] + " " + ". " + rel_str[random_list[1]] + "\n\n" + funeral_str[random_list[1]]
    msg_lst.append(message2)
    message3 = info_str[random_list[2]] + " " + ". " + rel_str[random_list[2]] + "\n\n" + funeral_str[random_list[2]]
    msg_lst.append(message3)
    message4 = info_str[random_list[3]] + " " + ". " + rel_str[random_list[3]] + "\n\n" + funeral_str[random_list[3]]
    msg_lst.append(message4)

    corrected_lst = []
    for i in msg_lst:
        correct_i = gender_errors(i, deceased_geneder)
        corrected_lst.append(correct_i)

    return corrected_lst

def return_basic_msgs(response):
    """
    Basic Retreival
    """
    basic_ftrs = create_basic_ftrs(response)
    # print(basic_ftrs)

    deceased_geneder = basic_ftrs["gender"]

    msg_lst = single_component(basic_ftrs)

    corrected_lst = []
    for i in msg_lst:
        correct_i = gender_errors(i, deceased_geneder)
        corrected_lst.append(correct_i)

    return corrected_lst