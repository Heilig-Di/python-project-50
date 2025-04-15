def format_dict(value, depth):
    indent = ' ' * ((depth + 1) * 4)
    inner = [f'{indent}{k}: {format_value(v, depth + 1)}'
             for k, v in value.items()]
    closing_indent = ' ' * (depth * 4)
    return '{{\n{}\n{}}}'.format('\n'.join(inner), closing_indent)


def format_nested(node, depth):
    indent = ' ' * (depth * 4)
    nested_content = formater_stylish(node["children"], depth + 1)
    return [
        f'{indent}    {node["key"]}: {{',
        nested_content,
        f'{indent}    }}'
    ]


def format_primitive(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, str) and not value:
        return ' '
    return str(value)


def format_value(value, depth):
    if isinstance(value, dict):
        return format_dict(value, depth)
    return format_primitive(value)


def format_change(node, depth):
    indent = ' ' * (depth * 4)
    old_val = format_value(node["old_value"], depth)
    new_val = format_value(node["new_value"], depth)
    return [
        f'{indent}  - {node["key"]}: {old_val}',
        f'{indent}  + {node["key"]}: {new_val}'
    ]


def format_simple(node, depth):
    sign = {'append': '+', 'remove': '-', 'unchange': ' '}[node['type']]
    indent = ' ' * (depth * 4)
    value = format_value(node['value'], depth)
    return f"{indent}  {sign} {node['key']}: {value}"


def formater_stylish(diff, depth=0):
    result = []

    for node in diff:
        if node['type'] == 'nested':
            processed = format_nested(node, depth)
        elif node['type'] == 'change':
            processed = format_change(node, depth)
        else:
            processed = [format_simple(node, depth)]

        if isinstance(processed, list):
            result.extend(processed)
        else:
            result.append(processed)

    joined = '\n'.join([line for line in result if line is not None])

    if depth == 0:
        return f'{{\n{joined}\n}}'
    return joined
