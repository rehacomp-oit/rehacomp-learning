.PHONY = setup configure help lint run-dev test

# target: help - Display callable targets
help:
	@poetry version
	@echo -e "\n\nAvailable commands:"
	@grep -E "^# target:" ./makefile | awk -F ": " '{print $$2}'

# target: setup - sets up the necessary dependencies for the project, including the development environment
setup:
	@poetry install --no-root

# target: configure - generates the file with environment variables for the project
configure:
	@grep "^[^#]" ./config/envvars.template > ./.env


# target: lint - runs static checks for the source code
lint:
	@poetry run flake8 . && poetry run mypy server tests manage.py


# target: check-env - runs checks for the project's settings 
check-env:
	@poetry run python manage.py check


# target: test - runs all auto tests for the project
test: check-env
	@poetry run pytest


# target: shell - runs interactive python shell with prepaired django settings for the project
shell:
	@poetry run python manage.py shell


# target: run-dev - runs django web server for development on port 8000
run-dev:
	@poetry run python manage.py runserver
