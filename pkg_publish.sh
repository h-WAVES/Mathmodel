#!/usr/bin/env bash

rm -rf dist/* &&  python setup.py bdist_wheel --universal && python3 setup.py sdist && twine upload dist/*
