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
        self.work_dir = tempfile.mkdtemp()
        # copy local 'sample/' to temp-location
        self.src_dir = os.path.join(self.work_dir, 'sample')
        local_src = os.path.join(os.path.dirname(__file__), 'sample')
        shutil.copytree(local_src, self.src_dir)
        self.build_dir = os.path.join(self.src_dir, '_build')
        self.conf_dir = self.src_dir
        self.out_dir = os.path.join(self.build_dir, 'html')
        self.doctree_dir = os.path.join(self.build_dir, 'doctrees')
        os.makedirs(self.out_dir)
        os.makedirs(self.doctree_dir)

    def cleanup(self):
        if os.path.exists(self.work_dir):
            shutil.rmtree(self.work_dir)


@pytest.fixture(scope="function")
def sphinx_app(request):
    factory = SphinxAppFactory()
    request.addfinalizer(factory.cleanup)
    return factory


class TestAutodoc(object):

    def test_foo(self, sphinx_app):
        assert 1 == 1
        assert getattr(sphinx_app, 'app', 42) != 42
