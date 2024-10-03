# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_ContentBar.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_ContentBar(object):
    def setupUi(self, ContentBar):
        if not ContentBar.objectName():
            ContentBar.setObjectName(u"ContentBar")
        ContentBar.resize(320, 751)
        ContentBar.setMinimumSize(QSize(320, 0))
        ContentBar.setMaximumSize(QSize(320, 16777215))
        self.parameter = QWidget(ContentBar)
        self.parameter.setObjectName(u"parameter")
        self.parameter.setGeometry(QRect(0, 0, 320, 764))
        self.parameter.setMinimumSize(QSize(320, 0))
        self.parameter.setMaximumSize(QSize(320, 16777215))
        self.parameter.setStyleSheet(u"border-color: rgb(255, 46, 52);")
        self.gridLayout = QGridLayout(self.parameter)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, -1, 5, -1)
        self.label_contours_fixed = QLabel(self.parameter)
        self.label_contours_fixed.setObjectName(u"label_contours_fixed")
        self.label_contours_fixed.setMinimumSize(QSize(180, 0))
        self.label_contours_fixed.setMaximumSize(QSize(180, 20))

        self.gridLayout.addWidget(self.label_contours_fixed, 19, 0, 1, 1)

        self.label_title_fixed = QLabel(self.parameter)
        self.label_title_fixed.setObjectName(u"label_title_fixed")
        self.label_title_fixed.setMinimumSize(QSize(180, 20))
        self.label_title_fixed.setMaximumSize(QSize(180, 20))

        self.gridLayout.addWidget(self.label_title_fixed, 7, 0, 1, 2)

        self.btn_show_mask = QPushButton(self.parameter)
        self.btn_show_mask.setObjectName(u"btn_show_mask")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_show_mask.sizePolicy().hasHeightForWidth())
        self.btn_show_mask.setSizePolicy(sizePolicy)
        self.btn_show_mask.setMinimumSize(QSize(92, 25))
        self.btn_show_mask.setMaximumSize(QSize(92, 25))

        self.gridLayout.addWidget(self.btn_show_mask, 4, 1, 1, 1)

        self.label_pixel_scale = QLabel(self.parameter)
        self.label_pixel_scale.setObjectName(u"label_pixel_scale")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_pixel_scale.sizePolicy().hasHeightForWidth())
        self.label_pixel_scale.setSizePolicy(sizePolicy1)
        self.label_pixel_scale.setMinimumSize(QSize(90, 20))
        self.label_pixel_scale.setMaximumSize(QSize(90, 20))

        self.gridLayout.addWidget(self.label_pixel_scale, 11, 0, 1, 1)

        self.labe_select_roi_fixed = QLabel(self.parameter)
        self.labe_select_roi_fixed.setObjectName(u"labe_select_roi_fixed")
        self.labe_select_roi_fixed.setMinimumSize(QSize(180, 20))
        self.labe_select_roi_fixed.setMaximumSize(QSize(180, 20))

        self.gridLayout.addWidget(self.labe_select_roi_fixed, 13, 0, 1, 1)

        self.label_objectlength_fixed = QLabel(self.parameter)
        self.label_objectlength_fixed.setObjectName(u"label_objectlength_fixed")
        sizePolicy1.setHeightForWidth(self.label_objectlength_fixed.sizePolicy().hasHeightForWidth())
        self.label_objectlength_fixed.setSizePolicy(sizePolicy1)
        self.label_objectlength_fixed.setMinimumSize(QSize(90, 20))
        self.label_objectlength_fixed.setMaximumSize(QSize(90, 20))
        self.label_objectlength_fixed.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_objectlength_fixed, 9, 0, 1, 1)

        self.label_objectlength_fixed_2 = QLabel(self.parameter)
        self.label_objectlength_fixed_2.setObjectName(u"label_objectlength_fixed_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_objectlength_fixed_2.sizePolicy().hasHeightForWidth())
        self.label_objectlength_fixed_2.setSizePolicy(sizePolicy2)
        self.label_objectlength_fixed_2.setMinimumSize(QSize(70, 20))
        self.label_objectlength_fixed_2.setMaximumSize(QSize(70, 20))
        self.label_objectlength_fixed_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_objectlength_fixed_2, 9, 2, 1, 1)

        self.lineEdit_pixel_scale_value = QLineEdit(self.parameter)
        self.lineEdit_pixel_scale_value.setObjectName(u"lineEdit_pixel_scale_value")
        sizePolicy.setHeightForWidth(self.lineEdit_pixel_scale_value.sizePolicy().hasHeightForWidth())
        self.lineEdit_pixel_scale_value.setSizePolicy(sizePolicy)
        self.lineEdit_pixel_scale_value.setMinimumSize(QSize(0, 25))
        self.lineEdit_pixel_scale_value.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_pixel_scale_value.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_pixel_scale_value, 11, 1, 1, 1)

        self.lineEdit_contours_value = QLineEdit(self.parameter)
        self.lineEdit_contours_value.setObjectName(u"lineEdit_contours_value")
        sizePolicy.setHeightForWidth(self.lineEdit_contours_value.sizePolicy().hasHeightForWidth())
        self.lineEdit_contours_value.setSizePolicy(sizePolicy)
        self.lineEdit_contours_value.setMinimumSize(QSize(0, 25))
        self.lineEdit_contours_value.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_contours_value.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_contours_value, 20, 2, 1, 1)

        self.line_space1 = QFrame(self.parameter)
        self.line_space1.setObjectName(u"line_space1")
        self.line_space1.setMinimumSize(QSize(288, 1))
        self.line_space1.setMaximumSize(QSize(288, 1))
        self.line_space1.setAutoFillBackground(False)
        self.line_space1.setStyleSheet(u"background-color: rgb(113, 112, 111);")
        self.line_space1.setFrameShape(QFrame.Shape.HLine)
        self.line_space1.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_space1, 12, 0, 1, 1)

        self.btn_roi_analysis = QPushButton(self.parameter)
        self.btn_roi_analysis.setObjectName(u"btn_roi_analysis")
        sizePolicy.setHeightForWidth(self.btn_roi_analysis.sizePolicy().hasHeightForWidth())
        self.btn_roi_analysis.setSizePolicy(sizePolicy)
        self.btn_roi_analysis.setMinimumSize(QSize(92, 25))
        self.btn_roi_analysis.setMaximumSize(QSize(92, 25))
        font = QFont()
        font.setPointSize(12)
        self.btn_roi_analysis.setFont(font)

        self.gridLayout.addWidget(self.btn_roi_analysis, 21, 2, 1, 1)

        self.line_space3 = QFrame(self.parameter)
        self.line_space3.setObjectName(u"line_space3")
        self.line_space3.setMinimumSize(QSize(288, 1))
        self.line_space3.setMaximumSize(QSize(288, 1))
        self.line_space3.setAutoFillBackground(False)
        self.line_space3.setStyleSheet(u"background-color: rgb(113, 112, 111);")
        self.line_space3.setFrameShape(QFrame.Shape.HLine)
        self.line_space3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_space3, 6, 0, 1, 1)

        self.btn_refer_reset = QPushButton(self.parameter)
        self.btn_refer_reset.setObjectName(u"btn_refer_reset")
        sizePolicy.setHeightForWidth(self.btn_refer_reset.sizePolicy().hasHeightForWidth())
        self.btn_refer_reset.setSizePolicy(sizePolicy)
        self.btn_refer_reset.setMinimumSize(QSize(92, 25))
        self.btn_refer_reset.setMaximumSize(QSize(92, 25))
        self.btn_refer_reset.setFont(font)

        self.gridLayout.addWidget(self.btn_refer_reset, 7, 2, 1, 1)

        self.btn_show_image = QPushButton(self.parameter)
        self.btn_show_image.setObjectName(u"btn_show_image")
        sizePolicy.setHeightForWidth(self.btn_show_image.sizePolicy().hasHeightForWidth())
        self.btn_show_image.setSizePolicy(sizePolicy)
        self.btn_show_image.setMinimumSize(QSize(92, 25))
        self.btn_show_image.setMaximumSize(QSize(92, 25))
        self.btn_show_image.setFont(font)

        self.gridLayout.addWidget(self.btn_show_image, 4, 0, 1, 1)

        self.btn_change_mode = QPushButton(self.parameter)
        self.btn_change_mode.setObjectName(u"btn_change_mode")
        sizePolicy.setHeightForWidth(self.btn_change_mode.sizePolicy().hasHeightForWidth())
        self.btn_change_mode.setSizePolicy(sizePolicy)
        self.btn_change_mode.setMinimumSize(QSize(92, 25))
        self.btn_change_mode.setMaximumSize(QSize(92, 25))
        self.btn_change_mode.setFont(font)

        self.gridLayout.addWidget(self.btn_change_mode, 3, 2, 1, 1)

        self.label_objdect_ratio_fixed = QLabel(self.parameter)
        self.label_objdect_ratio_fixed.setObjectName(u"label_objdect_ratio_fixed")
        self.label_objdect_ratio_fixed.setMinimumSize(QSize(70, 20))
        self.label_objdect_ratio_fixed.setMaximumSize(QSize(70, 20))
        self.label_objdect_ratio_fixed.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_objdect_ratio_fixed, 11, 2, 1, 1)

        self.lineEdit_object_length = QLineEdit(self.parameter)
        self.lineEdit_object_length.setObjectName(u"lineEdit_object_length")
        sizePolicy.setHeightForWidth(self.lineEdit_object_length.sizePolicy().hasHeightForWidth())
        self.lineEdit_object_length.setSizePolicy(sizePolicy)
        self.lineEdit_object_length.setMinimumSize(QSize(0, 25))
        self.lineEdit_object_length.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_object_length.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_object_length, 9, 1, 1, 1)

        self.btn_refer_select = QPushButton(self.parameter)
        self.btn_refer_select.setObjectName(u"btn_refer_select")
        sizePolicy.setHeightForWidth(self.btn_refer_select.sizePolicy().hasHeightForWidth())
        self.btn_refer_select.setSizePolicy(sizePolicy)
        self.btn_refer_select.setMinimumSize(QSize(92, 25))
        self.btn_refer_select.setMaximumSize(QSize(92, 25))
        self.btn_refer_select.setFont(font)

        self.gridLayout.addWidget(self.btn_refer_select, 10, 0, 1, 1)

        self.checkBox_roi_reverse = QCheckBox(self.parameter)
        self.checkBox_roi_reverse.setObjectName(u"checkBox_roi_reverse")
        sizePolicy.setHeightForWidth(self.checkBox_roi_reverse.sizePolicy().hasHeightForWidth())
        self.checkBox_roi_reverse.setSizePolicy(sizePolicy)
        self.checkBox_roi_reverse.setMinimumSize(QSize(0, 25))
        self.checkBox_roi_reverse.setMaximumSize(QSize(16777215, 25))
        self.checkBox_roi_reverse.setCheckable(True)

        self.gridLayout.addWidget(self.checkBox_roi_reverse, 14, 0, 1, 1)

        self.label_show_image_fixed = QLabel(self.parameter)
        self.label_show_image_fixed.setObjectName(u"label_show_image_fixed")
        self.label_show_image_fixed.setMinimumSize(QSize(180, 20))
        self.label_show_image_fixed.setMaximumSize(QSize(180, 20))

        self.gridLayout.addWidget(self.label_show_image_fixed, 3, 0, 1, 1)

        self.btn_contours_find = QPushButton(self.parameter)
        self.btn_contours_find.setObjectName(u"btn_contours_find")
        self.btn_contours_find.setMinimumSize(QSize(92, 25))
        self.btn_contours_find.setMaximumSize(QSize(92, 25))

        self.gridLayout.addWidget(self.btn_contours_find, 21, 0, 1, 1)

        self.btn_refer_calculate = QPushButton(self.parameter)
        self.btn_refer_calculate.setObjectName(u"btn_refer_calculate")
        self.btn_refer_calculate.setEnabled(False)
        sizePolicy.setHeightForWidth(self.btn_refer_calculate.sizePolicy().hasHeightForWidth())
        self.btn_refer_calculate.setSizePolicy(sizePolicy)
        self.btn_refer_calculate.setMinimumSize(QSize(92, 25))
        self.btn_refer_calculate.setMaximumSize(QSize(92, 25))
        self.btn_refer_calculate.setFont(font)

        self.gridLayout.addWidget(self.btn_refer_calculate, 10, 2, 1, 1)

        self.btn_eraser = QPushButton(self.parameter)
        self.btn_eraser.setObjectName(u"btn_eraser")
        sizePolicy.setHeightForWidth(self.btn_eraser.sizePolicy().hasHeightForWidth())
        self.btn_eraser.setSizePolicy(sizePolicy)
        self.btn_eraser.setMinimumSize(QSize(92, 25))
        self.btn_eraser.setMaximumSize(QSize(92, 25))
        self.btn_eraser.setFont(font)

        self.gridLayout.addWidget(self.btn_eraser, 21, 1, 1, 1)

        self.btn_roi_reset = QPushButton(self.parameter)
        self.btn_roi_reset.setObjectName(u"btn_roi_reset")
        sizePolicy.setHeightForWidth(self.btn_roi_reset.sizePolicy().hasHeightForWidth())
        self.btn_roi_reset.setSizePolicy(sizePolicy)
        self.btn_roi_reset.setMinimumSize(QSize(92, 25))
        self.btn_roi_reset.setMaximumSize(QSize(92, 25))
        self.btn_roi_reset.setFont(font)

        self.gridLayout.addWidget(self.btn_roi_reset, 13, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 37, 1, 1, 1)

        self.label_contours_fixed2 = QLabel(self.parameter)
        self.label_contours_fixed2.setObjectName(u"label_contours_fixed2")
        self.label_contours_fixed2.setMinimumSize(QSize(180, 0))
        self.label_contours_fixed2.setMaximumSize(QSize(180, 20))

        self.gridLayout.addWidget(self.label_contours_fixed2, 20, 0, 1, 1)

        self.label_number_contours = QLabel(self.parameter)
        self.label_number_contours.setObjectName(u"label_number_contours")
        sizePolicy2.setHeightForWidth(self.label_number_contours.sizePolicy().hasHeightForWidth())
        self.label_number_contours.setSizePolicy(sizePolicy2)
        self.label_number_contours.setMinimumSize(QSize(70, 20))
        self.label_number_contours.setMaximumSize(QSize(70, 20))
        self.label_number_contours.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_number_contours, 19, 2, 1, 1)

        self.btn_roi_select = QPushButton(self.parameter)
        self.btn_roi_select.setObjectName(u"btn_roi_select")
        sizePolicy.setHeightForWidth(self.btn_roi_select.sizePolicy().hasHeightForWidth())
        self.btn_roi_select.setSizePolicy(sizePolicy)
        self.btn_roi_select.setMinimumSize(QSize(92, 25))
        self.btn_roi_select.setMaximumSize(QSize(92, 25))
        self.btn_roi_select.setFont(font)

        self.gridLayout.addWidget(self.btn_roi_select, 14, 2, 1, 1)

        self.btn_show_contours = QPushButton(self.parameter)
        self.btn_show_contours.setObjectName(u"btn_show_contours")
        sizePolicy.setHeightForWidth(self.btn_show_contours.sizePolicy().hasHeightForWidth())
        self.btn_show_contours.setSizePolicy(sizePolicy)
        self.btn_show_contours.setMinimumSize(QSize(92, 25))
        self.btn_show_contours.setMaximumSize(QSize(92, 25))

        self.gridLayout.addWidget(self.btn_show_contours, 4, 2, 1, 1)


        self.retranslateUi(ContentBar)

        QMetaObject.connectSlotsByName(ContentBar)
    # setupUi

    def retranslateUi(self, ContentBar):
        ContentBar.setWindowTitle(QCoreApplication.translate("ContentBar", u"Form", None))
        self.label_contours_fixed.setText(QCoreApplication.translate("ContentBar", u"Detected Contours", None))
        self.label_title_fixed.setText(QCoreApplication.translate("ContentBar", u"Physical Scale of the Image", None))
        self.btn_show_mask.setText(QCoreApplication.translate("ContentBar", u"Mask", None))
        self.label_pixel_scale.setText(QCoreApplication.translate("ContentBar", u"Pixel Scale:", None))
        self.labe_select_roi_fixed.setText(QCoreApplication.translate("ContentBar", u"Select Region of Interest", None))
        self.label_objectlength_fixed.setText(QCoreApplication.translate("ContentBar", u"Object length", None))
        self.label_objectlength_fixed_2.setText(QCoreApplication.translate("ContentBar", u" mm ", None))
        self.lineEdit_pixel_scale_value.setText("")
        self.lineEdit_contours_value.setText(QCoreApplication.translate("ContentBar", u"-1", None))
        self.btn_roi_analysis.setText(QCoreApplication.translate("ContentBar", u"Analysis", None))
        self.btn_refer_reset.setText(QCoreApplication.translate("ContentBar", u"Reset", None))
        self.btn_show_image.setText(QCoreApplication.translate("ContentBar", u"Image", None))
        self.btn_change_mode.setText(QCoreApplication.translate("ContentBar", u"Hist Mode", None))
        self.label_objdect_ratio_fixed.setText(QCoreApplication.translate("ContentBar", u"mm/pixel", None))
        self.lineEdit_object_length.setText("")
        self.btn_refer_select.setText(QCoreApplication.translate("ContentBar", u"Select", None))
        self.checkBox_roi_reverse.setText(QCoreApplication.translate("ContentBar", u"Reverse", None))
        self.label_show_image_fixed.setText(QCoreApplication.translate("ContentBar", u"View Mode", None))
        self.btn_contours_find.setText(QCoreApplication.translate("ContentBar", u"Find", None))
        self.btn_refer_calculate.setText(QCoreApplication.translate("ContentBar", u"Calculate", None))
        self.btn_eraser.setText(QCoreApplication.translate("ContentBar", u"Eraser", None))
        self.btn_roi_reset.setText(QCoreApplication.translate("ContentBar", u"Reset", None))
        self.label_contours_fixed2.setText(QCoreApplication.translate("ContentBar", u"Threshold Value", None))
        self.label_number_contours.setText(QCoreApplication.translate("ContentBar", u"0", None))
        self.btn_roi_select.setText(QCoreApplication.translate("ContentBar", u"Select ROI", None))
        self.btn_show_contours.setText(QCoreApplication.translate("ContentBar", u"Contours", None))
    # retranslateUi

