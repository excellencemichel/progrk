# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gestion.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from donnees import Database as mydb
from qt3.gridlayout import Window as gridlayout_widows
from login import Ui_DialogLogin


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 600)
        MainWindow.setStyleSheet("#centralwidget{\n"
" background-color:qlineargradient(spread:pad, x1:0.936, y1:0.188, x2:0.091, y2:1, stop:0 rgba(191, 249, 92, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}\n"
"\n"
"#login_widget, #sigup_widget,  #profile_widget{\n"
" background-color: qlineargradient(spread:pad, x1:0.201273, y1:0.842, x2:0.671, y2:0.448864, stop:0 rgba(0, 229, 242, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"#username_label, #password_label{\n"
"/*\n"
"background-color:qlineargradient(spread:pad, x1:0.984, y1:0.046, x2:0.97855, y2:0.063, stop:0 rgba(249, 249, 249, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-color: rgb(0, 255, 0);\n"
"*/\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        log_wind = QtWidgets.QWidget(self.centralwidget)
        un_win = Ui_DialogLogin()
        un_win.setupUi(log_wind)
        self.login_widget = QtWidgets.QWidget(self.centralwidget)
        # self.login_widget.hide()
        self.login_widget.setGeometry(QtCore.QRect(12, 112, 521, 321))
        self.login_widget.setObjectName("login_widget")
        self.username_login_lineEdit = QtWidgets.QLineEdit(self.login_widget)
        self.username_login_lineEdit.setGeometry(QtCore.QRect(180, 64, 241, 31))
        self.username_login_lineEdit.setObjectName("username_login_lineEdit")
        self.password_login_lineEdit = QtWidgets.QLineEdit(self.login_widget)
        self.password_login_lineEdit.setGeometry(QtCore.QRect(180, 144, 241, 31))
        self.password_login_lineEdit.setObjectName("password_login_lineEdit")
        self.login_button = QtWidgets.QPushButton(self.login_widget)
        self.login_button.setGeometry(QtCore.QRect(110, 210, 89, 25))
        self.login_button.setObjectName("login_button")
        self.sigup_login_button = QtWidgets.QPushButton(self.login_widget)
        self.sigup_login_button.setGeometry(QtCore.QRect(290, 210, 89, 25))
        self.sigup_login_button.setObjectName("sigup_login_button")
        self.username_login_label = QtWidgets.QLabel(self.login_widget)
        self.username_login_label.setGeometry(QtCore.QRect(60, 70, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.username_login_label.setFont(font)
        self.username_login_label.setStyleSheet("border-color: rgb(0, 255, 0);")
        self.username_login_label.setObjectName("username_login_label")
        self.password_label = QtWidgets.QLabel(self.login_widget)
        self.password_label.setGeometry(QtCore.QRect(60, 150, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.or_login_label = QtWidgets.QLabel(self.login_widget)
        self.or_login_label.setGeometry(QtCore.QRect(220, 210, 31, 17))
        self.or_login_label.setObjectName("or_login_label")

        self.sigup_widget = QtWidgets.QWidget(self.centralwidget)
        # self.sigup_widget.hide()
        self.sigup_widget.setEnabled(True)
        self.sigup_widget.setGeometry(QtCore.QRect(573, 112, 621, 471))
        self.sigup_widget.setObjectName("sigup_widget")
        self.username_signup_label = QtWidgets.QLabel(self.sigup_widget)
        self.username_signup_label.setGeometry(QtCore.QRect(40, 196, 91, 17))
        self.username_signup_label.setObjectName("username_signup_label")
        self.prenom_signup_label = QtWidgets.QLabel(self.sigup_widget)
        self.prenom_signup_label.setGeometry(QtCore.QRect(40, 50, 91, 17))
        self.prenom_signup_label.setObjectName("prenom_signup_label")
        self.nom_signup_label = QtWidgets.QLabel(self.sigup_widget)
        self.nom_signup_label.setGeometry(QtCore.QRect(40, 120, 81, 17))
        self.nom_signup_label.setObjectName("nom_signup_label")
        self.password_signup_label = QtWidgets.QLabel(self.sigup_widget)
        self.password_signup_label.setGeometry(QtCore.QRect(40, 290, 91, 17))
        self.password_signup_label.setObjectName("password_signup_label")
        self.confirmation_pass_signup_label = QtWidgets.QLabel(self.sigup_widget)
        self.confirmation_pass_signup_label.setGeometry(QtCore.QRect(40, 360, 91, 17))
        self.confirmation_pass_signup_label.setObjectName("confirmation_pass_signup_label")
        self.prenom_sigunp_lineEdit = QtWidgets.QLineEdit(self.sigup_widget)
        self.prenom_sigunp_lineEdit.setGeometry(QtCore.QRect(170, 44, 301, 31))
        self.prenom_sigunp_lineEdit.setObjectName("prenom_sigunp_lineEdit")
        self.nom_signup_lineEdit = QtWidgets.QLineEdit(self.sigup_widget)
        self.nom_signup_lineEdit.setGeometry(QtCore.QRect(172, 110, 301, 31))
        self.nom_signup_lineEdit.setObjectName("nom_signup_lineEdit")
        self.username_signup_lineEdit = QtWidgets.QLineEdit(self.sigup_widget)
        self.username_signup_lineEdit.setGeometry(QtCore.QRect(170, 190, 301, 31))
        self.username_signup_lineEdit.setObjectName("username_signup_lineEdit")
        self.password_signup_lineEdit = QtWidgets.QLineEdit(self.sigup_widget)
        self.password_signup_lineEdit.setGeometry(QtCore.QRect(170, 280, 301, 31))
        self.password_signup_lineEdit.setObjectName("password_signup_lineEdit")
        self.confirmation_pass_signup_lineEdit = QtWidgets.QLineEdit(self.sigup_widget)
        self.confirmation_pass_signup_lineEdit.setGeometry(QtCore.QRect(170, 354, 301, 31))
        self.confirmation_pass_signup_lineEdit.setObjectName("confirmation_pass_signup_lineEdit")
        self.signup_signup_button = QtWidgets.QPushButton(self.sigup_widget)
        self.signup_signup_button.setGeometry(QtCore.QRect(240, 410, 161, 25))
        self.signup_signup_button.setObjectName("signup_signup_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.barre_menu = QtWidgets.QMenuBar(MainWindow)
        self.barre_menu.setGeometry(QtCore.QRect(0, 7, 1400, 22))
        self.barre_menu.setObjectName("barre_menu")
        self.menuMenu = QtWidgets.QMenu(self.barre_menu)
        self.help_menu = QtWidgets.QMenu(self.barre_menu)
        self.filemenu = QtWidgets.QMenu(self.barre_menu)
        self.bureau_menu = QtWidgets.QMenu(self.barre_menu)
        # self.exit_menu = QtWidgets.QMenu(self.menuMenu)
        self.menuMenu.setObjectName("menuMenu")
        self.filemenu.setObjectName("filemenu")
        self.help_menu.setObjectName("help_menu")


        MainWindow.setMenuBar(self.barre_menu)
        self.barre_menu.addAction(self.menuMenu.menuAction())
        self.barre_menu.addAction(self.help_menu.menuAction())

        self.barre_menu.addAction(self.filemenu.menuAction())
        self.barre_menu.addAction(self.bureau_menu.menuAction())

        self.exit_action = QtWidgets.QAction("Exit", self)
        self.exit_action.setShortcut("Ctrl+Q")
        self.exit_action.setStatusTip("Exit application")

        self.menu_barre_connexion = QtWidgets.QAction("Connexion", self)
        self.menu_barre_connexion.setShortcut("Ctrl+Maj+C")
        self.menu_barre_connexion.setStatusTip("Connexion à une base de données")





        self.filemenu.addAction(self.exit_action)
        self.filemenu.addAction(self.menu_barre_connexion)

        # self.exit_action.triggered.connect(QtWidgets.qApp.quit)
        self.exit_action.triggered.connect(self.login_widget.hide)

        self.help_menu.triggered.connect(self.login_widget.hide)
        self.barre_menu.addAction(self.exit_action)




        self.database_connexion()

        # self.menu_barre_connexion.triggered.connect(self.widget_connexion.show)
        self.menu_barre_connexion.triggered.connect(self.login_widget.hide)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.username_login_lineEdit, self.password_login_lineEdit)
        MainWindow.setTabOrder(self.password_login_lineEdit, self.login_button)
        MainWindow.setTabOrder(self.login_button, self.sigup_login_button)
        MainWindow.setTabOrder(self.sigup_login_button, self.prenom_sigunp_lineEdit)
        MainWindow.setTabOrder(self.prenom_sigunp_lineEdit, self.nom_signup_lineEdit)
        MainWindow.setTabOrder(self.nom_signup_lineEdit, self.username_signup_lineEdit)
        MainWindow.setTabOrder(self.username_signup_lineEdit, self.password_signup_lineEdit)
        MainWindow.setTabOrder(self.password_signup_lineEdit, self.confirmation_pass_signup_lineEdit)
        MainWindow.setTabOrder(self.confirmation_pass_signup_lineEdit, self.signup_signup_button)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "La gestion des inscription"))
        # MainWindow.setWindowIcon(QtGui.QIcon("icons/line.png"))
        self.username_login_lineEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p>Vous pouvez faire entrer votre nom d\'utilisateur ou votre adresse mail</p></body></html>"))
        self.username_login_lineEdit.setPlaceholderText(_translate("MainWindow", "Username or email"))
        self.password_login_lineEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p>Votre mot de passe que avez mis lors de votre inscription</p></body></html>"))
        self.password_login_lineEdit.setPlaceholderText(_translate("MainWindow", "Password"))
        self.login_button.setText(_translate("MainWindow", "Login"))
        self.sigup_login_button.setText(_translate("MainWindow", "Sigup"))
        self.username_login_label.setText(_translate("MainWindow", "Username"))
        self.password_label.setText(_translate("MainWindow", "Password"))
        self.or_login_label.setText(_translate("MainWindow", "Ou"))
        self.username_signup_label.setText(_translate("MainWindow", "Username"))
        self.prenom_signup_label.setText(_translate("MainWindow", "Prenom"))
        self.nom_signup_label.setText(_translate("MainWindow", "Nom"))
        self.password_signup_label.setText(_translate("MainWindow", "Password"))
        self.confirmation_pass_signup_label.setText(_translate("MainWindow", "Confirmation"))
        self.prenom_sigunp_lineEdit.setPlaceholderText(_translate("MainWindow", "Michel"))
        self.nom_signup_lineEdit.setPlaceholderText(_translate("MainWindow", "Saint Pierre"))
        self.username_signup_lineEdit.setPlaceholderText(_translate("MainWindow", "ExcellenceMichel"))
        self.password_signup_lineEdit.setPlaceholderText(_translate("MainWindow", "Plus de 7 caractères"))
        self.confirmation_pass_signup_lineEdit.setPlaceholderText(_translate("MainWindow", "Confirmation du mot de passe"))
        self.signup_signup_button.setText(_translate("MainWindow", "Enregistrer"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.help_menu.setTitle(_translate("MainWindow", "Help"))
        self.filemenu.setTitle(_translate("MainWindow", "File"))
        self.bureau_menu.setTitle(_translate("MainWindow", "Bureau"))






    def database_connexion(self):


        self.widget_connexion = QtWidgets.QWidget(self.centralwidget)
        self.widget_connexion.hide()
        self.widget_connexion.setGeometry(QtCore.QRect(12, 112, 521, 321))

        # self.widget_connexion = QtWidgets.QWidget(self.centralwidget)
        # self.widget_connexion.setGeometry(QtCore.QRect(12, 112, 521, 321))
        # self.widget_connexion.setObjectName("widget_connexion")


        hboxlayout = QtWidgets.QHBoxLayout()

        self.dbname_lineEdit = QtWidgets.QLineEdit()
        self.dbname_lineEdit.setPlaceholderText("Nom de la base de données")

        self.dbuser_lineEdit = QtWidgets.QLineEdit()
        self.dbuser_lineEdit.setPlaceholderText("L'utilisateur de la base de bonnées")

        self.dbhost_lineEdit = QtWidgets.QLineEdit()
        self.dbhost_lineEdit.setPlaceholderText("Serveur location")

        self.dbpassword_lineEdit = QtWidgets.QLineEdit()
        self.dbpassword_lineEdit.setPlaceholderText("Mot de passe")

        self.dbport_lineEdit = QtWidgets.QLineEdit()
        self.dbport_lineEdit.setPlaceholderText("Port d'entrée")


        hboxlayout.addWidget(self.dbname_lineEdit)
        hboxlayout.addWidget(self.dbuser_lineEdit)
        hboxlayout.addWidget(self.dbhost_lineEdit)
        hboxlayout.addWidget(self.dbpassword_lineEdit)
        hboxlayout.addWidget(self.dbport_lineEdit)



        self.button_connexion = QtWidgets.QPushButton("Login")
        hboxlayout.addWidget(self.button_connexion)

        vbwidget = QtWidgets.QVBoxLayout()

        # vbwidget.addWidget(hboxlayout)


        self.widget_connexion.setLayout(hboxlayout)
        
        self.button_connexion.clicked.connect(self.login_db_button_clicked)
        self.button_connexion.clicked.connect(self.widget_connexion.hide)






    def login_db_button_clicked(self):

        dbname_lineEdit_value = self.dbname_lineEdit.text()
        dbuser_lineEdit_value = self.dbuser_lineEdit.text()
        dbhost_lineEdit_value = self.dbhost_lineEdit.text()
        dbpassword_lineEdit_value = self.dbpassword_lineEdit.text()
        dbport_lineEdit_value =  self.dbport_lineEdit.text()
        # import pdb; pdb.set<_trace()
        dt=mydb
    
        mydb.connexion_database(dt,dbname=dbname_lineEdit_value, user=dbuser_lineEdit_value, host=dbhost_lineEdit_value, password=dbpassword_lineEdit_value, port=dbport_lineEdit_value)
        QtWidgets.QMessageBox.information(self, "Information sur la connexion", "La connexion s'est bien déroulée")


        # except:
        #     print("La connexion n'a pas marché")
        #     QtWidgets.QMessageBox.information(self,  "Information sur la connexion", "La connexion s'est pas bien déroulée")
        





