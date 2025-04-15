from gendiff.diff import build_diff
from gendiff.path_data import read_file
from gendiff.stylish import formater_stylish


def generate_diff(file1_path, file2_path, format='stylish'):
    data1 = read_file(file1_path)
    data2 = read_file(file2_path)
    diff = build_diff(data1, data2)

    return formater_stylish(diff)
