import pytest

from gendiff.gendiff_compare import generate_diff


@pytest.fixture
def expected_result():
    return """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""


@pytest.mark.parametrize("file1, file2", [
    ('tests/test_data/example1.json', 'tests/test_data/example2.json'),
    ('tests/test_data/example1.yaml', 'tests/test_data/example2.yaml'),
])
def test_gendiff_plain(file1, file2, expected_result):
    assert generate_diff(file1, file2, 'plain') == expected_result
