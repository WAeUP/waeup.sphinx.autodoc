# -*- coding: utf-8 -*-
#
#  waeup.sphinx.autodoc -- Zope compatible autodocs for Sphinx
#  Copyright (C) 2015  Uli Fouquet, WAeUP Germany
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""
    waeup.sphinx.autodoc
    ~~~~~~~~~~~~~~~~~~~~

    Automatically insert docstrings for functions, classes or whole
    modules into the doctree, thus avoiding duplication between
    docstrings and documentation for those who like elaborate
    docstrings.

    :copyright: Copyright 2015 by Uli Fouquet, WAeUP Germany.
    :license: GPL v3+, see LICENSE for details.
"""
import pkg_resources
from grokcore.catalog import IndexesClass
from sphinx.ext.autodoc import ClassDocumenter, ModuleLevelDocumenter
from sphinx.util.docstrings import prepare_docstring


__version__ = pkg_resources.get_distribution('waeup.sphinx.autodoc').version


def is_indexes_object(obj):
    """Tell, whether `obj` is derived from `grok.Indexes`.

    `grok.Indexes` is not a class but an instance of
    `grokcore.catalog.IndexesClass`.
    """
    return isinstance(obj, IndexesClass)


def autodoc_skip_member(app, what, name, obj, skip, options):
    """Do not skip `grok.Indexes` classes.

    These are normally skipped due to their strange structure (they
    are Instances one can use a class base;
    """
    if is_indexes_object(obj):
        return False
    return skip


class GrokIndexesDocumenter(ClassDocumenter):
    """
    Specialized Documenter subclass for grok.Indexes instances.
    """
    objtype = 'grokindexes'
    member_order = ClassDocumenter.member_order + 10

    @classmethod
    def can_document_member(cls, member, membername, isattr, parent):
        """We can document `grok.Indexes` classes.
        """
        return is_indexes_object(member)

    def check_module(self):
        """Check if `self.object` is really defined in the module given by
        `self.modname`.

        XXX: The base class check is not valid for grok.Indexes.
        """
        return True

    def add_content(self, more_content, no_docstring=False):
        """Add content.

        This override excludes some base class functionality which
        prevented doc strings to be displayed.
        """
        ModuleLevelDocumenter.add_content(self, more_content)
        return


def setup(app):
    app.connect('autodoc-skip-member', autodoc_skip_member)
    app.add_autodocumenter(GrokIndexesDocumenter)
    return {
        'version': __version__,
        'parallel_read_safe': True
        }
