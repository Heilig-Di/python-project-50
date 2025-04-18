def format_dict(value, depth):
    indent = ' ' * (depth * 4 + 4)
    inner = [f'{indent}{k}: {format_value(v, depth)}' for k, v in value.items()]
    closing_indent = '    ' * depth
    return '{{\n{}\n{}}}'.format('\n'.join(inner), closing_indent)


def format_nested(node, depth):
    indent = '    ' * depth
    nested = formater_stylish(node["children"], depth + 1)
    return [
        f'{indent}    {node["key"]}: {{',
        nested,
        f'{indent}    }}'
    ]


def format_primitive(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return str(value)


def format_value(value, depth):
    if isinstance(value, dict):
        return format_dict(value, depth + 1)
    return format_primitive(value)


def format_change(node, depth):
    indent = '    ' * depth
    old_val = format_value(node["old_value"], depth)
    new_val = format_value(node["new_value"], depth)
    return [
        f'{indent}  - {node["key"]}: {old_val}',
        f'{indent}  + {node["key"]}: {new_val}'
    ]


def format_simple(node, depth):
    sign = {'added': '+', 'removed': '-', 'unchanged': ' '}[node['type']]
    indent = '    ' * depth
    value = format_value(node['value'], depth)
    return f"{indent}  {sign} {node['key']}: {value}"


def formater_stylish(diff, depth=0):
    lines = []

    for node in diff:
        node_type = node['type']

        if node_type == 'nested':
            processed = format_nested(node, depth)
        elif node_type == 'changed':
            processed = format_change(node, depth)
        else:
            processed = format_simple(node, depth)

        if isinstance(processed, list):
            lines.extend(processed)
        else:
            lines.append(processed)

    if depth == 0:
        return "{{\n{}\n}}".format("\n".join(lines))
    return "\n".join(lines)
