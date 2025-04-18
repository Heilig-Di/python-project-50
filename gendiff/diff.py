def build_diff(data1, data2):
    diff = []
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    for key in all_keys:
        value1 = data1.get(key)
        value2 = data2.get(key)
        if key not in data2:
            diff.append({
                "type": "removed",
                "key": key,
                "value": value1
            })
        elif key not in data1:
            diff.append({
                "type": "added",
                "key": key,
                "value": value2
            })
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff.append({
                "type": "nested",
                "key": key,
                "children": build_diff(value1, value2)
            })
        elif value1 != value2:
            diff.append({
                "type": "changed",
                "key": key,
                "old_value": value1,
                "new_value": value2
            })
        else:
            diff.append({
                "type": "unchanged",
                "key": key,
                "value": value1
            })
    return diff
