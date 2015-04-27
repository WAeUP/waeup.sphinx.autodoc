# tests for waeup.sphinxext.autodoc
import grok
import os
import py.path
import pytest
import tempfile
from sphinx.application import Sphinx
from sphinx_testing import with_app, TestApp
from waeup.sphinx.autodoc import is_indexes_object, autodoc_skip_member


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
        self.work_dir.remove(rec=1)
        return


@pytest.fixture(scope="session")
def sphinx_app(request):
    tmpdir = py.path.local(tempfile.mkdtemp())
    factory = SphinxAppFactory(tmpdir)
    factory.build()
    request.addfinalizer(factory.cleanup)
    return factory


@pytest.fixture(scope="session")
def static_sphinx(request):
    """A fixture that provides a static sphinx build.

    'static' means: the HTML docs are built once and results can be
    retrieved during test session.

    After test session all generated stuff (files etc.) is removed.
    """
    exc = None
    app = TestApp(buildername='html', srcdir=SAMPLE_SPHINX_SRC,
                  copy_srcdir_to_tmpdir=True)
    try:
        app.build()
    except Exception as _exc:
        exc = _exc
    if app:
        if exc:
            request.addfinalizer(app.cleanup, error=exc)
        else:
            request.addfinalizer(app.cleanup)
    return app


class SampleCatalogClass(grok.Indexes):
    pass


class TestAutodoc(object):

    def test_is_indexes_object(self):
        # we can tell whether something is an instance of grok.Indexes
        assert is_indexes_object(object()) is False
        assert is_indexes_object(SampleCatalogClass) is True

    def test_autodoc_skip_member(self):
        # by default we return the passed in status
        assert autodoc_skip_member(
            None, 'module', 'MyObject', object(), True, {}) is True
        assert autodoc_skip_member(
            None, 'module', 'MyObject', object(), False, {}) is False

    def test_autodoc_skip_member_allows_grok_indexes(self):
        # we do not skip grok.Indexes
        assert autodoc_skip_member(
            None, 'mod', 'MyName', SampleCatalogClass, True, {}) is False
        assert autodoc_skip_member(
            None, 'mod', 'MyName', SampleCatalogClass, False, {}) is False

    @with_app(buildername='html', srcdir=SAMPLE_SPHINX_SRC,
              copy_srcdir_to_tmpdir=True)
    def test_regular_class_is_documented(self, app, status, warning):
        app.build()
        html = (app.outdir / 'contents.html').read_text()
        assert 'SampleApp_docstring' in html

    @with_app(buildername='html', srcdir=SAMPLE_SPHINX_SRC,
              copy_srcdir_to_tmpdir=True)
    def test_indexes_are_documented(self, app, status, warning):
        app.build()
        html = (app.outdir / 'contents.html').read_text()
        assert 'SampleAppCatalog' in html

    def test_indexes_docstrins_are_shown(self, static_sphinx):
        html = (static_sphinx.outdir / 'contents.html').read_text()
        assert 'SampleAppCatalog_docstring' in html
