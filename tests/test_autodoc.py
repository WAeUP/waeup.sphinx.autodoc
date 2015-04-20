# tests for waeup.sphinxext.autodoc
import os
import pytest
import tempfile
import shutil
from sphinx.application import Sphinx


class SphinxAppFactory(object):
    """A factory providing `Sphinx` apps suitable for testing.
    """
    app = None

    def __init__(self):
        self.root_dir = tempfile.mkdtemp()
        pass

    def cleanup(self):
        if os.path.exists(self.root_dir):
            shutil.rmtree(self.root_dir)


@pytest.fixture(scope="function")
def sphinx_app(request):
    factory = SphinxAppFactory()
    request.addfinalizer(factory.cleanup)
    return factory


class TestAutodoc(object):

    def test_foo(self, sphinx_app):
        assert 1 == 1
        assert getattr(sphinx_app, 'app', 42) != 42
