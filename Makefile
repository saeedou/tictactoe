PRJ = tictactoe


.PHONY: test
test:
	pytest 

.PHONY: make cover
cover:
	pytest --cov=$(PRJ) .

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
