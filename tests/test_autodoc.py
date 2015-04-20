# tests for waeup.sphinxext.autodoc
import os
import py.path
import pytest
from sphinx.application import Sphinx

LOCAL_TEST_DIR = py.path.local(os.path.dirname(__file__) or '.')
SAMPLE_SPHINX_SRC = LOCAL_TEST_DIR / "sample"


class SphinxAppFactory(object):
    """A factory providing `Sphinx` apps suitable for testing.

    Expects a `py.path` path as temporary dir.

    A `Sphinx` application instance is available as `app`.
    """
    app = None

    def __init__(self, work_dir):
        self.work_dir = work_dir
        self.src_dir = self.work_dir / 'sample'
        SAMPLE_SPHINX_SRC.copy(self.src_dir)
        self.build_dir = self.src_dir.mkdir('_build')
        self.conf_dir = self.src_dir
        self.out_dir = self.build_dir.mkdir('html')
        self.doctree_dir = self.build_dir.mkdir('doctrees')
        self.app = Sphinx(
            self.src_dir.strpath, self.conf_dir.strpath,
            self.out_dir.strpath, self.doctree_dir.strpath,
            'html', freshenv=True)

    def build(self):
        """Build the sample HTML docs.
        """
        return self.app.build(force_all=True)

    def cleanup(self):
        return


@pytest.fixture(scope="function")
def sphinx_app(request, tmpdir):
    factory = SphinxAppFactory(tmpdir)
    request.addfinalizer(factory.cleanup)
    return factory


class TestAutodoc(object):

    def test_regular_class_is_documented(self, sphinx_app):
        sphinx_app.build()
        contents_html = sphinx_app.out_dir.join('contents.html')
        assert contents_html.check()
        with contents_html.open('r') as fd:
            contents = fd.read()
        assert 'SampleApp_docstring' in contents
