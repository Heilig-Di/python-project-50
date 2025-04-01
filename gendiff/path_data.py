import json
import os

import yaml


def read_file(file_path):
    extension = os.path.splitext(file_path)
    with open(file_path, 'r') as file:
        if extension in ('json',):
            return json.load(file)
        if extension in ('yaml', 'yml'):
            return yaml.safe_load(file)
        raise ValueError(f'Unsupported file format: {extension}')


def load_data(file1_path, file2_path):
    ext1 = read_file(file1_path)
    ext2 = read_file(file2_path)

    if ext1 != ext2:
        raise ValueError('Files must have the same format')

    data1 = read_file(file1_path, ext1)
    data2 = read_file(file2_path, ext2)

    return data1, data2
