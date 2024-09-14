# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_StatisticsView.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_StatisticsView(object):
    def setupUi(self, StatisticsView):
        if not StatisticsView.objectName():
            StatisticsView.setObjectName(u"StatisticsView")
        StatisticsView.resize(1036, 100)
        StatisticsView.setMinimumSize(QSize(1036, 100))
        StatisticsView.setMaximumSize(QSize(16777215, 100))
        StatisticsView.setStyleSheet(u"background-color: rgb(190, 190, 190);")
        self.label_avgsurface = QLabel(StatisticsView)
        self.label_avgsurface.setObjectName(u"label_avgsurface")
        self.label_avgsurface.setGeometry(QRect(10, 36, 270, 30))
        self.label_avgsurface.setMinimumSize(QSize(270, 30))
        self.label_avgsurface.setMaximumSize(QSize(270, 30))
        self.label_d2 = QLabel(StatisticsView)
        self.label_d2.setObjectName(u"label_d2")
        self.label_d2.setGeometry(QRect(570, 36, 270, 25))
        self.label_d2.setMinimumSize(QSize(270, 0))
        self.label_d2.setMaximumSize(QSize(270, 16777215))
        self.label_mode = QLabel(StatisticsView)
        self.label_mode.setObjectName(u"label_mode")
        self.label_mode.setGeometry(QRect(290, 36, 270, 30))
        self.label_mode.setMinimumSize(QSize(270, 30))
        self.label_mode.setMaximumSize(QSize(270, 30))
        self.label_d3 = QLabel(StatisticsView)
        self.label_d3.setObjectName(u"label_d3")
        self.label_d3.setGeometry(QRect(570, 71, 270, 25))
        self.label_d3.setMinimumSize(QSize(270, 0))
        self.label_d3.setMaximumSize(QSize(270, 16777215))
        self.label_nums = QLabel(StatisticsView)
        self.label_nums.setObjectName(u"label_nums")
        self.label_nums.setGeometry(QRect(290, 71, 270, 25))
        self.label_nums.setMinimumSize(QSize(270, 0))
        self.label_nums.setMaximumSize(QSize(270, 16777215))
        self.label_d1 = QLabel(StatisticsView)
        self.label_d1.setObjectName(u"label_d1")
        self.label_d1.setGeometry(QRect(570, 0, 270, 26))
        self.label_d1.setMinimumSize(QSize(270, 0))
        self.label_d1.setMaximumSize(QSize(270, 16777215))
        self.label_deviation = QLabel(StatisticsView)
        self.label_deviation.setObjectName(u"label_deviation")
        self.label_deviation.setGeometry(QRect(10, 71, 270, 30))
        self.label_deviation.setMinimumSize(QSize(270, 30))
        self.label_deviation.setMaximumSize(QSize(270, 30))
        self.label_property_title = QLabel(StatisticsView)
        self.label_property_title.setObjectName(u"label_property_title")
        self.label_property_title.setGeometry(QRect(10, 0, 550, 30))
        self.label_property_title.setMinimumSize(QSize(0, 30))
        self.label_property_title.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_property_title.setFont(font)

        self.retranslateUi(StatisticsView)

        QMetaObject.connectSlotsByName(StatisticsView)
    # setupUi

    def retranslateUi(self, StatisticsView):
        StatisticsView.setWindowTitle(QCoreApplication.translate("StatisticsView", u"Form", None))
        self.label_avgsurface.setText(QCoreApplication.translate("StatisticsView", u"Average Surface :", None))
        self.label_d2.setText(QCoreApplication.translate("StatisticsView", u"D2 :", None))
        self.label_mode.setText(QCoreApplication.translate("StatisticsView", u"Mode Surface : ", None))
        self.label_d3.setText(QCoreApplication.translate("StatisticsView", u"D3 :", None))
        self.label_nums.setText(QCoreApplication.translate("StatisticsView", u"Nums Coffee Particle : ", None))
        self.label_d1.setText(QCoreApplication.translate("StatisticsView", u"D1 :", None))
        self.label_deviation.setText(QCoreApplication.translate("StatisticsView", u"Standard Deviation :", None))
        self.label_property_title.setText(QCoreApplication.translate("StatisticsView", u"<html><head/><body><p>Properties of the Particle Distribution</p></body></html>", None))
    # retranslateUi

