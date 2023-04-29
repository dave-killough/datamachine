
https://packaging.python.org/tutorials/packaging-projects/

To build the distribution: 

python -m build

Submit to pypi: 

python -m twine upload --repository testpypi dist/*
