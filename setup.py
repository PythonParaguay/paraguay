# -*- coding: utf-8 -*-

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="paraguay",
    version="0.0.1",
    author="Marcelo Elizeche Landó",
    author_email="melizeche@gmail.com",
    description="Python Paraguay community package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pythonparaguay/paraguay",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
    ),
    keywords='python paraguay community comunidad pythonpy this',
    project_urls={
        'Website': 'https://pythonpy.org',
        'Meetup': 'https://meetup.com/Python-Paraguay',
        'Twitter': 'https://twitter.com/PythonParaguay',
    },

)