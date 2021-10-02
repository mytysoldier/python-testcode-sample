from src import code

def test_calc():
    result1, result2 = code.calc(1,2)
    assert result1 == 3
    assert result2 == 1

def get_json_data_mock(id):
    return {'name': 'test'}

def test_get_user_names(monkeypatch):
    monkeypatch.setattr(
        code, 'get_json_data', get_json_data_mock)
    result = code.get_user_names(['001', '009'])

    assert list(result.keys()) == ['001', '009']
    assert list(result.values()) == ['test', 'test']

import pytest

def test_user_name_validation():
    with pytest.raises(ValueError) as e:
        code.user_name_validation(None)
    assert str(e.value) == '名前が設定されていません'