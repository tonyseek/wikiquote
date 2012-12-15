all: venv

venv:
	virtualenv -p python2.7 venv
	echo "wikiquote" > venv/__name__
