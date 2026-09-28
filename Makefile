ARG ?= config.json

install:
	pip install -r requirements.txt

run:
	python3 pac-man.py $(ARG)

debug:
	python3 -m pdb pac-man.py $(ARG)

clean:
	find . -name "__pycache__" -exec rm -rf {} +
	find . -name ".mypy_cache" -exec rm -rf {} +
	find . -name "pytest_cache" -exec rm -rf {} +

lint:
	flake8 pac-man.py src/
	mypy pac-man.py src/ --warn-return-any \
	--warn-unused-ignores \
	--ignore-missing-imports \
	--disallow-untyped-defs \
	--check-untyped-defs

lint-strict:
	flake8 src/ pac-man.py
	mypy src/ pac-man.py --strict
