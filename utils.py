import csv
import json


def load_custom_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        custom_data = json.load(file)
    return custom_data


def csv_to_json(csv_file_path, json_file_path):
    # Read CSV file and convert it to a list of dictionaries
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = list(csv_reader)

    # Write the data to a JSON file
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
