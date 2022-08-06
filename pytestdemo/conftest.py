import pytest


@pytest.fixture
def setup(scope="class"):
    print('i will be executing first')
    yield
    print("i will execute last")

@pytest.fixture()
def dataload(scope="class"):
    print("user profile data is created")
    return ["rahul","vishnu","ram"]