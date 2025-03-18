from gendiff.diff import build_diff
from gendiff.path_data import load_data
from gendiff.stylish import formater_stylish


def generate_diff(file1_path, file2_path, format='stylish'):
    data1, data2 = load_data(file1_path, file2_path)
    diff = build_diff(data1, data2)

    if format == 'stylish':
        return formater_stylish(diff)
