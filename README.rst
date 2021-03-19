**mathmodel**
==============

.. image:: https://img.shields.io/pypi/v/mathmodel
   :target: https://pypi.org/project/mathmodel/

.. image:: https://img.shields.io/github/downloads/h-WAVES/Mathmodel/total
   :target: https://img.shields.io/github/downloads/h-WAVES/Mathmodel/total

.. image:: https://img.shields.io/github/license/h-WAVES/Mathmodel
   :target: https://img.shields.io/github/license/h-WAVES/Mathmodel
   :alt: license

.. image:: https://img.shields.io/badge/keras-tensorflow-blue.svg
    :target: https://img.shields.io/badge/keras-tensorflow-blue.svg
    :alt: keras-tensorflow

.. image:: https://img.shields.io/badge/keras-tf.keras-blue.svg
   :target: https://img.shields.io/badge/keras-tf.keras-blue.svg
   :alt: keras-tf.keras



Describe
------------
**[**
`中文  <https://github.com/h-WAVES/Mathmodel/blob/main/README.rst>`_
|
`English <https://github.com/h-WAVES/Mathmodel/blob/main/README-zh-CN.md>`_
**]**


mathmodel is a set of modules that we use to manage aspects of our mathmodel
infrastructure.


Installation
------------

**[**
`Down Package <https://pypi.org/project/mathmodel/>`_
**|**
`Github Homepage <https://github.com/h-WAVES/Mathmodel>`_
**]**


**Using pip**:

Install this through pip::

    pip install mathmodel

**From source**:

Download the source code by cloning the repository or by pressing [`Download ZIP <https://github.com/h-WAVES/Mathmodel/archive/main.zip>`_
] on this page.
Install by navigating to the proper directory and running::

    python setup.py install

Usage
-----------
Python version 3.x，Get data(type ``pandas``)  quickly ::

    from mathmodelimport dataset
    data=dataset.load_boston()




Contributing
------------
1. Fork the repository on GitHub.
2. Run the mathmodel with **python** to confirm they all pass on your system.
   If the running fail, **then try and find out why this is happening. If you aren't
   able to do this yourself, then don't hesitate to either create an issue on
   GitHub**, contact me on Discord or send an email to [`hhtnan@163.com <mailto:hhtnan@163.com>`_]
3. Either create your feature and then write tests for it, or do this the other
   way around.
4. Run all mathmodel again with with ``python`` to confirm that everything
   still passes, including your newly added test(s).
5. Create a pull request for the main repository's ``master`` branch