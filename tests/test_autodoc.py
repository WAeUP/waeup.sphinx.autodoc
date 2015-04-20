# tests for waeup.sphinxext.autodoc
import pytest
from sphinx.application import Sphinx


class SphinxAppFactory(object):
    """A factory providing `Sphinx` apps suitable for testing.
    """
    app = None

    def __init__(self):
        pass


@pytest.fixture(scope="function")
def sphinx_app(request):
    return SphinxAppFactory()


class TestAutodoc(object):

    def test_foo(self, sphinx_app):
        assert 1 == 1
        assert getattr(sphinx_app, 'app', 42) != 42
