from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(428, 390)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(16)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.cbox_clasic = QtWidgets.QCheckBox(self.groupBox)
        self.cbox_clasic.setObjectName("cbox_clasic")
        self.verticalLayout_3.addWidget(self.cbox_clasic)
        self.cbox_margharita = QtWidgets.QCheckBox(self.groupBox)
        self.cbox_margharita.setObjectName("cbox_margharita")
        self.verticalLayout_3.addWidget(self.cbox_margharita)
        self.cbox_turkish = QtWidgets.QCheckBox(self.groupBox)
        self.cbox_turkish.setObjectName("cbox_turkish")
        self.verticalLayout_3.addWidget(self.cbox_turkish)
        self.cbox_simple = QtWidgets.QCheckBox(self.groupBox)
        self.cbox_simple.setObjectName("cbox_simple")
        self.verticalLayout_3.addWidget(self.cbox_simple)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.line_price = QtWidgets.QLineEdit(self.groupBox_4)
        self.line_price.setEnabled(True)
        self.line_price.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.line_price.setAutoFillBackground(False)
        self.line_price.setMaxLength(32782)
        self.line_price.setFrame(True)
        self.line_price.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.line_price.setCursorPosition(3)
        self.line_price.setReadOnly(True)
        self.line_price.setObjectName("line_price")
        self.verticalLayout_2.addWidget(self.line_price)
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.line_name = QtWidgets.QLineEdit(self.groupBox_4)
        self.line_name.setObjectName("line_name")
        self.verticalLayout_2.addWidget(self.line_name)
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.line_id = QtWidgets.QLineEdit(self.groupBox_4)
        self.line_id.setText("")
        self.line_id.setObjectName("line_id")
        self.verticalLayout_2.addWidget(self.line_id)
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.line_credit_number = QtWidgets.QLineEdit(self.groupBox_4)
        self.line_credit_number.setText("")
        self.line_credit_number.setObjectName("line_credit_number")
        self.verticalLayout_2.addWidget(self.line_credit_number)
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.line_credit_pass = QtWidgets.QLineEdit(self.groupBox_4)
        self.line_credit_pass.setText("")
        self.line_credit_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_credit_pass.setObjectName("line_credit_pass")
        self.verticalLayout_2.addWidget(self.line_credit_pass)
        self.pushButton_finish = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_finish.setObjectName("pushButton_finish")
        self.verticalLayout_2.addWidget(self.pushButton_finish)
        self.gridLayout.addWidget(self.groupBox_4, 1, 1, 2, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.cbox_sauce_olive = QtWidgets.QCheckBox(self.groupBox_2)
        self.cbox_sauce_olive.setObjectName("cbox_sauce_olive")
        self.verticalLayout_4.addWidget(self.cbox_sauce_olive)
        self.cbox_sauce_mushroom = QtWidgets.QCheckBox(self.groupBox_2)
        self.cbox_sauce_mushroom.setObjectName("cbox_sauce_mushroom")
        self.verticalLayout_4.addWidget(self.cbox_sauce_mushroom)
        self.cbox_sauce_goatCheese = QtWidgets.QCheckBox(self.groupBox_2)
        self.cbox_sauce_goatCheese.setObjectName("cbox_sauce_goatCheese")
        self.verticalLayout_4.addWidget(self.cbox_sauce_goatCheese)
        self.cbox_sauce_meat = QtWidgets.QCheckBox(self.groupBox_2)
        self.cbox_sauce_meat.setObjectName("cbox_sauce_meat")
        self.verticalLayout_4.addWidget(self.cbox_sauce_meat)
        self.cbox_sauce_onion = QtWidgets.QCheckBox(self.groupBox_2)
        self.cbox_sauce_onion.setObjectName("cbox_sauce_onion")
        self.verticalLayout_4.addWidget(self.cbox_sauce_onion)
        self.cbox_sauce_corn = QtWidgets.QCheckBox(self.groupBox_2)
        self.cbox_sauce_corn.setObjectName("cbox_sauce_corn")
        self.verticalLayout_4.addWidget(self.cbox_sauce_corn)
        self.gridLayout.addWidget(self.groupBox_2, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 428, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setWindowIcon(QtGui.QIcon('pizzaLogo.png'))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Pizza Order\'a Hoşgeldiniz!</span></p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", " Lütfen bir pizza tabanı seçiniz "))
        self.cbox_clasic.setText(_translate("MainWindow", "Klasik"))
        self.cbox_margharita.setText(_translate("MainWindow", "Margarita"))
        self.cbox_turkish.setText(_translate("MainWindow", "Türk Pizza"))
        self.cbox_simple.setText(_translate("MainWindow", "Sade"))
        self.groupBox_4.setTitle(_translate("MainWindow", " Ödeme İşlemleri "))
        self.label_2.setText(_translate("MainWindow", "Toplam Tutar"))
        self.line_price.setText(_translate("MainWindow", "0 ₺"))
        self.label_3.setText(_translate("MainWindow", "İsim"))
        self.label_4.setText(_translate("MainWindow", "ID Numara"))
        self.label_5.setText(_translate("MainWindow", "Kredi Kartı Numarası"))
        self.label_6.setText(_translate("MainWindow", "Kredi Kartı Parolası"))
        self.pushButton_finish.setText(_translate("MainWindow", "Ödemeyi Tamamla"))
        self.groupBox_2.setTitle(_translate("MainWindow", " Lütfen sos seçimi yapınız "))
        self.cbox_sauce_olive.setText(_translate("MainWindow", "Zeytin"))
        self.cbox_sauce_mushroom.setText(_translate("MainWindow", "Mantar"))
        self.cbox_sauce_goatCheese.setText(_translate("MainWindow", "Keçi Peyniri"))
        self.cbox_sauce_meat.setText(_translate("MainWindow", "Et"))
        self.cbox_sauce_onion.setText(_translate("MainWindow", "Soğan"))
        self.cbox_sauce_corn.setText(_translate("MainWindow", "Mısır"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
