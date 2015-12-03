import os
import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

# Utility function to read the README file used for the long_description
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

# Get current version from plotbox.version.py
exec(compile(open('plotbox/version.py').read(),
                  'plotbox/version.py', 'exec'))


config = {
    'name': 'plotbox',
    'version': __version__,
    'author': 'Anmol Garg',
    'author_email': 'agarg@teslamotors.com',
    'description': 'Plotting library with a common API for static and interactive visualization',
    'license': 'MIT',
    'keywords': 'plotting visualization interactive',
    'url': 'https://github.com/anmolgarg/plotbox',
    'packages': find_packages(),
    'long_description': read('README.txt'),
    'install_requires': [
        'matplotlib',
        'numpy',
        'pandas',
        'seaborn',
        'plotly',
    ], 
    'package_data': {'plotbox' : ['../README.md']},
    'dependency_links': [],
    'scripts': [],
}

print 'Installing PlotBox.'
print 'Installing dependencies.'
setup(**config)
