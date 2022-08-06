import pytest


def test_program():
    print('myprogram')


@pytest.mark.skip
@pytest.mark.smoke
def test_dem():
    print('don')

