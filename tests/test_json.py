from gendiff.json_utils import generate_diff


def wait_result():
    with open('tests/test_data/example_result.txt', 'r') as result:
        return result.read().strip()


def test_gendiff():
    assert wait_result() == generate_diff('tests/test_data/example1.json',
                                'tests/test_data/example2.json')
