.PHONY: test
test:
	pytest

.PHONY: cover
cover:
	pytest --cov tictactoe_core/ tests/


.PHONY: lint
lint:
	pylama

.PHONY: env
env:
	pip install -r requirements.txt
	pip install -e .

.PHONY: venv
venv:
	python3 -m venv .venv
