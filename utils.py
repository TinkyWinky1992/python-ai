import csv
import json


def creating_conversation_dict(main_dict, text, len):
    counter = len
    for line in text:
        dict = {}
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        if not clear_line:
            continue
        command, description = clear_line.split(':', +1)
        dict[command] = description
        main_dict[str(counter)] = dict
        counter += 1


def convert_dict_to_json(dialog):
    with open("C:/Users/yuval/PycharmProjects/chat-ai/DataSets/conversation_in_action.json", "w") as fp:
        json.dump(dialog, fp, indent=4, sort_keys=True)



def convert_to_json_from_txt(file_name):
    list_of_obj = {}
    counter = 1
    with open(file_name, encoding="utf8") as file:
        creating_conversation_dict(list_of_obj, file, 0)

    with open("C:/Users/yuval/PycharmProjects/chat-ai/DataSets/human.json", "w") as fp:
        json.dump(list_of_obj, fp, indent=4, sort_keys=True)


def load_custom_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        custom_data = json.load(file)
    return custom_data
