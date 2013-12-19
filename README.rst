.. image:: https://travis-ci.org/badele/github-summary.png?branch=master
   :target: https://travis-ci.org/badele/github-summary


.. image:: https://coveralls.io/repos/badele/github-summary/badge.png
   :target: https://coveralls.io/r/badele/github-summary

.. disableimage:: https://pypip.in/v/github-summary/badge.png
   :target: https://crate.io/packages/github-summary/

.. disableimage:: https://pypip.in/d/github-summary/badge.png
   :target: https://crate.io/packages/github-summary/



About
=====

``github-summary`` is a python tool for generate github summary in multiple formats. It can generate a github summary in multiple formats (RST, TXT, HTML, etc ...)

Installing
==========

To install the latest release from `PyPI <http://pypi.python.org/pypi/github-summary>`_

.. code-block:: console

    $ pip install github-summary

To install the latest development version from `GitHub <https://github.com/badele/github-summary>`_

.. code-block:: console

    $ pip install git+git://github.com/badele/github-summary.git

Utilization
===========

Modify ``~/.github-summary.py`` or ``config.py``, for security reason, it is preferable modify ``~/.github-summary.py`` and execute command

.. code-block:: bash

	githubsummary -t rst/index-en.rst -j example_projects.json -s example.rst

Options
-------

You can configure options by projects, options is stored in JSON format. Here an exemple of JSON options

.. code-block:: JSON

   {
    "fabrecipes": {
        "hours": "89", 
        "description": "A overwriting description text for fabrecipe."
    }, 
    "JobCatcher": {
        "hours": "108", 
        "description": "Another overwriting description text for JobCatcher."
    }, 
    "gitcheck": {
        "hours": "15", 
        "url": "http://bruno.adele.im/projets/gitcheck", 
        "description": "Check multiple git repository in one pass."
    }, 
    "github-summary": {
        "coveralls": "True", 
        "description": "Python tool for generate github summary in multiple formats (TXT, RST, HTML, ...)", 
        "pypi": "True", 
        "pydownload": "True", 
        "hours": "30", 
        "travis": "True"
    }
   }


You can also use the externals tools for populate the JSON file. Ex: Emacs Org file to JSON file (projects contributed time)

.. code-block:: bash

   org2json -o project.org -s example_projects.json

You can see the generated `example <https://github.com/badele/github-summary/blob/master/example.rst>`_ in RST format

.. image:: http://bruno.adele.im/static/github-summary.png

You can also see the result directely in my personnal `website <http://bruno.adele.im>`_ 

