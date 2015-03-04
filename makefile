.PHONY: help bootstrap clean-pyc clean lint test coverage docs

help:
	@echo "bootstrap - bootstrap a local dev environment in vagrant"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean     - remove various artifacts"
	@echo "lint      - check style with flake8"
	@echo "test      - run tests"
	@echo "coverage  - check code coverage"
	@echo "docs      - generate Sphinx HTML documentation, including API docs"

bootstrap:
	vagrant up
	honcho run python manage.py migrate
	honcho run python -c "from django.db import DEFAULT_DB_ALIAS as db; from django.contrib.auth.models import User; User.objects.db_manager(db).create_superuser('admin', 'admin@example.com', 'admin')"


clean-pyc:
	find . -type d -name "__pycache__" -print0 | xargs -0 rm -rf
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

clean: clean-pyc
	rm -rf htmlcov/

lint:
	flake8 --max-line-length=120 --exclude=migrations --ignore=E128 revision

test:
	honcho run python manage.py test

coverage:
	honcho run coverage run --source='.' manage.py test
	coverage html
	open htmlcov/index.html

docs:
	@echo "Not implemented"
