import pytest


def test_first():
    msg = 'hi'
    assert msg == "hi", "test failed due strings do not match"


@pytest.mark.smoke
def test_second():
    msg = 'hello'
    assert msg == "hell", "tset failed due to string do not match"