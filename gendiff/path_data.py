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
