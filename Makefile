
# Install
install:
	@echo "Creating virtual environment and installing dependencies..."
	python3 -m venv .venv
	pip install -r requirements.txt

format:
	@echo "Formatting code with black..."
	black src tests
	@echo "Formatting code with isort..."
	isort src tests

lint:
	@echo "Running linters..."
	pylint src tests

test:
	@echo "Running tests..."
	PYTHONPATH=. pytest tests

checks: format lint
	@echo "Running all checks..."
	@echo "All checks passed!"