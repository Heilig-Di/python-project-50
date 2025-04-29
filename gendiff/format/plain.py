def primitive_format(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str):
        return f"'{value}'"
    if value is None:
        return 'null'
    return str(value).lower() if isinstance(value, bool) else str(value)


def format_plain(diff, parent_key=''):
    lines = []

    for node in diff:
        node_type = node['type']
        key = node['key']
        full_path = f'{parent_key}.{key}' if parent_key else key

        if node_type == 'nested':
            lines.append(format_plain(node['children'], full_path))
        elif node_type == 'added':
            value = primitive_format(node['value'])
            lines.append(
                        f"Property '{full_path}' was added with value:"
                        f" {value}"
                        )
        elif node_type == 'removed':
            lines.append(f"Property '{full_path}' was removed")
        elif node_type == 'changed':
            old_val = primitive_format(node['old_value'])
            new_val = primitive_format(node['new_value'])
            lines.append(
                        f"Property '{full_path}' was updated."
                        f" From {old_val} to {new_val}"
            )

    return '\n'.join(line for line in lines if line)
