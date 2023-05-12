import sys
from PyQt6.QtWidgets import QApplication, QDialog
from ugk import Ui_ugk_planner

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_ugk_planner()
ui.setupUi(window)

window.show()
sys.exit(app.exec())