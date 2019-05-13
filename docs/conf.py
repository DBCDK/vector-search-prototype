# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import setuptools
sys.path.insert(0, os.path.abspath('../src')) # inserted by /home/shm/anaconda3/bin/project-starter


# -- Project information -----------------------------------------------------

project = 'vector-search'
copyright = '2019, shm'
author = 'shm'

# The short X.Y version
version = get_version(os.path.abspath(os.path.join(os.path.realpath(__file__), '../../setup.py'))) # inserted by /home/shm/anaconda3/bin/project-starter

# The full version, including alpha/beta/rc tags
release = get_version(os.path.abspath(os.path.join(os.path.realpath(__file__), '../../setup.py')), release=True) # inserted by /home/shm/anaconda3/bin/project-starter

########## Inserted by /home/shm/anaconda3/bin/project-starter ##########
class __MockSetup():
    def __init__(self, setup_dir, mock_setup):
        self.setup = setuptools.setup
        self.mock_setup = mock_setup
        self.setup_dir = setup_dir
        self.dir = os.getcwd()

    def __enter__(self):
        setuptools.setup = self.mock_setup
        os.chdir(self.setup_dir)

    def __exit__(self, type, value, traceback):
        setuptools.setup = self.setup
        os.chdir(self.dir)


class __SetupWrapper():
    def setup(self, **kwargs):
        self.kwargs = kwargs


def get_version(setup_path, release=True):
    sw = __SetupWrapper()
    with __MockSetup(os.path.dirname(setup_path), sw.setup):
        exec(open(setup_path).read())
    vsplit = sw.kwargs['version'].split('.')
    if release:
        return '.'.join(vsplit)
    return '.'.join(vsplit[:2])
#########################################################################

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}
