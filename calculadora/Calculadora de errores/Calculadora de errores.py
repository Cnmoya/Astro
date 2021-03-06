# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import operaciones_de_errores as oper

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):
    def setupUi(self):
        self.setObjectName(_fromUtf8("MainWindow"))
        self.resize(560, 552)
        self.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(177, 177, 177, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.mas = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mas.sizePolicy().hasHeightForWidth())
        self.mas.setSizePolicy(sizePolicy)
        self.mas.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(24)
        self.mas.setFont(font)
        self.mas.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 61);"))
        self.mas.setObjectName(_fromUtf8("mas"))
        self.gridLayout.addWidget(self.mas, 6, 5, 1, 1)
        self.error_botton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.error_botton.sizePolicy().hasHeightForWidth())
        self.error_botton.setSizePolicy(sizePolicy)
        self.error_botton.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(24)
        self.error_botton.setFont(font)
        self.error_botton.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 61);"))
        self.error_botton.setCheckable(True)
        self.error_botton.setObjectName(_fromUtf8("error_botton"))
        self.gridLayout.addWidget(self.error_botton, 3, 0, 1, 1)
        self.multiplicacion = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.multiplicacion.sizePolicy().hasHeightForWidth())
        self.multiplicacion.setSizePolicy(sizePolicy)
        self.multiplicacion.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(24)
        self.multiplicacion.setFont(font)
        self.multiplicacion.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 61);"))
        self.multiplicacion.setObjectName(_fromUtf8("multiplicacion"))
        self.gridLayout.addWidget(self.multiplicacion, 4, 5, 1, 1)
        self.division = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.division.sizePolicy().hasHeightForWidth())
        self.division.setSizePolicy(sizePolicy)
        self.division.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(24)
        self.division.setFont(font)
        self.division.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 61);"))
        self.division.setObjectName(_fromUtf8("division"))
        self.gridLayout.addWidget(self.division, 3, 2, 1, 1)
        self.elevado = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.elevado.sizePolicy().hasHeightForWidth())
        self.elevado.setSizePolicy(sizePolicy)
        self.elevado.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(36)
        self.elevado.setFont(font)
        self.elevado.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 61);"))
        self.elevado.setObjectName(_fromUtf8("elevado"))
        self.gridLayout.addWidget(self.elevado, 3, 1, 1, 1)
        self.menos = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menos.sizePolicy().hasHeightForWidth())
        self.menos.setSizePolicy(sizePolicy)
        self.menos.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(24)
        self.menos.setFont(font)
        self.menos.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 61);"))
        self.menos.setObjectName(_fromUtf8("menos"))
        self.gridLayout.addWidget(self.menos, 5, 5, 1, 1)
        self.igual = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.igual.sizePolicy().hasHeightForWidth())
        self.igual.setSizePolicy(sizePolicy)
        self.igual.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(24)
        self.igual.setFont(font)
        self.igual.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 61);"))
        self.igual.setObjectName(_fromUtf8("igual"))
        self.gridLayout.addWidget(self.igual, 7, 5, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.botton4 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.botton4.sizePolicy().hasHeightForWidth())
        self.botton4.setSizePolicy(sizePolicy)
        self.botton4.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(24)
        self.botton4.setFont(font)
        self.botton4.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 61);"))
        self.botton4.setObjectName(_fromUtf8("botton4"))
        self.gridLayout_2.addWidget(self.botton4, 1, 0, 1, 1)
        self.boton1 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton1.sizePolicy().hasHeightForWidth())
        self.boton1.setSizePolicy(sizePolicy)
        self.boton1.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(24)
        self.boton1.setFont(font)
        self.boton1.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 61);"))
        self.boton1.setObjectName(_fromUtf8("boton1"))
        self.gridLayout_2.addWidget(self.boton1, 2, 0, 1, 1)
        self.boton5 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton5.sizePolicy().hasHeightForWidth())
        self.boton5.setSizePolicy(sizePolicy)
        self.boton5.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(24)
        self.boton5.setFont(font)
        self.boton5.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 61);"))
        self.boton5.setObjectName(_fromUtf8("boton5"))
        self.gridLayout_2.addWidget(self.boton5, 1, 1, 1, 1)
        self.boton7 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton7.sizePolicy().hasHeightForWidth())
        self.boton7.setSizePolicy(sizePolicy)
        self.boton7.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(24)
        self.boton7.setFont(font)
        self.boton7.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 61);"))
        self.boton7.setObjectName(_fromUtf8("boton7"))
        self.gridLayout_2.addWidget(self.boton7, 0, 0, 1, 1)
        self.boton8 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton8.sizePolicy().hasHeightForWidth())
        self.boton8.setSizePolicy(sizePolicy)
        self.boton8.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(24)
        self.boton8.setFont(font)
        self.boton8.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 61);"))
        self.boton8.setObjectName(_fromUtf8("boton8"))
        self.gridLayout_2.addWidget(self.boton8, 0, 1, 1, 1)
        self.boton9 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton9.sizePolicy().hasHeightForWidth())
        self.boton9.setSizePolicy(sizePolicy)
        self.boton9.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(24)
        self.boton9.setFont(font)
        self.boton9.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 61);"))
        self.boton9.setObjectName(_fromUtf8("boton9"))
        self.gridLayout_2.addWidget(self.boton9, 0, 2, 1, 1)
        self.boton2 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton2.sizePolicy().hasHeightForWidth())
        self.boton2.setSizePolicy(sizePolicy)
        self.boton2.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(24)
        self.boton2.setFont(font)
        self.boton2.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 61);"))
        self.boton2.setObjectName(_fromUtf8("boton2"))
        self.gridLayout_2.addWidget(self.boton2, 2, 1, 1, 1)
        self.boton6 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton6.sizePolicy().hasHeightForWidth())
        self.boton6.setSizePolicy(sizePolicy)
        self.boton6.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(24)
        self.boton6.setFont(font)
        self.boton6.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 61);"))
        self.boton6.setObjectName(_fromUtf8("boton6"))
        self.gridLayout_2.addWidget(self.boton6, 1, 2, 1, 1)
        self.boton3 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton3.sizePolicy().hasHeightForWidth())
        self.boton3.setSizePolicy(sizePolicy)
        self.boton3.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(24)
        self.boton3.setFont(font)
        self.boton3.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 61);"))
        self.boton3.setObjectName(_fromUtf8("boton3"))
        self.gridLayout_2.addWidget(self.boton3, 2, 2, 1, 1)
        self.coma = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.coma.sizePolicy().hasHeightForWidth())
        self.coma.setSizePolicy(sizePolicy)
        self.coma.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(24)
        self.coma.setFont(font)
        self.coma.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 61);"))
        self.coma.setObjectName(_fromUtf8("coma"))
        self.gridLayout_2.addWidget(self.coma, 3, 2, 1, 1)
        self.botton0 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.botton0.sizePolicy().hasHeightForWidth())
        self.botton0.setSizePolicy(sizePolicy)
        self.botton0.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(24)
        self.botton0.setFont(font)
        self.botton0.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 61);"))
        self.botton0.setObjectName(_fromUtf8("botton0"))
        self.gridLayout_2.addWidget(self.botton0, 3, 0, 1, 2)
        self.gridLayout.addLayout(self.gridLayout_2, 4, 0, 4, 5)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.datos = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.datos.sizePolicy().hasHeightForWidth())
        self.datos.setSizePolicy(sizePolicy)
        self.datos.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(24)
        self.datos.setFont(font)
        self.datos.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 61);"))
        self.datos.setText(_fromUtf8(""))
        self.datos.setReadOnly(True)
        self.datos.setObjectName(_fromUtf8("datos"))
        self.horizontalLayout.addWidget(self.datos)
        self.error = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.error.sizePolicy().hasHeightForWidth())
        self.error.setSizePolicy(sizePolicy)
        self.error.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(24)
        self.error.setFont(font)
        self.error.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 61);"))
        self.error.setText(_fromUtf8(""))
        self.error.setReadOnly(True)
        self.error.setObjectName(_fromUtf8("error"))
        self.horizontalLayout.addWidget(self.error)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 6)
        self.masmenos = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.masmenos.sizePolicy().hasHeightForWidth())
        self.masmenos.setSizePolicy(sizePolicy)
        self.masmenos.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(24)
        self.masmenos.setFont(font)
        self.masmenos.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 61);"))
        self.masmenos.setObjectName(_fromUtf8("masmenos"))
        self.gridLayout.addWidget(self.masmenos, 3, 3, 1, 1)
        self.borrar = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.borrar.sizePolicy().hasHeightForWidth())
        self.borrar.setSizePolicy(sizePolicy)
        self.borrar.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(24)
        self.borrar.setFont(font)
        self.borrar.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 61);"))
        self.borrar.setObjectName(_fromUtf8("borrar"))
        self.gridLayout.addWidget(self.borrar, 3, 4, 1, 2)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 560, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.setMenuBar(self.menubar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("Calculador de Errores")
        self.mas.setText(_translate("MainWindow", "+", None))
        self.mas.setShortcut(_translate("MainWindow", "+", None))
        self.error_botton.setText(_translate("MainWindow", "ERROR", None))
        self.error_botton.setShortcut(_translate("MainWindow", "Space", None))
        self.multiplicacion.setText(_translate("MainWindow", "*", None))
        self.multiplicacion.setShortcut(_translate("MainWindow", "*", None))
        self.division.setText(_translate("MainWindow", "/", None))
        self.division.setShortcut(_translate("MainWindow", "/", None))
        self.elevado.setText(_translate("MainWindow", "^ ", None))
        self.menos.setText(_translate("MainWindow", "-", None))
        self.menos.setShortcut(_translate("MainWindow", "-", None))
        self.igual.setText(_translate("MainWindow", "=", None))
        self.igual.setShortcut(_translate("MainWindow", "=", None))
        self.botton4.setText(_translate("MainWindow", "4", None))
        self.botton4.setShortcut(_translate("MainWindow", "4", None))
        self.boton1.setText(_translate("MainWindow", "1", None))
        self.boton1.setShortcut(_translate("MainWindow", "1", None))
        self.boton5.setText(_translate("MainWindow", "5", None))
        self.boton5.setShortcut(_translate("MainWindow", "5", None))
        self.boton7.setText(_translate("MainWindow", "7", None))
        self.boton7.setShortcut(_translate("MainWindow", "7", None))
        self.boton8.setText(_translate("MainWindow", "8", None))
        self.boton8.setShortcut(_translate("MainWindow", "8", None))
        self.boton9.setText(_translate("MainWindow", "9", None))
        self.boton9.setShortcut(_translate("MainWindow", "9", None))
        self.boton2.setText(_translate("MainWindow", "2", None))
        self.boton2.setShortcut(_translate("MainWindow", "2", None))
        self.boton6.setText(_translate("MainWindow", "6", None))
        self.boton6.setShortcut(_translate("MainWindow", "6", None))
        self.boton3.setText(_translate("MainWindow", "3", None))
        self.boton3.setShortcut(_translate("MainWindow", "3", None))
        self.coma.setText(_translate("MainWindow", ",", None))
        self.coma.setShortcut(",")
        self.botton0.setText(_translate("MainWindow", "0", None))
        self.botton0.setShortcut(_translate("MainWindow", "0", None))
        self.masmenos.setText(_translate("MainWindow", "+/-", None))
        self.borrar.setText(_translate("MainWindow", "<-", None))
        self.borrar.setShortcut(_translate("MainWindow", "Backspace", None))
        self.elevado.setShortcut("")
        self.boton1.clicked.connect(self.teclado_signal)
        self.boton2.clicked.connect(self.teclado_signal)
        self.boton3.clicked.connect(self.teclado_signal)
        self.botton4.clicked.connect(self.teclado_signal)
        self.boton5.clicked.connect(self.teclado_signal)
        self.boton6.clicked.connect(self.teclado_signal)
        self.boton7.clicked.connect(self.teclado_signal)
        self.boton8.clicked.connect(self.teclado_signal)
        self.boton9.clicked.connect(self.teclado_signal)
        self.botton0.clicked.connect(self.teclado_signal)
        self.error_botton.clicked.connect(self.error_signal)
        self.coma.clicked.connect(self.coma_siganl)
        self.borrar.clicked.connect(self.borrar_siganl)
        self.mas.clicked.connect(self.mas_signal)
        self.menos.clicked.connect(self.menos_signal)
        self.multiplicacion.clicked.connect(self.multy_signal)
        self.elevado.clicked.connect(self.elev_signal)
        self.division.clicked.connect(self.div_signal)
        self.masmenos.clicked.connect(self.masmenos_signal)
        self.igual.clicked.connect(self.igual_signal)
        self.datos_anterior = 0
        self.error_anterior = 0
        self.display = True
        self.operacion = None



    def teclado_signal(self):
        sender = self.sender()
        if self.display:
            self.datos.setText(self.datos.text()+sender.text())
        else:
            self.error.setText(self.error.text()+sender.text())


    def error_signal(self):
        self.display = not self.display


    def coma_siganl(self):
        sender = self.sender()
        if self.display :
            if self.datos.text().find(",")==-1:
                self.datos.setText(self.datos.text() + sender.text())
        elif self.error.text().find(",") ==-1:
            self.error.setText(self.error.text() + sender.text())


    def borrar_siganl(self):
        modifiers = QtGui.QApplication.keyboardModifiers()
        if self.display :
            self.datos.setText(self.datos.text()[:-1])
        else:
            self.error.setText(self.error.text()[:-1])
        if modifiers == QtCore.Qt.AltModifier:
            self.datos.setText("")
            self.error.setText("")


    def mas_signal(self):
        try:
            self.datos_anterior = float(self.datos.text().replace(",","."))
        except ValueError:
            self.datos_anterior = 0
        try:
            self.error_anterior = float(self.error.text().replace(",", "."))
        except ValueError:
            self.error_anterior = 0
        self.operacion = "mas"
        self.datos.setText("")
        self.error.setText("")



    def menos_signal(self):
        try:
            self.datos_anterior = float(self.datos.text().replace(",","."))
        except ValueError:
            self.datos_anterior = 0
        try:
            self.error_anterior = float(self.error.text().replace(",", "."))
        except ValueError:
            self.error_anterior = 0
        self.operacion = "menos"
        self.datos.setText("")
        self.error.setText("")



    def multy_signal(self):
        try:
            self.datos_anterior = float(self.datos.text().replace(",","."))
        except ValueError:
            self.datos_anterior = 0
        try:
            self.error_anterior = float(self.error.text().replace(",", "."))
        except ValueError:
            self.error_anterior = 0
        self.operacion = "multy"
        self.datos.setText("")
        self.error.setText("")


    def div_signal(self):
        try:
            self.datos_anterior = float(self.datos.text().replace(",", "."))
        except ValueError:
            self.datos_anterior = 0
        try:
            self.error_anterior = float(self.error.text().replace(",", "."))
        except ValueError:
            self.error_anterior = 0
        self.operacion = "div"
        self.datos.setText("")
        self.error.setText("")


    def elev_signal(self):
        try:
            self.datos_anterior = float(self.datos.text().replace(",","."))
        except ValueError:
            self.datos_anterior = 0
        try:
            self.error_anterior = float(self.error.text().replace(",", "."))
        except ValueError:
            self.error_anterior = 0
        self.operacion = "elev"
        self.datos.setText("")
        self.error.setText("")


    def masmenos_signal(self):
        if self.display:
            if self.datos.text().find("-") == -1:
                self.datos.setText("-" + self.datos.text())
            else:
                self.datos.setText(self.datos.text()[1:])
        else :
            if self.error.text().find("-") == -1:
                self.error.setText("-" + self.error.text())
            else:
                self.error.setText(self.error.text()[1:])


    def igual_signal(self):
        try:
            datos_temp = float(self.datos.text().replace(",","."))
        except ValueError:
            datos_temp = self.datos_anterior
        try:
            error_temp = float(self.error.text().replace(",", "."))
        except ValueError:
            error_temp = self.error_anterior
        if self.operacion == "mas":
            temp = oper.sumar_con_error(self.datos_anterior,self.error_anterior,
                                                    datos_temp,error_temp)
            self.datos.setText(str(temp[0]))
            self.error.setText(str(temp[1]))
        elif self.operacion == "menos":
            temp = oper.sumar_con_error(self.datos_anterior, self.error_anterior,
                                                           - datos_temp, error_temp)
            self.datos.setText(str(temp[0]))
            self.error.setText(str(temp[1]))
        elif self.operacion == "multy":
            temp = oper.multiplicacion_con_error(self.datos_anterior, self.error_anterior,
                                     datos_temp, error_temp)
            self.datos.setText(str(temp[0]))
            self.error.setText(str(temp[1]))
        elif self.operacion == "div":
            try:
                temp = oper.division_con_error(self.datos_anterior, self.error_anterior,
                                                 datos_temp, error_temp)
            except ValueError:
                temp = ("ERROR","ERROR")
            self.datos.setText(str(temp[0]))
            self.error.setText(str(temp[1]))
        elif self.operacion == "elev":
            temp = oper.elevacion_exacta(self.datos_anterior, self.error_anterior,
                                                 datos_temp)
            self.datos.setText(str(temp[0]))
            self.error.setText(str(temp[1]))
        self.operacion = None




if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())

