from app.messages.personal_info import personal_info_component
from app.messages.relations import relations_component
from app.messages.spouse import spouse_component
from app.messages.funeral import funeral_component
from app.messages.single_comp import single_component
import numpy as np

personal_info_features = {
    "name": "HORNELL ANN",
    "age": 65,
    "demise_place": "Lochmaben Hospital",
    'demise_date': "2nd September 2016",
    'demise_how': "peacefully",
    'home_town': "Brooms Road, Dumfries",
    "gender": "F",
    'nick_name': "Annie"
}

relations_features = {
    "spouse_name": "Late Ian",
    "spouse_gender": "wife",
    'grandparent_gender': "grandmother",
    'grandchildren_name': "Grace, Cathie and Meg",
    'great_grandchildren_name': "Rowan",
    'great_grandparent_gender': "great-gran",
    'children_name': "Carol, Michael, Catherine and Stephen",
    'parent_gender': "mother",
    'children_in_law_name': "Michael",
    'parent_in_law_gender': "mother-in-law",
    'siblings_gender': "sister",
    'siblings_name': "Grace, Cathie and Meg",
    # 'other_relations_names': ,
    # 'other_relations_types': ,
}

funeral_features = {
    'funeral_place': "St Michael's RC Church, Linlithgow",
    'flowers': "Family flowers only",
    'cemetery_time': "11.15 am",
    'funeral_time': "10 am",
    'cemetery_place': "Kingscavil Cemetery",
    'guests_list': "all friends and family",
    'charity_name': "British Heart Foundation",
    'funeral_date': "Friday, April 12",
    'nick_name': "Annie"
}

def return_msgs():
    # info_str = personal_info_component(personal_info_features)
    # funeral_str = funeral_component(funeral_features)
    # rel_str = relations_component(relations_features)

    # random_list = [0, 1, 2, 3]
    # random_list = np.random.randint(4, size=4)
    # print(random_list)
    # print(len(info_str), len(spouse_str), len(funeral_str), len(rel_str))

    # msg_lst = []

    # print("\nCompnents \n")

    # message1 = info_str[random_list[0]] + " " + ". " + rel_str[random_list[0]] + "\n\n" + funeral_str[random_list[0]]
    # # print("\n message1 \n", message1)
    # msg_lst.append(message1)

    # message2 = info_str[random_list[1]] + " " + ". " + rel_str[random_list[1]] + "\n\n" + funeral_str[random_list[1]]
    # # print("\n message2 \n", message2)
    # msg_lst.append(message2)

    # message3 = info_str[random_list[2]] + " " + ". " + rel_str[random_list[2]] + "\n\n" + funeral_str[random_list[2]]
    # # print("\n message3 \n", message3)
    # msg_lst.append(message3)

    # message4 = info_str[random_list[3]] + " " + ". " + rel_str[random_list[3]] + "\n\n" + funeral_str[random_list[3]]
    # # print("\n message4 \n", message4)
    # msg_lst.append(message4)

    single_features = {}
    single_features.update(personal_info_features)
    single_features.update(relations_features)
    single_features.update(funeral_features)

    # print("\nBasic \n")

    msg_lst = single_component(single_features)
    # print("\n message1 \n", single_str[0])
    # print("\n message2 \n", single_str[1])
    # print("\n message3 \n", single_str[2])
    # print("\n message4 \n", single_str[3])

    return msg_lst

# print(return_msgs()[0])