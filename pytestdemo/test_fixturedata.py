import pytest


@pytest.mark.usefixtures("dataload")
class Testexan:
    def test_demo(self,dataload):
        print(dataload)

@pytest.fixture(params=["chrome","firefox","IE"])
def crossBrowser(request):
    return  request.param
