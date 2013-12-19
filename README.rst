.. image:: https://travis-ci.org/badele/github-summary.png?branch=master
   :target: https://travis-ci.org/badele/github-summary


.. image:: https://coveralls.io/repos/badele/github-summary/badge.png
   :target: https://coveralls.io/r/badele/github-summary

.. image:: https://pypip.in/v/github-summary/badge.png
   :target: https://crate.io/packages/github-summary/

.. image:: https://pypip.in/d/github-summary/badge.png
   :target: https://crate.io/packages/github-summary/



About
=====

``github-summary`` Python tool for generate github summary in multiple formats. It can generate a github summary in multiple formats (RST, TXT, HTML, etc ...)

Installing
==========

To install the latest release from `PyPI <http://pypi.python.org/pypi/github-summary>`_

.. code-block:: console

    $ pip install github-summary

To install the latest development version from `GitHub <https://github.com/badele/github-summary>`_

.. code-block:: console

    $ pip install git+git://github.com/badele/github-summary.git

Example
=======

Here is an example commands using ``github-summary``

.. code-block:: python

	githubsummary -t rst/index-en.rst -j example_projects.json -s example.rst

You can also use the tools, ex: Emacs Org file to JSON file (projects contributed time)

.. code-block:: python

   org2json -o project.org -s example_projects.json

You can see a `example <https://github.com/badele/github-summary/blob/master/example.rst>`_ result

.. image:: http://bruno.adele.im/static/github-summary.png

You can also see the result directely in my personnal `website <http://bruno.adele.im>`_ 

