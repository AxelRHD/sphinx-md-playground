# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Playground"
copyright = "2025, Axel Rudolf"
author = "Axel Rudolf"
release = "0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx.ext.duration",
    "sphinx_rtd_theme",
    "sphinx_rtd_dark_mode",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "de"


# -- MyST configuration ---------------------------------------------------

myst_enable_extensions = ["attrs_block", "attrs_inline", "colon_fence", "fieldlist"]

# -- RTD theme configuration ---------------------------------------------------

default_dark_mode = False

html_theme_options = {
    "navigation_depth": 2,
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_css_files = ["css/custom.css"]

html_favicon = "favicon.png"

html_static_path = ["_static"]

# html_style = "css/custom.css"
