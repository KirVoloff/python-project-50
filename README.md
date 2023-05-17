### Hexlet tests and linter status:
[![Actions Status](https://github.com/KirVoloff/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/KirVoloff/python-project-50/actions)
<a href="https://codeclimate.com/github/KirVoloff/python-project-50/maintainability"><img src="https://api.codeclimate.com/v1/badges/33dd7be23993e377a447/maintainability" /></a>
[![Python CI](https://github.com/KirVoloff/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/KirVoloff/python-project-50/actions/workflows/pyci.yml)
<a href="https://codeclimate.com/github/KirVoloff/python-project-50/test_coverage"><img src="https://api.codeclimate.com/v1/badges/33dd7be23993e377a447/test_coverage" /></a>

# Getting started

### Description:

This is a utility that compares two json/yml files and shows the result in three different formats: stylish, plain or json

### Clone the repository using this command:

git clone [https://github.com/KirVoloff/python-project-50.git]

### Requirements:

* python >= 3.7
* Poetry >= 1.14

# Makefile

In order to use commands from Makefile, you need to have poetry installed

Firstly, check your current pip version and upgrade it, if needed:

**python -m pip --version**

**python -m pip install --upgrade pip**

After successful installation, you need to initiate new poetry package using this command:

**poetry init**

## Makefile commands:
**make install** install poetry packages

**make build** build poetry package and create dist directories

**make package-install** install built package to start using simple shell commands

**make publish** publish the project to PyPI after making a build


# Videos with examples of utility work

Example of work with flat types(json):
[![asciicast](https://asciinema.org/a/Ha3Zfzsrhax8Ztav3cyGHNlIU.svg)](https://asciinema.org/a/Ha3Zfzsrhax8Ztav3cyGHNlIU)

Example of work with flat types(yaml):
[![asciicast](https://asciinema.org/a/5os906oSKLRtTZfng79EwJnn9.svg)](https://asciinema.org/a/5os906oSKLRtTZfng79EwJnn9)

Example of work with nested types(json and yaml) - stylish:


Example of work with nested types(json and yaml) - plain:
[![asciicast](https://asciinema.org/a/VKbOQNQ8jDimUOyAGDlBVFJvZ.svg)](https://asciinema.org/a/VKbOQNQ8jDimUOyAGDlBVFJvZ)

Example of work with json formatting(flat):


Example of work with json formatting(nested):
[![asciicast](https://asciinema.org/a/LH51jN6qjlvM9aqn6VUxkoF4J.svg)](https://asciinema.org/a/LH51jN6qjlvM9aqn6VUxkoF4J)
