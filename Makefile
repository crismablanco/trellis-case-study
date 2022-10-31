.PHONY: runserver migrate shell createsuperuser makemigrations pylint black

TAG="\n\n\033[0;32m\#\#\# "
END=" \#\#\# \033[0m\n"

HOST=localhost
PORT=8000
PYTHONPATH=api
DJANGO_SETTINGS=api.settings.dev
PYTEST_XDIST_NODE_COUNT=2

django-command = poetry run django-admin $(1) $(2) --settings $(DJANGO_SETTINGS) --pythonpath $(PYTHONPATH)


runserver:
	@echo $(TAG)Running Server $(END)
	$(call django-command, runserver, $(HOST):$(PORT))

migrate:
	@echo $(TAG)Running Migrate $(END)
	$(call django-command, migrate)

shell:
	@echo $(TAG)Running Shell $(END)
	$(call django-command, shell)

test:
	@echo $(TAG)Running Tests $(END)
	poetry run pytest --cov api -n $(PYTEST_XDIST_NODE_COUNT)

black:
	poetry run black . --check

pylint:
	poetry run pylint --rcfile=.pylintrc api/*

pytest:
	poetry run pytest --cov-report term-missing --cov-config=.coveragerc --cov=api/ --cov-fail-under=90 api

build : black pylint pytest