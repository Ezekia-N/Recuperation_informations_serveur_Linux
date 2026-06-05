all: ressources_rc.py ui_form.py
	python3 src/python/widget.py

ui_form.py: form.ui
	pyside6-uic form.ui -o src/python/ui_form.py

ressources_rc.py: ressource/ressources.qrc
	pyside6-rcc ressource/ressources.qrc -o src/python/ressources_rc.py
