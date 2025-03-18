import json

import yaml


def load_data(file1_path, file2_path):
    if file1_path.endswith('.json') and file2_path.endswith('.json'):
        with open(file1_path, 'r') as file1:
            data1 = json.load(file1)

        with open(file2_path, 'r') as file2:
            data2 = json.load(file2)

    elif (file1_path.endswith(('.yaml', '.yml')) and
            file2_path.endswith(('.yaml', '.yml'))):
        with open(file1_path, 'r') as file1:
            data1 = yaml.safe_load(file1)

        with open(file2_path, 'r') as file2:
            data2 = yaml.safe_load(file2)
    else:
        raise ValueError('Unsupported format file. Use json or yaml.')

    return data1, data2
