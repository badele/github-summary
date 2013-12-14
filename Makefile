BASEDIR=$(CURDIR)
DISTDIR=$(BASEDIR)/dist
BUILDDIR=$(BASEDIR)/build

help:
	@echo 'Makefile for github-summary'
	@echo '                                                                     '
	@echo 'Usage:                                                               '
	@echo '   make doc              Generate sample & doc                       '
	@echo '   make dist             Generate a distributable package            '
	@echo '   make clean            Remove all temporary and generated artifacts'
	@echo '   make install          Install package                             '
	@echo '                                                                     '

doc:
	@echo 'Generating a example documentation'
	@./githubsummary/tools/org2json -o /LIVE/documents/project.org -s ./example_projects.json
	@./githubsummary/githubsummary.py -t rst/index-en.rst -j ./example_projects.json -s ./example.rst

build: 
	@echo 'Running build'
	@python setup.py build

test: 
	@echo 'Running test suite'
	@./githubsummary/tools/org2json -o /LIVE/documents/project.org -s ./example_projects.json
	@python setup.py test

dist:
	@echo 'Generating a distributable python package'
	@python setup.py sdist
	@echo 'Done'

install: 
	@echo 'Running install'
	@python setup.py install

clean:
	@rm -fr $(DISTDIR)
	@rm -fr $(BUILDDIR)

.PHONY: help doc build test dist install clean 
