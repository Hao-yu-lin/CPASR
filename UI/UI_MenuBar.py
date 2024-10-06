# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_MenuBar.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QWidget)

class Ui_MenuBar(object):
    def setupUi(self, MenuBar):
        if not MenuBar.objectName():
            MenuBar.setObjectName(u"MenuBar")
        MenuBar.resize(1129, 52)
        MenuBar.setMinimumSize(QSize(0, 52))
        MenuBar.setMaximumSize(QSize(1152, 52))
        MenuBar.setToolTipDuration(0)
        MenuBar.setStyleSheet(u"background-color: rgb(246, 245, 244);\n"
"border-color: rgb(94, 92, 100);")
        self.horizontalLayout = QHBoxLayout(MenuBar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.horizontalLayout.setContentsMargins(10, 5, 10, 5)
        self.btn_open_img = QPushButton(MenuBar)
        self.btn_open_img.setObjectName(u"btn_open_img")
        self.btn_open_img.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_open_img.sizePolicy().hasHeightForWidth())
        self.btn_open_img.setSizePolicy(sizePolicy)
        self.btn_open_img.setMinimumSize(QSize(0, 28))
        self.btn_open_img.setMaximumSize(QSize(16777215, 28))
        font = QFont()
        font.setBold(True)
        self.btn_open_img.setFont(font)
        self.btn_open_img.setToolTipDuration(-1)
        self.btn_open_img.setAutoFillBackground(False)
        self.btn_open_img.setStyleSheet(u"")
        self.btn_open_img.setAutoDefault(False)
        self.btn_open_img.setFlat(False)

        self.horizontalLayout.addWidget(self.btn_open_img)

        self.btn_save_data = QPushButton(MenuBar)
        self.btn_save_data.setObjectName(u"btn_save_data")
        self.btn_save_data.setEnabled(False)
        sizePolicy.setHeightForWidth(self.btn_save_data.sizePolicy().hasHeightForWidth())
        self.btn_save_data.setSizePolicy(sizePolicy)
        self.btn_save_data.setMinimumSize(QSize(0, 28))
        self.btn_save_data.setMaximumSize(QSize(16777215, 28))
        self.btn_save_data.setFont(font)
        self.btn_save_data.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.btn_save_data)

        self.btn_save_Hist = QPushButton(MenuBar)
        self.btn_save_Hist.setObjectName(u"btn_save_Hist")
        self.btn_save_Hist.setEnabled(False)
        sizePolicy.setHeightForWidth(self.btn_save_Hist.sizePolicy().hasHeightForWidth())
        self.btn_save_Hist.setSizePolicy(sizePolicy)
        self.btn_save_Hist.setMinimumSize(QSize(0, 28))
        self.btn_save_Hist.setMaximumSize(QSize(16777215, 28))
        self.btn_save_Hist.setFont(font)
        self.btn_save_Hist.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.btn_save_Hist)

        self.horizontalSpacer_file = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_file)

        self.btn_reset_view = QPushButton(MenuBar)
        self.btn_reset_view.setObjectName(u"btn_reset_view")
        sizePolicy.setHeightForWidth(self.btn_reset_view.sizePolicy().hasHeightForWidth())
        self.btn_reset_view.setSizePolicy(sizePolicy)
        self.btn_reset_view.setMinimumSize(QSize(0, 28))
        self.btn_reset_view.setMaximumSize(QSize(16777215, 28))
        self.btn_reset_view.setFont(font)

        self.horizontalLayout.addWidget(self.btn_reset_view)

        self.btn_zoom_out = QPushButton(MenuBar)
        self.btn_zoom_out.setObjectName(u"btn_zoom_out")
        sizePolicy.setHeightForWidth(self.btn_zoom_out.sizePolicy().hasHeightForWidth())
        self.btn_zoom_out.setSizePolicy(sizePolicy)
        self.btn_zoom_out.setMinimumSize(QSize(0, 28))
        self.btn_zoom_out.setMaximumSize(QSize(16777215, 28))
        self.btn_zoom_out.setFont(font)

        self.horizontalLayout.addWidget(self.btn_zoom_out)

        self.slider_zoom = QSlider(MenuBar)
        self.slider_zoom.setObjectName(u"slider_zoom")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.slider_zoom.sizePolicy().hasHeightForWidth())
        self.slider_zoom.setSizePolicy(sizePolicy1)
        self.slider_zoom.setMinimumSize(QSize(0, 40))
        self.slider_zoom.setMaximumSize(QSize(16777215, 40))
        self.slider_zoom.setMouseTracking(False)
        self.slider_zoom.setMaximum(100)
        self.slider_zoom.setValue(8)
        self.slider_zoom.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.slider_zoom)

        self.label_ratio = QLabel(MenuBar)
        self.label_ratio.setObjectName(u"label_ratio")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_ratio.sizePolicy().hasHeightForWidth())
        self.label_ratio.setSizePolicy(sizePolicy2)
        self.label_ratio.setMinimumSize(QSize(0, 28))
        self.label_ratio.setMaximumSize(QSize(16777215, 28))
        font1 = QFont()
        font1.setPointSize(16)
        self.label_ratio.setFont(font1)

        self.horizontalLayout.addWidget(self.label_ratio)

        self.btn_zoom_in = QPushButton(MenuBar)
        self.btn_zoom_in.setObjectName(u"btn_zoom_in")
        sizePolicy.setHeightForWidth(self.btn_zoom_in.sizePolicy().hasHeightForWidth())
        self.btn_zoom_in.setSizePolicy(sizePolicy)
        self.btn_zoom_in.setMinimumSize(QSize(0, 28))
        self.btn_zoom_in.setMaximumSize(QSize(16777215, 28))
        self.btn_zoom_in.setFont(font)

        self.horizontalLayout.addWidget(self.btn_zoom_in)


        self.retranslateUi(MenuBar)

        QMetaObject.connectSlotsByName(MenuBar)
    # setupUi

    def retranslateUi(self, MenuBar):
        MenuBar.setWindowTitle(QCoreApplication.translate("MenuBar", u"Form", None))
        self.btn_open_img.setText(QCoreApplication.translate("MenuBar", u"Open Image", None))
        self.btn_save_data.setText(QCoreApplication.translate("MenuBar", u"Save Data", None))
        self.btn_save_Hist.setText(QCoreApplication.translate("MenuBar", u"Save Histogram", None))
        self.btn_reset_view.setText(QCoreApplication.translate("MenuBar", u"Reset View", None))
        self.btn_zoom_out.setText(QCoreApplication.translate("MenuBar", u"Zoom Out", None))
        self.label_ratio.setText(QCoreApplication.translate("MenuBar", u"Ratio:100%", None))
        self.btn_zoom_in.setText(QCoreApplication.translate("MenuBar", u"Zoom In", None))
    # retranslateUi

