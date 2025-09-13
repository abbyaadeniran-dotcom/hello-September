import pytest

@pytest.mark.smoke
def test_add():
    assert 2 + 3 == 5

@pytest.mark.regression
def test_subtract():
    assert 5 - 2 == 3