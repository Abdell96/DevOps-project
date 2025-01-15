.PHONY: help init install build rn test test-api clean docker-build docker-run docker-test

# Display help information about the Makefile targets
help:
	@echo "Available commands:"
	@echo "  make help         Display this help message"
	@echo "  make init         Set up the environment (create virtualenv and install dependencies)"
	@echo "  make install      Install dependencies from requirements.txt"
	@echo "  make build        Build the application (e.g., Docker image)"
	@echo "  make rn           Run the application locally"
	@echo "  make test         Run unit tests"
	@echo "  make test-api     Test API endpoints using curl"
	@echo "  make clean        Remove temporary and compiled files"
	@echo "  make docker-build Build the Docker image for the app"
	@echo "  make docker-run   Run the app in a Docker container"
	@echo "  make docker-test  Run tests inside a Docker container"

# Initialize the environment
init:
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

# Install dependencies
install:
	pip install -r requirements.txt

# Build (alias for Docker build)
build: docker-build

# Run the application locally
rn:
	python app.py

# Run unit tests
test:
	python -m pytest test.py -v

# Run API tests using curl
test-api:
	@echo "Starting the application..."
	@(python app.py > /dev/null 2>&1 & echo $$! > .flask.pid) & sleep 2
	@echo "Testing BMI endpoint..."
	@curl -X POST http://localhost:5000/bmi \
		-H "Content-Type: application/json" \
		-d '{"height": 1.75, "weight": 70}'
	@echo "\nTesting BMR endpoint..."
	@curl -X POST http://localhost:5000/bmr \
		-H "Content-Type: application/json" \
		-d '{"height": 175, "weight": 70, "age": 30, "gender": "male"}'
	@echo "\nStopping the application..."
	@if [ -f .flask.pid ]; then \
		kill `cat .flask.pid` 2>/dev/null || true; \
		rm .flask.pid; \
	fi
	@exit 0

# Clean up temporary and compiled files
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete

# Build the Docker image
docker-build:
	docker build -t health-calculator:latest .

# Run the app in a Docker container
docker-run:
	docker run -p 5000:5000 health-calculator:latest

# Run tests inside a Docker container
docker-test:
	docker run health-calculator:latest python -m pytest test.py -v




















#.PHONY: install test run clean docker-build docker-run docker-test

#install:
#	pip install -r requirements.txt

#test:
#	python -m pytest test.py -v

#run:
#	python app.py

#clean:
#	find . -type f -name "*.pyc" -delete
#	find . -type d -name "__pycache__" -delete

#docker-build:
#	docker build -t health-calculator:latest .

#docker-run:
#	docker run -p 5000:5000 health-calculator:latest

#docker-test:
#	docker run health-calculator:latest python -m pytest test.py -v









#init:
#	pip install -r requirements.txt

#run:
#	python app.py

#test:
#	python -m unittest test.py
