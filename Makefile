.PHONY: all test
PYTHON ?= python3
all:
	$(PYTHON) run_all.py
test:
	$(PYTHON) -m pytest -q
