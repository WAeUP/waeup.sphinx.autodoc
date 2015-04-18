# -*- coding: utf-8 -*-
import sys, os

sys.path.append(os.path.abspath('.'))

extensions = ['sphinx.ext.autodoc', 'waeup.sphinx.autodoc']

master_doc = 'contents'
source_suffix = ['.txt', '.add', '.foo']
source_parsers = {'.foo': 'parsermod.Parser'}

project = 'WAeUP Sphinx Extensions <Tests>'
copyright = '2015, WAeUP Germany'
version = '0.1'
release = '0.1.alpha1'
keep_warnings = True
pygments_style = 'sphinx'
show_authors = True
numfig = True
