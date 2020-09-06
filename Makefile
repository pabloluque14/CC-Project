# Instalar las dependencias del proyecto
install: requirements.txt
	#crea entorno vitual
	pipenv install --three
	#Instala versiones de coverage y codecov necesarias
	pipenv run pip3 install -r requirements.txt
# Ejecutar los tests
test: 
	# Estos comando ejecuta tanto los tests unitarios y de integración como los tests de cobertura
	pipenv run coverage run tests/test_datamanager.py
	# tests sobre el microservicio shop-manager
	pipenv run coverage run tests/test_shopmanager.py
	# tests sobre el microservicio transaction-manager
	pipenv run coverage run tests/test_transactionmanager.py
	# tests sobre el microservicio statistic-manager
	pipenv run coverage run tests/test_statisticmanager.py
	# Mostrar el resultado de los tests de cobertura
	pipenv run coverage report -m
	# pasamos los resultados a codecov
	pipenv run codecov
