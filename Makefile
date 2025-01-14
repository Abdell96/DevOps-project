.PHONY: install test run clean docker-build docker-run docker-test

install:
	pip install -r requirements.txt

test:
	python -m pytest test.py -v

run:
	python app.py

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete

docker-build:
	docker build -t health-calculator:latest .

docker-run:
	docker run -p 5000:5000 health-calculator:latest

docker-test:
	docker run health-calculator:latest python -m pytest test.py -v









#init:
#	pip install -r requirements.txt

#run:
#	python app.py

#test:
#	python -m unittest test.py
