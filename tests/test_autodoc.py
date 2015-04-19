# tests for waeup.sphinxext.autodoc
import pytest


@pytest.fixture(scope="function")
def sphinx_app(request):
    return None


class TestAutodoc(object):

    def test_foo(self):
        assert 1 == 1
