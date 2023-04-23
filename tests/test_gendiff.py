import json
import pytest

def test_compare_flat_json():
    # загружаем два плоских json-файла
    with open('tests/fixtures/file1.json') as f:
        file1_data = json.load(f)
    with open('tests/fixtures/file2.json') as f:
        file2_data = json.load(f)
    
    # сравниваем ключи в каждом файле
    assert sorted(file1_data.keys()) == sorted(file2_data.keys())
    
    # сравниваем значения для каждого ключа
    for key in file1_data:
        assert file1_data[key] == file2_data[key]



