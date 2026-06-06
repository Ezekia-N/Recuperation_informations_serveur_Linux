all: ressources_rc.py ui_form.py
	python3 src/python/widget.py

ui_form.py: form.ui
	pyside6-uic form.ui -o src/python/ui_form.py

ressources_rc.py: ressources/ressources.qrc
	pyside6-rcc ressources/ressources.qrc -o src/python/ressources_rc.py

deploier: src/python/widget.py
	pyinstaller --noconsole --onefile src/python/widget.py