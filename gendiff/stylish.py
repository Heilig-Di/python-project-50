 def format_dict(value, depth):
    indent = ' ' * ((depth + 1) * 4)
    inner = [f'{indent}{k}: {format_value(v, depth + 1)}' for k, v in value.items()]
    return '{{\n{}\n{}}}'.format('\n'.join(inner), ' ' * (depth * 4))


def format_primitiv(value):
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


def format_nested(node, depth):
    indent = ' ' * (depth * 4)
    return [
        f'{indent}    {node['key']}: {{',
        formater_stylish(node['children'], depth + 1),
        f'{indent}    }}'
    ]


def format_change(node, depth):
    indent = ' ' * (depth * 4)
    return [
            f'{indent}  - {node["key"]}: {format_value(node["old_value"], depth)}',
            f'{indent}  + {node["key"]}: {format_value(node["new_value"], depth)}'
    ]


def format_simple(node, depth):
    sign = {'append': '+', 'remove': '-', 'unchange': ' '}
    indent = ' ' * (depth * 4)
    return f"{indent}  {sign} {node['key']}: {format_value(node['value'], depth)}"


def formater_stylish(diff, depth=0):
    result = []
    for node in diff:
        handler = {
            'nested': format_nested,
            'change': format_change
        }.get(node['type'], lambda n, d: [format_simple(n, d)])
        
        result.extend(handler(node, depth))
    
    joined_result = '\n'.join(result)
    return f'{{\n{joined_result}\n}}' if depth == 0 else joined_result
