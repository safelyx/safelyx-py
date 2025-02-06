.PHONY: install
install:
	python -m venv .venv
	source .venv/bin/activate && python -m pip install -r requirements-dev.txt

.PHONY: format
format:
	source .venv/bin/activate && black .

.PHONY: test
test:
	source .venv/bin/activate && python -m pytest test.py

.PHONY: publish
publish:
	rm -fr ./dist
	source .venv/bin/activate && python -m build
	source .venv/bin/activate && python -m twine upload	dist/*
