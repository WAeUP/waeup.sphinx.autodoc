# -*- coding: utf-8 -*-
"""
    waeup.sphinx.autodoc
    ~~~~~~~~~~~~~~~~~~~~

    Automatically insert docstrings for functions, classes or whole modules into
    the doctree, thus avoiding duplication between docstrings and documentation
    for those who like elaborate docstrings.

    :copyright: Copyright 2015 by Uli Fouquet, WAeUP Germany.
    :license: GPL v3+, see LICENSE for details.
"""
import sphinx


def setup(app):
    return {
        'version': sphinx.__display_version__,
        'parallel_read_safe': True
        }
