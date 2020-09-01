# Instalar las dependencias del proyecto
install: requirements.txt
	#crea entorno vitual
	pipenv install --three
	#Instala versiones de coverage y codecov necesarias
	pipenv run	pip3 install -r requirements.txt
# Ejecutar los tests
test: 
	# Este comando ejecuta tanto los tests unitarios y de integración como los tests de cobertura
	pipenv run coverage run tests/test_datamanager.py
	pipenv run coverage run tests/test_shopmanager.py
	# Mostrar el resultado de los tests de cobertura
	pipenv run coverage report -m
	# pasamos los resultados a codecov
	pipenv run codecov
