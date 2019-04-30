init:
	pip install -r requirements.txt

test:
	nosetests tests/*

test_verbose:
	nosetests --nocapture tests/*
