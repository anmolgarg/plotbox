Distribution
'''''''''''''''''''''''''''''''''''''''

Versioning is handled manually in plotbox. We follow the rules of [Semantic Versioning](http://semver.org/).

**To update the version**
---------------------------------------

1. Edit plotbox/plotbox/version.py
2. Edit plotbox/docs/source/conf.py


**To upload to PyPI**
---------------------------------------

1. Check installation works
2. Create sdist and bdist_wheel distributions
3. Use twine to upload to pypi and skip any existing build

.. code:: sh

	sudo python setup.py install
	sudo python setup.py sdist bdist_wheel
	twine upload --skip-existing dist/*