# Form implementation generated from reading ui file 'ui_imagedialog.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ugk_planner(object):
    def setupUi(self, ugk_planner):
        ugk_planner.setObjectName("ugk_planner")
        ugk_planner.resize(986, 709)
        ugk_planner.setAutoFillBackground(False)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=ugk_planner)
        self.buttonBox.setGeometry(QtCore.QRect(790, 650, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.calendarWidget = QtWidgets.QCalendarWidget(parent=ugk_planner)
        self.calendarWidget.setGeometry(QtCore.QRect(40, 330, 271, 301))
        self.calendarWidget.setObjectName("calendarWidget")
        self.textEdit = QtWidgets.QTextEdit(parent=ugk_planner)
        self.textEdit.setGeometry(QtCore.QRect(40, 170, 271, 141))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(parent=ugk_planner)
        self.textEdit_2.setGeometry(QtCore.QRect(40, 20, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(parent=ugk_planner)
        self.dateTimeEdit.setGeometry(QtCore.QRect(40, 650, 271, 24))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.textEdit_3 = QtWidgets.QTextEdit(parent=ugk_planner)
        self.textEdit_3.setGeometry(QtCore.QRect(40, 100, 271, 51))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(parent=ugk_planner)
        self.textEdit_4.setGeometry(QtCore.QRect(340, 20, 621, 611))
        self.textEdit_4.setObjectName("textEdit_4")
        self.pushButton = QtWidgets.QPushButton(parent=ugk_planner)
        self.pushButton.setGeometry(QtCore.QRect(340, 650, 113, 32))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(ugk_planner)
        self.buttonBox.accepted.connect(ugk_planner.accept) # type: ignore
        self.buttonBox.rejected.connect(ugk_planner.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(ugk_planner)

    def retranslateUi(self, ugk_planner):
        _translate = QtCore.QCoreApplication.translate
        ugk_planner.setWindowTitle(_translate("ugk_planner", "UGK"))
        self.textEdit.setHtml(_translate("ugk_planner", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir=\'rtl\' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; color:#9e1d22;\">Описание события</span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("ugk_planner", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; color:#000000;\">Введите ФИО</span></p></body></html>"))
        self.textEdit_3.setHtml(_translate("ugk_planner", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt;\">Кафедра</span></p></body></html>"))
        self.textEdit_4.setHtml(_translate("ugk_planner", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt;\">Таблица с расписанием</span></p></body></html>"))
        self.pushButton.setText(_translate("ugk_planner", "PushButton"))
