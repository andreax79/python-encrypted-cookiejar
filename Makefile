SHELL=/bin/bash -e

help:
	@echo - make coverage
	@echo - make test
	@echo - make lint
	@echo - make release
	@echo - make clean

coverage:
	python3 -m coverage run --source=encrypted_cookiejar test.py && python3 -m coverage report -m

test:
	python3 setup.py test

lint:
	python3 setup.py flake8

release:
	python3 ./setup.py bdist_wheel
	cd docs; $(MAKE) html

clean:
	-rm -rf build dist
	-rm -rf *.egg-info
	-rm -rf docs/_build

