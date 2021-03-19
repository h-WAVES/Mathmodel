"""Setup information for the mathmodel API package."""
import os
import re
import codecs
from setuptools import setup, find_packages

current_path = os.path.abspath(os.path.dirname(__file__))


def read_file(*parts):
    with codecs.open(os.path.join(current_path, *parts), 'r', 'utf8') as reader:
        return reader.read()


def get_requirements(*parts):
    with codecs.open(os.path.join(current_path, *parts), 'r', 'utf8') as reader:
        return list(map(lambda x: x.strip(), reader.readlines()))


def find_version(*file_paths):
    version_file = read_file(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')

setup(
    name='mathmodel',
    packages=find_packages(),
    version=find_version('mathmodel', '__init__.py'),
    description='mathmodel REST API access modules',
    author='Waves',
    author_email='hhtnan@163.com',
    maintainer='Waves',
    maintainer_email='hhtnan@163.com',
    license='MIT',
    install_requires=get_requirements('requirements.txt'),
    url='https://github.com/h-WAVES/Mathmodel',
    keywords=['mathmodel', 'Model', 'alg', 'mathematical', 'mcm'],
    long_description=read_file('README.rst'),
    # long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Systems Administration",
        "Topic :: Internet",

    ]
)

