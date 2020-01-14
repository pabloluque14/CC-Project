# Instalar las dependencias del proyecto
install: requirements.txt
	#crea entorno vitual
	python3 -m venv venv
	#activa el entorno virtual
	. venv/bin/activate
	#Instala versiones de coverage y codecov necesarias
	pip3 install -r requirements.txt
# Ejecutar los tests
test: tests/tests.py
	#activa el entorno virtual
	. venv/bin/activate
	# Este comando ejecuta tanto los tests unitarios y de integración como los tests de cobertura
	coverage run tests/tests.py
	# Mostrar el resultado de los tests de cobertura
	coverage report -m
	# pasamos los resultados a codecov
	codecov
