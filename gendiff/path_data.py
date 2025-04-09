import json
import os

import yaml


def read_file(file_path):
    _, extension = os.path.splitext(file_path)
    extension = extension.lower().lstrip('.')
    with open(file_path, 'r') as file:
        if extension in ('json'):
            return json.load(file)
        if extension in ('yaml', 'yml'):
            return yaml.safe_load(file)
        raise ValueError(f'Unsupported file format: {extension}')


def load_data(file1_path, file2_path):
    ext1 = os.path.splitext(file1_path)[1].lstrip('.').lower()
    ext2 = os.path.splitext(file2_path)[1].lstrip('.').lower()

    if ext1 != ext2:
        raise ValueError('Files must have the same format')

    data1 = read_file(file1_path)
    data2 = read_file(file2_path)

    return data1, data2
