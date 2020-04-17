# file to collect all the generated texts from different methods

from app.messages.personal_info import personal_info_component
from app.messages.relations import relations_component
from app.messages.funeral import funeral_component
from app.messages.basic import basic_generation
from app.messages.errors import gender_errors
from app.messages.utility import gender_features, create_basic_ftrs, create_comp_ftrs
import numpy as np
import pandas as pd


# main function for collecting and sending four generated texts using component retrieval method
def return_comp_messages(response):
    """
    Component Retreival
    """

    response = gender_features(response)

    # get the curated features dictionary
    personal_info_features, relations_features, funeral_features = create_comp_ftrs(response)

    # get texts for personal_info_component
    info_str = personal_info_component(personal_info_features)

    # get texts for funeral_component
    funeral_str = funeral_component(funeral_features)

    # get texts for relations_component
    rel_str = relations_component(relations_features)

    # generate four different messages
    random_list = [0, 1, 2, 3]
    msg_lst = []
    message1 = info_str[random_list[0]] + " " + ". " + rel_str[random_list[0]] + ". " + funeral_str[random_list[0]]
    msg_lst.append(message1)
    message2 = info_str[random_list[1]] + " " + ". " + rel_str[random_list[1]] + ". " + funeral_str[random_list[1]]
    msg_lst.append(message2)
    message3 = info_str[random_list[2]] + " " + ". " + rel_str[random_list[2]] + ". " + funeral_str[random_list[2]]
    msg_lst.append(message3)
    message4 = info_str[random_list[3]] + " " + ". " + rel_str[random_list[3]] + ". " + funeral_str[random_list[3]]
    msg_lst.append(message4)

    # apply rule-based error handling for gender based mistakes
    deceased_geneder = personal_info_features["gender"]
    corrected_lst = []
    for i in msg_lst:
        correct_i = gender_errors(i, deceased_geneder)
        corrected_lst.append(correct_i)

    return corrected_lst

# main function for collecting and sending four generated texts using basic retrieval method
def return_basic_msgs(response):
    """
    Basic Retreival
    """

    print("Befor gender features")

    response = gender_features(response)

    print("After gender features")
    # get the features dictionary
    basic_ftrs = create_basic_ftrs(response)
    
    # get the different messages
    msg_lst = basic_generation(basic_ftrs)

    # apply rule-based error handling for gender based mistakes
    deceased_geneder = basic_ftrs["gender"]
    corrected_lst = []
    for i in msg_lst:
        correct_i = gender_errors(i, deceased_geneder)
        corrected_lst.append(correct_i)

    return corrected_lst