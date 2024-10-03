# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_HistogramBar.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QWidget)

class Ui_HistogramBar(object):
    def setupUi(self, HistogramBar):
        if not HistogramBar.objectName():
            HistogramBar.setObjectName(u"HistogramBar")
        HistogramBar.resize(320, 709)
        HistogramBar.setMinimumSize(QSize(320, 709))
        HistogramBar.setMaximumSize(QSize(320, 16777215))
        self.scrollArea = QScrollArea(HistogramBar)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 0, 320, 699))
        self.scrollArea.setMinimumSize(QSize(320, 699))
        self.scrollArea.setMaximumSize(QSize(320, 699))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 320, 900))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(320, 900))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(320, 900))
        self.parameter = QWidget(self.scrollAreaWidgetContents)
        self.parameter.setObjectName(u"parameter")
        self.parameter.setGeometry(QRect(0, 0, 300, 831))
        self.parameter.setMinimumSize(QSize(300, 831))
        self.parameter.setMaximumSize(QSize(300, 16777215))
        self.parameter.setStyleSheet(u"border-color: rgb(255, 46, 52);")
        self.gridLayout_2 = QGridLayout(self.parameter)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, -1, 5, -1)
        self.label_x_axis_min_fixed = QLabel(self.parameter)
        self.label_x_axis_min_fixed.setObjectName(u"label_x_axis_min_fixed")
        self.label_x_axis_min_fixed.setMinimumSize(QSize(90, 0))
        self.label_x_axis_min_fixed.setMaximumSize(QSize(90, 16777215))

        self.gridLayout_2.addWidget(self.label_x_axis_min_fixed, 47, 0, 1, 1)

        self.btn_load_data2 = QPushButton(self.parameter)
        self.btn_load_data2.setObjectName(u"btn_load_data2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_load_data2.sizePolicy().hasHeightForWidth())
        self.btn_load_data2.setSizePolicy(sizePolicy)
        self.btn_load_data2.setMinimumSize(QSize(92, 25))
        self.btn_load_data2.setMaximumSize(QSize(92, 25))
        font = QFont()
        font.setPointSize(12)
        self.btn_load_data2.setFont(font)

        self.gridLayout_2.addWidget(self.btn_load_data2, 34, 0, 1, 1)

        self.label_showhist_fixed = QLabel(self.parameter)
        self.label_showhist_fixed.setObjectName(u"label_showhist_fixed")
        self.label_showhist_fixed.setMinimumSize(QSize(90, 20))
        self.label_showhist_fixed.setMaximumSize(QSize(90, 20))

        self.gridLayout_2.addWidget(self.label_showhist_fixed, 43, 0, 1, 1)

        self.label_show_image_fixed = QLabel(self.parameter)
        self.label_show_image_fixed.setObjectName(u"label_show_image_fixed")
        self.label_show_image_fixed.setMinimumSize(QSize(180, 20))
        self.label_show_image_fixed.setMaximumSize(QSize(180, 20))

        self.gridLayout_2.addWidget(self.label_show_image_fixed, 2, 0, 1, 1)

        self.lineEdit_xaxis_min_value = QLineEdit(self.parameter)
        self.lineEdit_xaxis_min_value.setObjectName(u"lineEdit_xaxis_min_value")
        sizePolicy.setHeightForWidth(self.lineEdit_xaxis_min_value.sizePolicy().hasHeightForWidth())
        self.lineEdit_xaxis_min_value.setSizePolicy(sizePolicy)
        self.lineEdit_xaxis_min_value.setMinimumSize(QSize(0, 25))
        self.lineEdit_xaxis_min_value.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_xaxis_min_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_xaxis_min_value, 47, 1, 1, 1)

        self.lineEdit_data2_name = QLineEdit(self.parameter)
        self.lineEdit_data2_name.setObjectName(u"lineEdit_data2_name")
        self.lineEdit_data2_name.setMinimumSize(QSize(180, 0))
        self.lineEdit_data2_name.setMaximumSize(QSize(180, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_data2_name, 33, 1, 1, 2)

        self.btn_clear_data1 = QPushButton(self.parameter)
        self.btn_clear_data1.setObjectName(u"btn_clear_data1")
        sizePolicy.setHeightForWidth(self.btn_clear_data1.sizePolicy().hasHeightForWidth())
        self.btn_clear_data1.setSizePolicy(sizePolicy)
        self.btn_clear_data1.setMinimumSize(QSize(92, 25))
        self.btn_clear_data1.setMaximumSize(QSize(92, 25))
        self.btn_clear_data1.setFont(font)

        self.gridLayout_2.addWidget(self.btn_clear_data1, 28, 2, 1, 1)

        self.label_data1_min_value = QLabel(self.parameter)
        self.label_data1_min_value.setObjectName(u"label_data1_min_value")

        self.gridLayout_2.addWidget(self.label_data1_min_value, 32, 0, 1, 1)

        self.label_title_fixed_3 = QLabel(self.parameter)
        self.label_title_fixed_3.setObjectName(u"label_title_fixed_3")
        self.label_title_fixed_3.setMinimumSize(QSize(150, 20))
        self.label_title_fixed_3.setMaximumSize(QSize(150, 20))

        self.gridLayout_2.addWidget(self.label_title_fixed_3, 45, 0, 1, 1)

        self.checkBox_show_std = QCheckBox(self.parameter)
        self.checkBox_show_std.setObjectName(u"checkBox_show_std")
        self.checkBox_show_std.setMinimumSize(QSize(90, 0))
        self.checkBox_show_std.setMaximumSize(QSize(90, 16777215))
        self.checkBox_show_std.setChecked(False)

        self.gridLayout_2.addWidget(self.checkBox_show_std, 54, 2, 1, 1)

        self.label_data1_avg = QLabel(self.parameter)
        self.label_data1_avg.setObjectName(u"label_data1_avg")
        self.label_data1_avg.setMinimumSize(QSize(80, 20))
        self.label_data1_avg.setMaximumSize(QSize(80, 20))

        self.gridLayout_2.addWidget(self.label_data1_avg, 29, 0, 1, 1)

        self.label_data1_max_value = QLabel(self.parameter)
        self.label_data1_max_value.setObjectName(u"label_data1_max_value")

        self.gridLayout_2.addWidget(self.label_data1_max_value, 32, 1, 1, 1)

        self.label_show_avg_fixed = QLabel(self.parameter)
        self.label_show_avg_fixed.setObjectName(u"label_show_avg_fixed")
        self.label_show_avg_fixed.setMinimumSize(QSize(170, 20))
        self.label_show_avg_fixed.setMaximumSize(QSize(170, 20))

        self.gridLayout_2.addWidget(self.label_show_avg_fixed, 52, 0, 1, 1)

        self.label_data1_avg_value = QLabel(self.parameter)
        self.label_data1_avg_value.setObjectName(u"label_data1_avg_value")

        self.gridLayout_2.addWidget(self.label_data1_avg_value, 30, 0, 1, 1)

        self.label_data2_min_value = QLabel(self.parameter)
        self.label_data2_min_value.setObjectName(u"label_data2_min_value")

        self.gridLayout_2.addWidget(self.label_data2_min_value, 38, 0, 1, 1)

        self.label_data2_avg = QLabel(self.parameter)
        self.label_data2_avg.setObjectName(u"label_data2_avg")
        self.label_data2_avg.setMinimumSize(QSize(80, 20))
        self.label_data2_avg.setMaximumSize(QSize(80, 20))

        self.gridLayout_2.addWidget(self.label_data2_avg, 35, 0, 1, 1)

        self.label_data1_max = QLabel(self.parameter)
        self.label_data1_max.setObjectName(u"label_data1_max")
        self.label_data1_max.setMinimumSize(QSize(80, 20))
        self.label_data1_max.setMaximumSize(QSize(80, 20))

        self.gridLayout_2.addWidget(self.label_data1_max, 31, 1, 1, 1)

        self.label_x_axis_min_unit = QLabel(self.parameter)
        self.label_x_axis_min_unit.setObjectName(u"label_x_axis_min_unit")

        self.gridLayout_2.addWidget(self.label_x_axis_min_unit, 47, 2, 1, 1)

        self.label_data2_median_value = QLabel(self.parameter)
        self.label_data2_median_value.setObjectName(u"label_data2_median_value")

        self.gridLayout_2.addWidget(self.label_data2_median_value, 36, 1, 1, 1)

        self.label_data1_std = QLabel(self.parameter)
        self.label_data1_std.setObjectName(u"label_data1_std")
        self.label_data1_std.setMinimumSize(QSize(80, 20))
        self.label_data1_std.setMaximumSize(QSize(80, 20))

        self.gridLayout_2.addWidget(self.label_data1_std, 29, 2, 1, 1)

        self.label_x_axis_max_unit = QLabel(self.parameter)
        self.label_x_axis_max_unit.setObjectName(u"label_x_axis_max_unit")

        self.gridLayout_2.addWidget(self.label_x_axis_max_unit, 51, 2, 1, 1)

        self.label_data2_avg_value = QLabel(self.parameter)
        self.label_data2_avg_value.setObjectName(u"label_data2_avg_value")

        self.gridLayout_2.addWidget(self.label_data2_avg_value, 36, 0, 1, 1)

        self.label_show_cumulative_fixed = QLabel(self.parameter)
        self.label_show_cumulative_fixed.setObjectName(u"label_show_cumulative_fixed")
        self.label_show_cumulative_fixed.setMinimumSize(QSize(170, 20))
        self.label_show_cumulative_fixed.setMaximumSize(QSize(170, 20))

        self.gridLayout_2.addWidget(self.label_show_cumulative_fixed, 55, 0, 1, 1)

        self.label_x_axis_spacing_fixed = QLabel(self.parameter)
        self.label_x_axis_spacing_fixed.setObjectName(u"label_x_axis_spacing_fixed")
        self.label_x_axis_spacing_fixed.setMinimumSize(QSize(90, 0))
        self.label_x_axis_spacing_fixed.setMaximumSize(QSize(90, 16777215))

        self.gridLayout_2.addWidget(self.label_x_axis_spacing_fixed, 46, 0, 1, 1)

        self.label_data1_min = QLabel(self.parameter)
        self.label_data1_min.setObjectName(u"label_data1_min")
        self.label_data1_min.setMinimumSize(QSize(80, 20))
        self.label_data1_min.setMaximumSize(QSize(80, 20))

        self.gridLayout_2.addWidget(self.label_data1_min, 31, 0, 1, 1)

        self.label_show_std_fixed = QLabel(self.parameter)
        self.label_show_std_fixed.setObjectName(u"label_show_std_fixed")
        self.label_show_std_fixed.setMinimumSize(QSize(170, 20))
        self.label_show_std_fixed.setMaximumSize(QSize(170, 20))

        self.gridLayout_2.addWidget(self.label_show_std_fixed, 54, 0, 1, 1)

        self.lineEdit_show_D1_value = QLineEdit(self.parameter)
        self.lineEdit_show_D1_value.setObjectName(u"lineEdit_show_D1_value")
        sizePolicy.setHeightForWidth(self.lineEdit_show_D1_value.sizePolicy().hasHeightForWidth())
        self.lineEdit_show_D1_value.setSizePolicy(sizePolicy)
        self.lineEdit_show_D1_value.setMinimumSize(QSize(0, 25))
        self.lineEdit_show_D1_value.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_show_D1_value.setMaxLength(100)
        self.lineEdit_show_D1_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_show_D1_value, 61, 0, 1, 1)

        self.label_data2_max_value = QLabel(self.parameter)
        self.label_data2_max_value.setObjectName(u"label_data2_max_value")

        self.gridLayout_2.addWidget(self.label_data2_max_value, 38, 1, 1, 1)

        self.checkBox_show_data1 = QCheckBox(self.parameter)
        self.checkBox_show_data1.setObjectName(u"checkBox_show_data1")
        self.checkBox_show_data1.setMinimumSize(QSize(100, 0))
        self.checkBox_show_data1.setMaximumSize(QSize(100, 16777215))
        self.checkBox_show_data1.setChecked(False)

        self.gridLayout_2.addWidget(self.checkBox_show_data1, 42, 0, 1, 1)

        self.label_data1_total = QLabel(self.parameter)
        self.label_data1_total.setObjectName(u"label_data1_total")
        self.label_data1_total.setMinimumSize(QSize(80, 20))
        self.label_data1_total.setMaximumSize(QSize(80, 20))

        self.gridLayout_2.addWidget(self.label_data1_total, 31, 2, 1, 1)

        self.line_space1_2 = QFrame(self.parameter)
        self.line_space1_2.setObjectName(u"line_space1_2")
        self.line_space1_2.setMinimumSize(QSize(288, 1))
        self.line_space1_2.setMaximumSize(QSize(288, 1))
        self.line_space1_2.setAutoFillBackground(False)
        self.line_space1_2.setStyleSheet(u"background-color: rgb(113, 112, 111);")
        self.line_space1_2.setFrameShape(QFrame.Shape.HLine)
        self.line_space1_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_space1_2, 5, 0, 1, 1)

        self.btn_update_histogram = QPushButton(self.parameter)
        self.btn_update_histogram.setObjectName(u"btn_update_histogram")
        sizePolicy.setHeightForWidth(self.btn_update_histogram.sizePolicy().hasHeightForWidth())
        self.btn_update_histogram.setSizePolicy(sizePolicy)
        self.btn_update_histogram.setMinimumSize(QSize(92, 25))
        self.btn_update_histogram.setMaximumSize(QSize(92, 25))
        self.btn_update_histogram.setFont(font)

        self.gridLayout_2.addWidget(self.btn_update_histogram, 41, 2, 1, 1)

        self.label_data1_median = QLabel(self.parameter)
        self.label_data1_median.setObjectName(u"label_data1_median")
        self.label_data1_median.setMinimumSize(QSize(80, 20))
        self.label_data1_median.setMaximumSize(QSize(80, 20))

        self.gridLayout_2.addWidget(self.label_data1_median, 29, 1, 1, 1)

        self.line_space2_2 = QFrame(self.parameter)
        self.line_space2_2.setObjectName(u"line_space2_2")
        self.line_space2_2.setMinimumSize(QSize(288, 1))
        self.line_space2_2.setMaximumSize(QSize(288, 1))
        self.line_space2_2.setAutoFillBackground(False)
        self.line_space2_2.setStyleSheet(u"background-color: rgb(113, 112, 111);")
        self.line_space2_2.setFrameShape(QFrame.Shape.HLine)
        self.line_space2_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_space2_2, 40, 0, 1, 1)

        self.label_data2_std = QLabel(self.parameter)
        self.label_data2_std.setObjectName(u"label_data2_std")
        self.label_data2_std.setMinimumSize(QSize(80, 20))
        self.label_data2_std.setMaximumSize(QSize(80, 20))

        self.gridLayout_2.addWidget(self.label_data2_std, 35, 2, 1, 1)

        self.checkBox_show_median = QCheckBox(self.parameter)
        self.checkBox_show_median.setObjectName(u"checkBox_show_median")
        self.checkBox_show_median.setMinimumSize(QSize(90, 0))
        self.checkBox_show_median.setMaximumSize(QSize(90, 16777215))
        self.checkBox_show_median.setChecked(False)

        self.gridLayout_2.addWidget(self.checkBox_show_median, 53, 2, 1, 1)

        self.label_x_axis_max_fixed = QLabel(self.parameter)
        self.label_x_axis_max_fixed.setObjectName(u"label_x_axis_max_fixed")
        self.label_x_axis_max_fixed.setMinimumSize(QSize(90, 0))
        self.label_x_axis_max_fixed.setMaximumSize(QSize(90, 16777215))

        self.gridLayout_2.addWidget(self.label_x_axis_max_fixed, 51, 0, 1, 1)

        self.label_data2_max = QLabel(self.parameter)
        self.label_data2_max.setObjectName(u"label_data2_max")
        self.label_data2_max.setMinimumSize(QSize(80, 20))
        self.label_data2_max.setMaximumSize(QSize(80, 20))

        self.gridLayout_2.addWidget(self.label_data2_max, 37, 1, 1, 1)

        self.lineEdit_data1_name = QLineEdit(self.parameter)
        self.lineEdit_data1_name.setObjectName(u"lineEdit_data1_name")
        self.lineEdit_data1_name.setMinimumSize(QSize(180, 0))
        self.lineEdit_data1_name.setMaximumSize(QSize(180, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_data1_name, 27, 1, 1, 2)

        self.btn_clear_data2 = QPushButton(self.parameter)
        self.btn_clear_data2.setObjectName(u"btn_clear_data2")
        sizePolicy.setHeightForWidth(self.btn_clear_data2.sizePolicy().hasHeightForWidth())
        self.btn_clear_data2.setSizePolicy(sizePolicy)
        self.btn_clear_data2.setMinimumSize(QSize(92, 25))
        self.btn_clear_data2.setMaximumSize(QSize(92, 25))
        self.btn_clear_data2.setFont(font)

        self.gridLayout_2.addWidget(self.btn_clear_data2, 34, 2, 1, 1)

        self.label_data2_total = QLabel(self.parameter)
        self.label_data2_total.setObjectName(u"label_data2_total")
        self.label_data2_total.setMinimumSize(QSize(80, 20))
        self.label_data2_total.setMaximumSize(QSize(80, 20))

        self.gridLayout_2.addWidget(self.label_data2_total, 37, 2, 1, 1)

        self.lineEdit_xaxis_max_value = QLineEdit(self.parameter)
        self.lineEdit_xaxis_max_value.setObjectName(u"lineEdit_xaxis_max_value")
        sizePolicy.setHeightForWidth(self.lineEdit_xaxis_max_value.sizePolicy().hasHeightForWidth())
        self.lineEdit_xaxis_max_value.setSizePolicy(sizePolicy)
        self.lineEdit_xaxis_max_value.setMinimumSize(QSize(0, 25))
        self.lineEdit_xaxis_max_value.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_xaxis_max_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_xaxis_max_value, 51, 1, 1, 1)

        self.label_data2_median = QLabel(self.parameter)
        self.label_data2_median.setObjectName(u"label_data2_median")
        self.label_data2_median.setMinimumSize(QSize(80, 20))
        self.label_data2_median.setMaximumSize(QSize(80, 20))

        self.gridLayout_2.addWidget(self.label_data2_median, 35, 1, 1, 1)

        self.label_data2_total_value = QLabel(self.parameter)
        self.label_data2_total_value.setObjectName(u"label_data2_total_value")

        self.gridLayout_2.addWidget(self.label_data2_total_value, 38, 2, 1, 1)

        self.checkBox_show_data2 = QCheckBox(self.parameter)
        self.checkBox_show_data2.setObjectName(u"checkBox_show_data2")
        self.checkBox_show_data2.setMinimumSize(QSize(100, 0))
        self.checkBox_show_data2.setMaximumSize(QSize(100, 16777215))
        self.checkBox_show_data2.setChecked(False)

        self.gridLayout_2.addWidget(self.checkBox_show_data2, 42, 1, 1, 1)

        self.label_data1_name = QLabel(self.parameter)
        self.label_data1_name.setObjectName(u"label_data1_name")

        self.gridLayout_2.addWidget(self.label_data1_name, 27, 0, 1, 1)

        self.label_data1_std_value = QLabel(self.parameter)
        self.label_data1_std_value.setObjectName(u"label_data1_std_value")

        self.gridLayout_2.addWidget(self.label_data1_std_value, 30, 2, 1, 1)

        self.label_data2_name = QLabel(self.parameter)
        self.label_data2_name.setObjectName(u"label_data2_name")

        self.gridLayout_2.addWidget(self.label_data2_name, 33, 0, 1, 1)

        self.label_show_median_fixed = QLabel(self.parameter)
        self.label_show_median_fixed.setObjectName(u"label_show_median_fixed")
        self.label_show_median_fixed.setMinimumSize(QSize(170, 20))
        self.label_show_median_fixed.setMaximumSize(QSize(170, 20))

        self.gridLayout_2.addWidget(self.label_show_median_fixed, 53, 0, 1, 1)

        self.label_data1_median_value = QLabel(self.parameter)
        self.label_data1_median_value.setObjectName(u"label_data1_median_value")

        self.gridLayout_2.addWidget(self.label_data1_median_value, 30, 1, 1, 1)

        self.btn_load_data1 = QPushButton(self.parameter)
        self.btn_load_data1.setObjectName(u"btn_load_data1")
        sizePolicy.setHeightForWidth(self.btn_load_data1.sizePolicy().hasHeightForWidth())
        self.btn_load_data1.setSizePolicy(sizePolicy)
        self.btn_load_data1.setMinimumSize(QSize(92, 25))
        self.btn_load_data1.setMaximumSize(QSize(92, 25))
        self.btn_load_data1.setFont(font)

        self.gridLayout_2.addWidget(self.btn_load_data1, 28, 0, 1, 1)

        self.checkBox_show_avg = QCheckBox(self.parameter)
        self.checkBox_show_avg.setObjectName(u"checkBox_show_avg")
        self.checkBox_show_avg.setMinimumSize(QSize(90, 0))
        self.checkBox_show_avg.setMaximumSize(QSize(90, 16777215))
        self.checkBox_show_avg.setChecked(False)

        self.gridLayout_2.addWidget(self.checkBox_show_avg, 52, 2, 1, 1)

        self.label_data1_total_value = QLabel(self.parameter)
        self.label_data1_total_value.setObjectName(u"label_data1_total_value")

        self.gridLayout_2.addWidget(self.label_data1_total_value, 32, 2, 1, 1)

        self.checkBox_show_cumulative = QCheckBox(self.parameter)
        self.checkBox_show_cumulative.setObjectName(u"checkBox_show_cumulative")
        self.checkBox_show_cumulative.setMinimumSize(QSize(90, 0))
        self.checkBox_show_cumulative.setMaximumSize(QSize(90, 16777215))
        self.checkBox_show_cumulative.setChecked(True)

        self.gridLayout_2.addWidget(self.checkBox_show_cumulative, 55, 2, 1, 1)

        self.checkBox_show_D2 = QCheckBox(self.parameter)
        self.checkBox_show_D2.setObjectName(u"checkBox_show_D2")

        self.gridLayout_2.addWidget(self.checkBox_show_D2, 60, 1, 1, 1)

        self.btn_change_mode = QPushButton(self.parameter)
        self.btn_change_mode.setObjectName(u"btn_change_mode")
        sizePolicy.setHeightForWidth(self.btn_change_mode.sizePolicy().hasHeightForWidth())
        self.btn_change_mode.setSizePolicy(sizePolicy)
        self.btn_change_mode.setMinimumSize(QSize(92, 25))
        self.btn_change_mode.setMaximumSize(QSize(92, 25))
        self.btn_change_mode.setFont(font)

        self.gridLayout_2.addWidget(self.btn_change_mode, 2, 2, 1, 1)

        self.lineEdit_show_D2_value = QLineEdit(self.parameter)
        self.lineEdit_show_D2_value.setObjectName(u"lineEdit_show_D2_value")
        sizePolicy.setHeightForWidth(self.lineEdit_show_D2_value.sizePolicy().hasHeightForWidth())
        self.lineEdit_show_D2_value.setSizePolicy(sizePolicy)
        self.lineEdit_show_D2_value.setMinimumSize(QSize(0, 25))
        self.lineEdit_show_D2_value.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_show_D2_value.setMaxLength(100)
        self.lineEdit_show_D2_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_show_D2_value, 61, 1, 1, 1)

        self.label_showinfo_fixed = QLabel(self.parameter)
        self.label_showinfo_fixed.setObjectName(u"label_showinfo_fixed")
        self.label_showinfo_fixed.setMinimumSize(QSize(90, 20))
        self.label_showinfo_fixed.setMaximumSize(QSize(90, 20))

        self.gridLayout_2.addWidget(self.label_showinfo_fixed, 6, 0, 1, 1)

        self.label_data2_min = QLabel(self.parameter)
        self.label_data2_min.setObjectName(u"label_data2_min")
        self.label_data2_min.setMinimumSize(QSize(80, 20))
        self.label_data2_min.setMaximumSize(QSize(80, 20))

        self.gridLayout_2.addWidget(self.label_data2_min, 37, 0, 1, 1)

        self.label_histogram_fixed = QLabel(self.parameter)
        self.label_histogram_fixed.setObjectName(u"label_histogram_fixed")
        self.label_histogram_fixed.setMinimumSize(QSize(150, 20))
        self.label_histogram_fixed.setMaximumSize(QSize(150, 20))

        self.gridLayout_2.addWidget(self.label_histogram_fixed, 41, 0, 1, 1)

        self.label_data2_std_value = QLabel(self.parameter)
        self.label_data2_std_value.setObjectName(u"label_data2_std_value")

        self.gridLayout_2.addWidget(self.label_data2_std_value, 36, 2, 1, 1)

        self.checkBox_show_D3 = QCheckBox(self.parameter)
        self.checkBox_show_D3.setObjectName(u"checkBox_show_D3")

        self.gridLayout_2.addWidget(self.checkBox_show_D3, 60, 2, 1, 1)

        self.comboBox_show_info_type = QComboBox(self.parameter)
        self.comboBox_show_info_type.addItem("")
        self.comboBox_show_info_type.addItem("")
        self.comboBox_show_info_type.setObjectName(u"comboBox_show_info_type")
        sizePolicy.setHeightForWidth(self.comboBox_show_info_type.sizePolicy().hasHeightForWidth())
        self.comboBox_show_info_type.setSizePolicy(sizePolicy)
        self.comboBox_show_info_type.setMinimumSize(QSize(90, 25))
        self.comboBox_show_info_type.setMaximumSize(QSize(90, 25))
        self.comboBox_show_info_type.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_show_info_type.setMinimumContentsLength(6)

        self.gridLayout_2.addWidget(self.comboBox_show_info_type, 6, 1, 1, 1)

        self.lineEdit_show_D3_value = QLineEdit(self.parameter)
        self.lineEdit_show_D3_value.setObjectName(u"lineEdit_show_D3_value")
        sizePolicy.setHeightForWidth(self.lineEdit_show_D3_value.sizePolicy().hasHeightForWidth())
        self.lineEdit_show_D3_value.setSizePolicy(sizePolicy)
        self.lineEdit_show_D3_value.setMinimumSize(QSize(0, 25))
        self.lineEdit_show_D3_value.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_show_D3_value.setMaxLength(100)
        self.lineEdit_show_D3_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_show_D3_value, 61, 2, 1, 1)

        self.lineEdit_xaxis_spacing_value = QLineEdit(self.parameter)
        self.lineEdit_xaxis_spacing_value.setObjectName(u"lineEdit_xaxis_spacing_value")
        sizePolicy.setHeightForWidth(self.lineEdit_xaxis_spacing_value.sizePolicy().hasHeightForWidth())
        self.lineEdit_xaxis_spacing_value.setSizePolicy(sizePolicy)
        self.lineEdit_xaxis_spacing_value.setMinimumSize(QSize(0, 25))
        self.lineEdit_xaxis_spacing_value.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_xaxis_spacing_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_xaxis_spacing_value, 46, 1, 1, 1)

        self.comboBox_show_hist_type = QComboBox(self.parameter)
        self.comboBox_show_hist_type.addItem("")
        self.comboBox_show_hist_type.addItem("")
        self.comboBox_show_hist_type.setObjectName(u"comboBox_show_hist_type")
        sizePolicy.setHeightForWidth(self.comboBox_show_hist_type.sizePolicy().hasHeightForWidth())
        self.comboBox_show_hist_type.setSizePolicy(sizePolicy)
        self.comboBox_show_hist_type.setMinimumSize(QSize(110, 25))
        self.comboBox_show_hist_type.setMaximumSize(QSize(110, 25))
        self.comboBox_show_hist_type.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_show_hist_type.setMinimumContentsLength(6)

        self.gridLayout_2.addWidget(self.comboBox_show_hist_type, 43, 1, 1, 1)

        self.checkBox_show_D1 = QCheckBox(self.parameter)
        self.checkBox_show_D1.setObjectName(u"checkBox_show_D1")

        self.gridLayout_2.addWidget(self.checkBox_show_D1, 60, 0, 1, 1)

        self.label_x_axis_spacing_unit = QLabel(self.parameter)
        self.label_x_axis_spacing_unit.setObjectName(u"label_x_axis_spacing_unit")

        self.gridLayout_2.addWidget(self.label_x_axis_spacing_unit, 46, 2, 1, 1)

        self.label_data_unit = QLabel(self.parameter)
        self.label_data_unit.setObjectName(u"label_data_unit")
        self.label_data_unit.setMinimumSize(QSize(50, 0))
        self.label_data_unit.setMaximumSize(QSize(50, 16777215))
        self.label_data_unit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_data_unit, 6, 2, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(HistogramBar)

        QMetaObject.connectSlotsByName(HistogramBar)
    # setupUi

    def retranslateUi(self, HistogramBar):
        HistogramBar.setWindowTitle(QCoreApplication.translate("HistogramBar", u"Form", None))
        self.label_x_axis_min_fixed.setText(QCoreApplication.translate("HistogramBar", u"MIN value:", None))
        self.btn_load_data2.setText(QCoreApplication.translate("HistogramBar", u"Load Data2", None))
        self.label_showhist_fixed.setText(QCoreApplication.translate("HistogramBar", u"Hist Type", None))
        self.label_show_image_fixed.setText(QCoreApplication.translate("HistogramBar", u"Histogram Mode", None))
        self.lineEdit_xaxis_min_value.setText(QCoreApplication.translate("HistogramBar", u"-1", None))
        self.lineEdit_data2_name.setText("")
        self.btn_clear_data1.setText(QCoreApplication.translate("HistogramBar", u" Clear Data1", None))
        self.label_data1_min_value.setText(QCoreApplication.translate("HistogramBar", u"-1", None))
        self.label_title_fixed_3.setText(QCoreApplication.translate("HistogramBar", u"X-axis", None))
        self.checkBox_show_std.setText(QCoreApplication.translate("HistogramBar", u"Show", None))
        self.label_data1_avg.setText(QCoreApplication.translate("HistogramBar", u"Average ", None))
        self.label_data1_max_value.setText(QCoreApplication.translate("HistogramBar", u"-1", None))
        self.label_show_avg_fixed.setText(QCoreApplication.translate("HistogramBar", u"Average ", None))
        self.label_data1_avg_value.setText(QCoreApplication.translate("HistogramBar", u"-1", None))
        self.label_data2_min_value.setText(QCoreApplication.translate("HistogramBar", u"-1", None))
        self.label_data2_avg.setText(QCoreApplication.translate("HistogramBar", u"Average ", None))
        self.label_data1_max.setText(QCoreApplication.translate("HistogramBar", u"Max Value", None))
        self.label_x_axis_min_unit.setText(QCoreApplication.translate("HistogramBar", u"\u03bcm", None))
        self.label_data2_median_value.setText(QCoreApplication.translate("HistogramBar", u"-1", None))
        self.label_data1_std.setText(QCoreApplication.translate("HistogramBar", u"std", None))
        self.label_x_axis_max_unit.setText(QCoreApplication.translate("HistogramBar", u"\u03bcm", None))
        self.label_data2_avg_value.setText(QCoreApplication.translate("HistogramBar", u"-1", None))
        self.label_show_cumulative_fixed.setText(QCoreApplication.translate("HistogramBar", u"Cumulative Distribution line", None))
        self.label_x_axis_spacing_fixed.setText(QCoreApplication.translate("HistogramBar", u"Spacing:", None))
        self.label_data1_min.setText(QCoreApplication.translate("HistogramBar", u"Min Value", None))
        self.label_show_std_fixed.setText(QCoreApplication.translate("HistogramBar", u"Standard Deviation :", None))
        self.lineEdit_show_D1_value.setText(QCoreApplication.translate("HistogramBar", u"20", None))
        self.label_data2_max_value.setText(QCoreApplication.translate("HistogramBar", u"-1", None))
        self.checkBox_show_data1.setText(QCoreApplication.translate("HistogramBar", u"Show Data1", None))
        self.label_data1_total.setText(QCoreApplication.translate("HistogramBar", u"Total", None))
        self.btn_update_histogram.setText(QCoreApplication.translate("HistogramBar", u"Update", None))
        self.label_data1_median.setText(QCoreApplication.translate("HistogramBar", u"median", None))
        self.label_data2_std.setText(QCoreApplication.translate("HistogramBar", u"std", None))
        self.checkBox_show_median.setText(QCoreApplication.translate("HistogramBar", u"Show", None))
        self.label_x_axis_max_fixed.setText(QCoreApplication.translate("HistogramBar", u"MAX value:", None))
        self.label_data2_max.setText(QCoreApplication.translate("HistogramBar", u"Max Value", None))
        self.lineEdit_data1_name.setText("")
        self.btn_clear_data2.setText(QCoreApplication.translate("HistogramBar", u" Clear Data2", None))
        self.label_data2_total.setText(QCoreApplication.translate("HistogramBar", u"Total", None))
        self.lineEdit_xaxis_max_value.setText(QCoreApplication.translate("HistogramBar", u"-1", None))
        self.label_data2_median.setText(QCoreApplication.translate("HistogramBar", u"median", None))
        self.label_data2_total_value.setText(QCoreApplication.translate("HistogramBar", u"-1", None))
        self.checkBox_show_data2.setText(QCoreApplication.translate("HistogramBar", u"Show Data2", None))
        self.label_data1_name.setText(QCoreApplication.translate("HistogramBar", u"Data 1 Name", None))
        self.label_data1_std_value.setText(QCoreApplication.translate("HistogramBar", u"-1", None))
        self.label_data2_name.setText(QCoreApplication.translate("HistogramBar", u"Data 2 Name", None))
        self.label_show_median_fixed.setText(QCoreApplication.translate("HistogramBar", u"Median ", None))
        self.label_data1_median_value.setText(QCoreApplication.translate("HistogramBar", u"-1", None))
        self.btn_load_data1.setText(QCoreApplication.translate("HistogramBar", u"Load Data1", None))
        self.checkBox_show_avg.setText(QCoreApplication.translate("HistogramBar", u"Show", None))
        self.label_data1_total_value.setText(QCoreApplication.translate("HistogramBar", u"-1", None))
        self.checkBox_show_cumulative.setText(QCoreApplication.translate("HistogramBar", u"Show", None))
        self.checkBox_show_D2.setText(QCoreApplication.translate("HistogramBar", u"Show D2", None))
        self.btn_change_mode.setText(QCoreApplication.translate("HistogramBar", u"View Mode", None))
        self.lineEdit_show_D2_value.setText(QCoreApplication.translate("HistogramBar", u"50", None))
        self.label_showinfo_fixed.setText(QCoreApplication.translate("HistogramBar", u"Info Type", None))
        self.label_data2_min.setText(QCoreApplication.translate("HistogramBar", u"Min Value", None))
        self.label_histogram_fixed.setText(QCoreApplication.translate("HistogramBar", u"Histogram Setting", None))
        self.label_data2_std_value.setText(QCoreApplication.translate("HistogramBar", u"-1", None))
        self.checkBox_show_D3.setText(QCoreApplication.translate("HistogramBar", u"Show D3", None))
        self.comboBox_show_info_type.setItemText(0, QCoreApplication.translate("HistogramBar", u"Diameter", None))
        self.comboBox_show_info_type.setItemText(1, QCoreApplication.translate("HistogramBar", u"Surface", None))

        self.lineEdit_show_D3_value.setText(QCoreApplication.translate("HistogramBar", u"75", None))
        self.lineEdit_xaxis_spacing_value.setText(QCoreApplication.translate("HistogramBar", u"10", None))
        self.comboBox_show_hist_type.setItemText(0, QCoreApplication.translate("HistogramBar", u"Percent", None))
        self.comboBox_show_hist_type.setItemText(1, QCoreApplication.translate("HistogramBar", u"Number", None))

        self.checkBox_show_D1.setText(QCoreApplication.translate("HistogramBar", u"Show D1", None))
        self.label_x_axis_spacing_unit.setText(QCoreApplication.translate("HistogramBar", u"\u03bcm", None))
        self.label_data_unit.setText(QCoreApplication.translate("HistogramBar", u"\u03bcm", None))
    # retranslateUi

