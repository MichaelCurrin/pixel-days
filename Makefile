default: install install-dev


h help:
	@egrep '(^\S)|(^$$)|\s+@echo' Makefile


install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt


format:
	black .
format-check:
	black . --diff --check

pylint:
	pylint pixeldays || pylint-exit $$?


flake8:
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

lint: pylint flake8

fix: format lint
