from gendiff.diff import build_diff
from gendiff.format.json import format_json
from gendiff.format.plain import format_plain
from gendiff.format.stylish import formater_stylish
from gendiff.path_data import read_file


def generate_diff(file1_path, file2_path, format='stylish'):
    data1 = read_file(file1_path)
    data2 = read_file(file2_path)
    diff = build_diff(data1, data2)

    formatters = {
        'stylish': formater_stylish,
        'plain': format_plain,
	'json': format_json
    }

    return formatters[format](diff)
