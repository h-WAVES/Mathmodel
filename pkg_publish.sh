#!/usr/bin/env bash
rm -rf dist/* && python3 setup.py sdist && twine upload dist/*
#rm -rf dist/* && python3 setup.py sdist && python setup.py bdist_wheel --universal && twine upload dist/*
