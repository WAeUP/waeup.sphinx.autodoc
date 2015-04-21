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
import sphinx


def setup(app):
    return {
        'version': sphinx.__display_version__,
        'parallel_read_safe': True
        }
