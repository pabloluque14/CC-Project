PIP= pip3
install: requirements.txt
	$(PIP) install -r requirements.txt
test: tests/tests.py
	coverage run tests/tests.py
	coverage report -m