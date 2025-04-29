# Install required tools

```
pip install wheel twine
```
```
pip install setuptools
```

# Build source distribution (.tar.gz) and wheel (.whl)
```
python setup.py sdist bdist_wheel
```
```
twine upload --repository testpypi dist/*
```

# For Upload in PYPI.org
```
twine upload dist/* 
```

# Clean old build
```
rm -rf build/ dist/ n8py.egg-info/
```
