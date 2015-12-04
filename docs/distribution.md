## Distribution

Versioning is handled manually in plotbox. We follow the rules of [Semantic Versioning](http://semver.org/).

### To update the version
1. Edit /plotbox/plotbox/version.py

### To upload to pypi
1. Check library installation works
2. Create distribution sdist and bdist_wheel
3. Use twine to upload to pypi (skip existing builds on pypi)

```sh
sudo python setup.py install
sudo python setup.py sdist bdist_wheel
twine upload --skip-existing dist/*
```