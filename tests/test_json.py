import json

import pytest

from gendiff.gendiff_compare import generate_diff


@pytest.fixture
def expected_json():
    with open('tests/test_data/example_json.json', 'r') as f:
        return json.load(f)


@pytest.mark.parametrize("file1, file2", [
    ('tests/test_data/example1.json', 'tests/test_data/example2.json'),
    ('tests/test_data/example1.yaml', 'tests/test_data/example2.yaml'),
])
def test_gendiff_json(file1, file2, expected_json):
    result = generate_diff(file1, file2, 'json')
    assert json.loads(result) == expected_json
