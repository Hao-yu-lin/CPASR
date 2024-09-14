# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1350, 800)
        MainWindow.setMinimumSize(QSize(1350, 800))
        self.CentralWidget = QWidget(MainWindow)
        self.CentralWidget.setObjectName(u"CentralWidget")
        self.CentralWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.CentralWidget.setStyleSheet(u"background-color: rgb(105, 105, 105);\n"
"border-color: rgb(94, 92, 100);")
        self.verticalLayout = QVBoxLayout(self.CentralWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.MenuBar = QWidget(self.CentralWidget)
        self.MenuBar.setObjectName(u"MenuBar")
        self.MenuBar.setMinimumSize(QSize(0, 52))
        self.MenuBar.setMaximumSize(QSize(16777215, 52))
        self.MenuBar.setAutoFillBackground(False)
        self.MenuBar.setStyleSheet(u"background-color: rgb(246, 245, 244);\n"
"border-color: rgb(94, 92, 100);")

        self.verticalLayout.addWidget(self.MenuBar)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ContentBar = QWidget(self.CentralWidget)
        self.ContentBar.setObjectName(u"ContentBar")
        self.ContentBar.setMinimumSize(QSize(300, 0))
        self.ContentBar.setMaximumSize(QSize(300, 16777215))
        self.ContentBar.setStyleSheet(u"background-color: rgb(246, 245, 244);")

        self.horizontalLayout.addWidget(self.ContentBar)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.StatisticsView = QWidget(self.CentralWidget)
        self.StatisticsView.setObjectName(u"StatisticsView")
        self.StatisticsView.setMinimumSize(QSize(0, 100))
        self.StatisticsView.setMaximumSize(QSize(16777215, 100))
        self.StatisticsView.setStyleSheet(u"background-color: rgb(246, 245, 244);\n"
"border-color: rgb(94, 92, 100);")

        self.verticalLayout_2.addWidget(self.StatisticsView)

        self.Viewer = QWidget(self.CentralWidget)
        self.Viewer.setObjectName(u"Viewer")
        self.Viewer.setMinimumSize(QSize(1036, 597))
        self.Viewer.setStyleSheet(u"background-color: rgb(246, 245, 244);\n"
"border-color: rgb(94, 92, 100);")

        self.verticalLayout_2.addWidget(self.Viewer)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.CentralWidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi

