# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_Viewer.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget, QStackedWidget)

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

class Ui_Viewer(object):
    def setupUi(self, Viewer):
        if not Viewer.objectName():
            Viewer.setObjectName(u"Viewer")
        Viewer.resize(1046, 607)
        Viewer.setMinimumSize(QSize(1036, 597))
        Viewer.setMouseTracking(False)
        Viewer.setStyleSheet(u"background-color: rgb(190, 190, 190);")
        self.verticalLayout_2 = QVBoxLayout(Viewer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)

        self.scrollArea = QScrollArea(Viewer)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(1036, 597))
        self.scrollArea.setStyleSheet(u"background-color: rgb(190, 190, 190);")
        self.scrollArea.setWidgetResizable(True)

        self.stackedWidget = QStackedWidget(Viewer)
        self.stackedWidget.setMinimumSize(QSize(1036, 597))

        # QLabel for displaying the image
        self.label_view = QLabel()
        self.label_view.setObjectName(u"label_view")
        self.label_view.setGeometry(QRect(12, 12, 1036, 597))
        self.label_view.setMinimumSize(QSize(1036, 597))
        self.label_view.setAlignment(Qt.AlignCenter)
        self.label_view.setStyleSheet(u"background-color: rgb(190, 190, 190);")

        # Matplotlib FigureCanvas for histogram or chart
        self.cvHistogram = FigureCanvas(plt.Figure())
        self.cvHistogram.setGeometry(QRect(12, 12, 1036, 597))
        self.cvHistogram.setMinimumSize(QSize(1036, 597))

        # Add both widgets (image and chart) to the stacked widget
        self.stackedWidget.addWidget(self.label_view)  # Index 0
        self.stackedWidget.addWidget(self.cvHistogram)  # Index 1

        # Add both widgets to the layout but show one at a time
        self.scrollArea.setWidget(self.stackedWidget)  # Initially set the image view
        self.verticalLayout_2.addWidget(self.scrollArea)

        self.retranslateUi(Viewer)
        QMetaObject.connectSlotsByName(Viewer)
    # setupUi

    def retranslateUi(self, Viewer):
        Viewer.setWindowTitle(QCoreApplication.translate("Viewer", u"Form", None))
        self.label_view.setText(QCoreApplication.translate("Viewer", u"No Image Loaded", None))
    # retranslateUi

