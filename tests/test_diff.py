import pytest

from gendiff.compare_data import generate_diff


def wait_result():
    with open('tests/test_data/example_result.txt', 'r') as result:
        return result.read().strip()


@pytest.mark.parametrize("file1, file2", [
    ('tests/test_data/example1.json', 'tests/test_data/example2.json'),
    ('tests/test_data/example1.yaml', 'tests/test_data/example2.yaml'),
])
def test_gendiff(file1, file2):
    assert wait_result() == generate_diff(file1, file2)
