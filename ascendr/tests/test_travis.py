import pytest


@pytest.mark.fast
def test_travis_pass():
    """
    This is our initial test, to have travis-ci pass with flying colors!
    :return:
    """
    assert 1+1 == 2
