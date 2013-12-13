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

You can see a `example <https://github.com/badele/github-summary/example.rst>`_ result or this picture

![github summary capture](http://bruno.adele.im/static/github-summary.png)
