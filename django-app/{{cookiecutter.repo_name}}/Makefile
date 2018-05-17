BUILDDIR?=build
DJANGO_SETTINGS_MODULE?="demo.settings"


help:
	@echo "develop                 setup development environment"
	@echo "lint                    run pyflake/isort checks"
	@echo "clean                   clean dev environment"
	@echo "fullclean               totally remove any development/test artifacts"
	@echo "test                    run test suite"

develop:
	@pip install -U pip setuptools
	@pip install -e .[dev]
	@PYTHONPATH=$(PYTHONPATH):tests/demoproject django-admin.py migrate --settings ${DJANGO_SETTINGS_MODULE}

compile-requirements:
	@pip-compile src/requirements/install.in \
		--upgrade \
		--rebuild \
		--no-header \
		--no-emit-trusted-host \
		--no-index -o src/requirements/install.pip
	@pip-compile src/requirements/testing.in \
		src/requirements/install.pip \
		--upgrade \
		--rebuild \
		--no-header \
		--no-emit-trusted-host \
		--no-index -o src/requirements/testing.pip


sync-requirements:
	pip-sync src/requirements/develop.pip
	pip install -e .[dev]


test:
	py.test tests -v --create-db


lint:
	flake8 src/ tests
	isort -rc src/ --check-only
	check-manifest
	PYTHONPATH=$(PYTHONPATH):tests/demoproject django-admin.py check --settings ${DJANGO_SETTINGS_MODULE}


clean:
	rm -fr ${BUILDDIR} dist *.egg-info .coverage coverage.xml .eggs
	find src -name __pycache__ -o -name "*.py?" -o -name "*.orig" -prune | xargs rm -rf
	find tests -name __pycache__ -o -name "*.py?" -o -name "*.orig" -prune | xargs rm -rf
	find src/concurrency/locale -name django.mo | xargs rm -f

fullclean:
	rm -fr .tox .cache
	$(MAKE) clean


docs: .mkbuilddir
	mkdir -p ${BUILDDIR}/docs
	sphinx-build -aE docs/ ${BUILDDIR}/docs
ifdef BROWSE
	firefox ${BUILDDIR}/docs/index.html
endif
