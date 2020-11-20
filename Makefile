default: install install-dev


h help:
	@egrep '(^\S)|(^$$)|\s+@echo' Makefile


install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt
