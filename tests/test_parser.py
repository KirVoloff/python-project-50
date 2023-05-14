from gendiff.parser import parse


def test_parse_module():
    json_file = parse(open('tests/fixtures/file1.json'), 'json')
    yaml_file = parse(open('tests/fixtures/file2.yml'), 'yaml')
    data_type = type(json_file)
    assert data_type == dict
    assert json_file == {'host': 'hexlet.io', 'timeout': 50,
                         'proxy': '123.234.53.22', 'follow': False}
    assert yaml_file == {'host': 'hexlet.io', 'timeout': 20,
                        'verbose': True}
