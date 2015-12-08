Distribution
'''''''''''''''''''''''''''''''''''''''

Versioning is handled manually in plotbox. We follow the rules of `semantic versioning <http://semver.org/>`_.

**To update the version**
---------------------------------------

1. Edit plotbox/plotbox/version.py


**To upload to PyPI**
---------------------------------------

1. Run setup
2. Create sdist and bdist_wheel distributions
3. Use twine to upload to pypi and skip any existing build
Note: You must update version before uploading to pypi

.. code:: sh

	sudo python setup.py install
	sudo python setup.py sdist bdist_wheel
	twine upload --skip-existing dist/*


**To build new documentation**
---------------------------------------

1. Run setup
2. Cd docs/ and run makehtml to build modules rst files
3. Commit and push to github for readthedocs to update

.. code:: sh

	sudo python setup.py install
	cd docs
	sudo python makehtml.py
	git commit -a -m 'updated docs'
	git push