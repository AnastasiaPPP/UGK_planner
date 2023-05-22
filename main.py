import sys
from PyQt6.QtWidgets import QApplication, QDialog
from qtpy import uic

Form, Window = uic.loadUiType("ugk_planner.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()


def one_click():
    print(form.calendarWidget.selectedDate().toString('dd-MM-yyyy'))


def one_click_calendar():
    print(form.calendarWidget.selectedDate().toString('dd-MM-yyyy'))
    form.dateTimeEdit.setDate(form.calendarWidget.selectedDate())


def one_dateedit_change():
    print(form.dateTimeEdit.dateTime().toString('dd-MM-yyyy'))
    form.calendarWidget.setSelectedDate(form.dateTimeEdit.date())


form.pushButton.clicked.connect(one_click)
form.calendarWidget.clicked.connect(one_click_calendar)
form.dateTimeEdit.dateChanged.connect(one_dateedit_change)

window.show()

sys.exit(app.exec())
