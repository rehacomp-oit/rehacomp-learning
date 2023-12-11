.PHONY = configure help lint test

# target: help - Display callable targets
help:
	@poetry version
	@echo -e "\n\nAvailable commands:"
	@grep -E "^# target:" makefile | awk -F ": " '{print $$2}'


# target: configure - generates the file with environment variables for the project
configure:
	@test ! -f .env && grep "^[^#]" ./config/envvars.template > ./.env


# target: lint - runs static checks for the source code
lint:
	@poetry run flake8 . && poetry run mypy .


check_env:
	@poetry run python manage.py check


# target: test - runs all auto tests for the project
test:
	@poetry run pytest
