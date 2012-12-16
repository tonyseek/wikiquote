all: venv

#
# virtualenv
#

venv:
	virtualenv --use-distribute -p python2.7 venv
	echo "wikiquote" > venv/__name__

drop_venv:
	rm -rf venv

rebuild_venv: drop_venv venv

#
# test and distribute
#

VENV = . venv/bin/activate; 

test:
	$(VENV) python setup.py test
