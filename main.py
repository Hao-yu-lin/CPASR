import sys
from PySide6.QtWidgets import QApplication
from View.MainWindow import MainWindow
from Controller.MainController import MainController




if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    # app.setStyleSheet("QLabel { color: black; }")
    app.setStyleSheet("QPushButton { color: black; } "
                      "QLabel { color: black; } "
                      "QCheckBox{color: black; }"
                      "QLineEdit{color: black; }"
                      "QComboBox{color: black; }")

    _MainWindow = MainWindow()
    _mainController = MainController(_MainWindow)
    _MainWindow.show()
    sys.exit(app.exec())



