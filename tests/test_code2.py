from src import code2

def test_diff():
    result = code2.diff(1,2)
    assert result == -1