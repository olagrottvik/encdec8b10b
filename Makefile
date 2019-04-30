.PHONY: init freeze test test_verbose build_dist upload

venv:
	python3 -m venv .env

init:
	pip install -r requirements.txt

freeze:
	pip freeze | grep -v "pkg-resources" > requirements.txt

test:
	nosetests tests/*

test_verbose:
	nosetests --nocapture tests/*

build_dist:
	rm -rf dist/*
	python3 setup.py sdist bdist_wheel

upload_test:
	python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

upload:
	python3 -m twine upload dist/*