from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys




if __name__ == '__main__':
	
	app = QApplication(sys.argv)
	view = QWebEngineView()
	view.show()
	view.setUrl(QUrl("https://www.linuxvdoice.com"))

	sys.exit(app.exec())