# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# -- Project information -----------------------------------------------------

project = u"dses"
copyright = u"2024, Sneha S for ARTPARK"
author = u"Sneha S"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_nb",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# -- Options for Markdown rendering ------------------------------------------

# Add the data_standards directory to the source directory
source_dir = os.path.abspath(os.path.dirname(__file__))
data_standards_dir = os.path.join(source_dir, "data_standards")

# Include data_standards directory for Markdown rendering
myst_include_patterns = [data_standards_dir]

# Recursively include subdirectories of data_standards
myst_include_directories = [data_standards_dir]

# If you want to customize how files in data_standards are rendered,
# you can do so using the `myst_custom_renderers` setting.
