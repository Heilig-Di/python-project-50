import json

import yaml


def format_value(value):
    return str(value).lower() if isinstance(value, bool) else value


def generate_diff(file1_path, file2_path):
    if file1_path.endswith('.json') and file2_path.endswith('.json'):
        with open(file1_path, 'r') as file1:
            data1 = json.load(file1)

        with open(file2_path, 'r') as file2:
            data2 = json.load(file2)

    elif file1_path.endswith(('.yaml', '.yml')) and file2_path.endswith(('.yaml', '.yml')):
        with open(file1_path, 'r') as file1:
            data1 = yaml.safe_load(file1)

        with open(file2_path, 'r') as file2:
            data2 = yaml.safe_load(file2)
    else:
        raise ValueError('Unsupported format file. Use json or yaml.')

    all_keys = sorted(set(data1.keys()).union(data2.keys()))
    diff = []

    for key in all_keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if key in data1 and key not in data2:
            diff.append(f'  - {key}: {format_value(value1)}')
        elif key in data2 and key not in data1:
            diff.append(f'  + {key}: {format_value(value2)}')
        elif value1 != value2:
            diff.append(f'  - {key}: {format_value(value1)}')
            diff.append(f'  + {key}: {format_value(value2)}')
        else:
            diff.append(f'    {key}: {format_value(value1)}')

    return '{\n' + '\n'.join(diff) + '\n}'
