default: install install-dev


h help:
	@egrep '(^\S)|(^$$)|\s+@echo' Makefile


install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt


# Format with Black.
format:
	black .
format-check:
	# Exit with error status if fixes need to be applied.
	black . --diff --check

# Lint with PyLint.
pylint:
	# Exit on fatal error code.
	pylint pixeldays || pylint-exit $$?


# Lint with Flake8.
flake8:
	# Stop the build if there are Python syntax errors or undefined names.
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	# Exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide.
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

lint: pylint flake8

# Apply formatting and lint fixes.
fix: format lint
