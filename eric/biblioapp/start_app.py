
#Standard import
import sys

#Library import
from PyQt5.QtWidgets import  QApplication
from PyQt5.QtCore import QTranslator, QLocale


#Local import
from main_window_biblio import MainWindowBiblio

app = QApplication(sys.argv)
enlangueNative = len(sys.argv)==1

if enlangueNative:
	locale = QLocale()
else:
	languePays = sys.argv[1]

translators = []
for prefixeQm in ("biblioapp.", "qt_", "qtbase_"):
	translator = QTranslator()
	translators.append(translator)
	if enlangueNative:
		translator.load(locale, prefixeQm)
	else:
		translator.load(prefixeQm+languePays)
	app.installTranslator(translator)

mainWindowBiblio = MainWindowBiblio()
mainWindowBiblio.show()
rc = app.exec_()
sys.exit(rc)
