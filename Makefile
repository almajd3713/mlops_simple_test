
# Install
install:
	@echo "Creating virtual environment and installing dependencies..."
	python3 -m venv .venv
	pip install -r requirements.txt

format:
	@echo "Formatting code with black..."
	black src tests

lint:
	@echo "Running linters..."
	flake8 src tests

check: format lint
	@echo "All checks passed!"