import json


def format_value(value):
    return str(value).lower() if isinstance(value, bool) else value


def generate_diff(file1, file2):
    with open('gendiff/file1.json', 'r') as file1:
        data1 = json.load(file1)

    with open('gendiff/file2.json', 'r') as file2:
        data2 = json.load(file2)

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
