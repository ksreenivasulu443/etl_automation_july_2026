import pytest

@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.prodrelease
@pytest.mark.sanity
def hdfc_one():
    assert True