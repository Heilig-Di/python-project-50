from gendiff.diff import build_diff


def format_value(value, depth):
    if isinstance(value, dict):
        indent = ' ' * ((depth + 1) * 4)
        inner = [f'{indent}{k}: {format_value(v, depth + 1)}' for k, v in value.items()]
        return '{{\n{}\n{}}}'.format('\n'.join(inner), ' ' * (depth * 4))

    elif isinstance(value, bool):
        return str(value).lower()

    elif value is None:
        return 'null'

    elif isinstance(value, str) and not value:
        return ' '
    return str(value)


def formater_stylish(diff, depth=0):
    result = []
    indent = ' ' * (depth * 4)

    for node in diff:
        key = node['key']
        type_ = node['type']

        if type_ == 'nested':
            result.append(f'{indent}    {key}: {{')
            result.append(formater_stylish(node['children'], depth + 1))
            result.append(f'{indent}    }}')

        elif type_ == 'change':
            result.append(f'{indent}  - {key}: {format_value(node["old_value"], depth)}')
            result.append(f'{indent}  + {key}: {format_value(node["new_value"], depth)}')

        else:
            sign = {'append': '+', 'remove': '-', 'unchange': ' '}[type_]
            value = format_value(node['value'], depth + 1)
            result.append(f'{indent}  {sign} {key}: {value}')

    if depth == 0:
        return '{{\n{}\n}}'.format('\n'.join(result))
    return '\n'.join(result)
