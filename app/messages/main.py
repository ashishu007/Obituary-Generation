from app.messages.personal_info import personal_info_component
from app.messages.relations import relations_component
from app.messages.spouse import spouse_component
from app.messages.funeral import funeral_component
from app.messages.single_comp import single_component
import numpy as np
from datetime import datetime

def create_basic_ftrs(diction):

    ftrs = {}

    for k, v in diction.items():
        if v[0] != '':
            if k == "demise_date":
                dobj = datetime.strptime(v[0], "%Y-%m-%d")
                t = dobj.strftime("%d %B %Y")
                ftrs[k] = str(t)
            elif k == "age":
                ftrs[k] = int(v[0])
            else:
                ftrs[k] = v[0]

    for k, v in ftrs.items():
        print(type(v))

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
        if k in p:
            pinfo[k] = v[0]
        elif k in r:
            relations[k] = v[0]
        else:
            funeral[k] = v[0]

    return pinfo, relations, funeral

def return_msgs(response):

    """
    Component Retreival
    """
    # personal_info_features, relations_features, funeral_features = create_comp_ftrs(response)
    # info_str = personal_info_component(personal_info_features)
    # funeral_str = funeral_component(funeral_features)
    # rel_str = relations_component(relations_features)
    # random_list = [0, 1, 2, 3]
    # msg_lst = []

    # message1 = info_str[random_list[0]] + " " + ". " + rel_str[random_list[0]] + "\n\n" + funeral_str[random_list[0]]
    # msg_lst.append(message1)
    # message2 = info_str[random_list[1]] + " " + ". " + rel_str[random_list[1]] + "\n\n" + funeral_str[random_list[1]]
    # msg_lst.append(message2)
    # message3 = info_str[random_list[2]] + " " + ". " + rel_str[random_list[2]] + "\n\n" + funeral_str[random_list[2]]
    # msg_lst.append(message3)
    # message4 = info_str[random_list[3]] + " " + ". " + rel_str[random_list[3]] + "\n\n" + funeral_str[random_list[3]]
    # msg_lst.append(message4)

    """
    Basic Retreival
    """
    basic_ftrs = create_basic_ftrs(response)
    print(basic_ftrs)

    msg_lst = single_component(basic_ftrs)

    return msg_lst