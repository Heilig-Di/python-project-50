import json


def convert_diff_to_dict(diff):
    result = {}
    for node in diff:
        key = node['key']
        node_type = node['type']

        if node_type == 'nested':
            result[key] = {
                "operation": "nested",
                "children": convert_diff_to_dict(node['children'])
            }
        elif node_type == 'changed':
            result[key] = {
                "operation": "changed",
                "old": node['old_value'],
                "new": node['new_value']
            }
        else:
            operation_map = {
                'added': 'added',
                'removed': 'removed',
                'unchanged': 'unchanged'
            }
            value_key = 'new' if node_type == 'added' else 'old'
            result[key] = {
                "operation": operation_map[node_type],
                value_key: node['value']
            }
    return result


def format_json(diff):
    diff_dict = convert_diff_to_dict(diff)
    return json.dumps(diff_dict, indent=4)
