# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Determined AI MyST Sphinx Test'
copyright = '2023, Determined AI'
author = 'tara-det-ai'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
#    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

#import better
#html_theme = 'better'
#html_theme_path = [better.better_theme_path]

# -- Options for EPUB output
epub_show_urls = 'footnote'

