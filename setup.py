import os
import sys
from setuptools import setup, find_packages

# Utility function to read the README file used for the long_description
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

# get version from plotbox/plotbox/_version.py
exec(open('plotbox/_version.py').read())

config = {
    'name': 'plotbox',
    'version': __version__,
    'author': 'Anmol Garg',
    'author_email': 'anmolgarg314@gmail.com',
    'description': 'Plotting library with a common API for static and interactive visualization',
    'license': 'MIT',
    'keywords': 'plotting visualization interactive',
    'url': 'https://github.com/anmolgarg/plotbox',
    'packages': find_packages(),
    'long_description': read('README.rst'),
    'install_requires': [
        'matplotlib',
        'numpy',
        'pandas',
        'seaborn',
        'plotly',
    ], 
    'package_data': {'plotbox' : ['../README.rst']},
    'classifiers': [
        'Development Status :: 2 - Pre-Alpha',
        'Topic :: Scientific/Engineering :: Visualization',
    ],
    'dependency_links': [],
    'scripts': []
}

setup(**config)
