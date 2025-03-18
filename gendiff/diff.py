from gendiff.path_data import load_data


def build_diff(data1, data2):
    all_keys = sorted(set(data1.keys()) | data2.keys())
    diff = []

    for key in all_keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if key in data1 and key not in data2:
            diff.append({'type': 'remove', 'key': key, 'value': value1})
        elif key in data2 and key not in data1:
            diff.append({'type': 'append', 'key': key, 'value': value2})
        elif value1 == value2:
            diff.append({'type': 'unchange', 'key': key, 'value': value1})
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff.append({
                'type': 'nested',
                'key': key,
                'children': build_diff(value1, value2)
                })
        else:
            diff.append({
                'type': 'change',
                'key': key,
                'old_value': value1,
                'new_value': value2
                })

    return diff
