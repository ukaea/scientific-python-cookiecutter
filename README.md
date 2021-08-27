# Scientific Python Cookiecutter

[![CI](https://github.com/ukaea/scientific-python-cookiecutter/actions/workflows/ci.yml/badge.svg)](https://github.com/ukaea/scientific-python-cookiecutter/actions/workflows/ci.yml) ![GitHub](https://img.shields.io/github/license/ukaea/scientific-python-cookiecutter) [![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CONTRIBUTING.md) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5243299.svg)](https://doi.org/10.5281/zenodo.5243299)


This repository contains a cookiecutter template for generating a scientific
Python project complete with CI testing and documentation.
See the usage section below for a quick start on how to obtain the template.

The repository also hosts an accompanying
[tutorial](https://ukaea.github.io/scientific-python-cookiecutter/) that
provides guided and detailed instructions about how to set up and use the
template and all of the features it contains. If you are new to cookiecutters
and Python packaging, then it is recommended to head there first.

The original version of these resources were produced by Brookhaven National
Lab, and this repository was forked from
[theirs](https://github.com/NSLS-II/scientific-python-cookiecutter) to add
support for GitLab and tailor it to UKAEA guidelines. Overall, it maintains a
fairly generic resource that should be valuable for any researcher, but there
are a few hyperlinks that point to internal UKAEA websites.

## Usage

On the command line, navigate to the directory where you would like to put your
project, and issue this command:

```bash
cookiecutter https://github.com/ukaea/scientific-python-cookiecutter
```

Follow the prompts to set up your project.


## Tutorial and Features

[The tutorial](https://ukaea.github.io/scientific-python-cookiecutter/) is
aimed at scientific researchers who have a novice level of experience with
Python. Typically, this means a researcher who knows the basic features of 
Python and has written a few scripts to perform analysis and visualisation but
has little or no awareness about how to package Python projects so they can be
shared. However, even if you consider yourself to be above novice level, this
tutorial could prove useful because it recommends a consistent set of tools and
practices that all successful Python projects should have.

You will be guided through setting up the following:

1. Version control for your project on GitHub or GitLab.
2. Creating a virtual environment for dependency management.
3. Documenting your code with Sphinx and publishing your documentation.
4. Tests for your code with pytest.
5. Continuous integration on Travis CI (for GitHub projects) or GitLab CI.
6. Publishing releases of your software and making it available on PyPI.
