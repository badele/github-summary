BASEDIR=$(CURDIR)
DISTDIR=$(BASEDIR)/dist
BUILDDIR=$(BASEDIR)/build
PACKAGE='githubsummary'

test: jsonfile pep8 coverage

prebuild:
	@echo 'Generating a example documentation'
	@./githubsummary/tools/org2json -o /LIVE/documents/project.org -s ./example_projects.json
	@./githubsummary/githubsummary.py -t rst/index-en.rst -j ./example_projects.json -s ./example.rst

build: 
	@echo 'Running build'
	@python setup.py build



deploy:
	@echo 'Upload to PyPi'
	@python setup.py sdist upload
	@echo 'Done'

dist:
	@echo 'Generating a distributable python package'
	@python setup.py sdist
	@echo 'Done'

install: 
	@echo 'Running install'
	@python setup.py install


jsonfile:
	@echo 'Generate JSON file from Org'
	@./githubsummary/tools/org2json -o /LIVE/documents/project.org -s ./example_projects.json

pep8:
	@pep8 $(PACKAGE) --config=pep8.rc
	@echo 'PEP8: OK'

coverage:
	@echo 'Running test suite with coverage'
	@coverage erase
	@coverage run --rcfile=coverage.rc tests.py
	@coverage html
	@coverage report --rcfile=coverage.rc

clean:
	@rm -fr $(DISTDIR)
	@rm -fr $(BUILDDIR)

.PHONY: help doc build test dist install clean 
