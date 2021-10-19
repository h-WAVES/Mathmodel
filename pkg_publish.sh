#!/usr/bin/env bash

rm -rf dist/* &&  python setup.py bdist_wheel --universal && python setup.py sdist && twine upload dist/*
#rm -rf dist/* &&  python setup.py bdist_wheel --universal && python setup.py sdist && twine upload dist/*
