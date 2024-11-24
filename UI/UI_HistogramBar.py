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
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_HistogramBar(object):
    def setupUi(self, HistogramBar):
        if not HistogramBar.objectName():
            HistogramBar.setObjectName(u"HistogramBar")
        HistogramBar.resize(320, 709)
        HistogramBar.setMinimumSize(QSize(320, 709))
        HistogramBar.setMaximumSize(QSize(344, 16777215))
        self.verticalLayout = QVBoxLayout(HistogramBar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 5, 0, 5)
        self.scrollArea = QScrollArea(HistogramBar)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(320, 699))
        self.scrollArea.setMaximumSize(QSize(320, 16777215))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -203, 320, 900))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(320, 900))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(320, 16777215))
        self.parameter = QWidget(self.scrollAreaWidgetContents)
        self.parameter.setObjectName(u"parameter")
        self.parameter.setGeometry(QRect(0, 0, 300, 901))
        self.parameter.setMinimumSize(QSize(300, 831))
        self.parameter.setMaximumSize(QSize(300, 16777215))
        self.parameter.setStyleSheet(u"border-color: rgb(255, 46, 52);")
        self.gridLayout_2 = QGridLayout(self.parameter)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, -1, 5, -1)
        self.label_x_axis_spacing_fixed = QLabel(self.parameter)
        self.label_x_axis_spacing_fixed.setObjectName(u"label_x_axis_spacing_fixed")
        self.label_x_axis_spacing_fixed.setMinimumSize(QSize(90, 20))
        self.label_x_axis_spacing_fixed.setMaximumSize(QSize(90, 20))

        self.gridLayout_2.addWidget(self.label_x_axis_spacing_fixed, 7, 1, 1, 1)

        self.label_showinfo_fixed = QLabel(self.parameter)
        self.label_showinfo_fixed.setObjectName(u"label_showinfo_fixed")
        self.label_showinfo_fixed.setMinimumSize(QSize(90, 20))
        self.label_showinfo_fixed.setMaximumSize(QSize(90, 20))

        self.gridLayout_2.addWidget(self.label_showinfo_fixed, 1, 1, 1, 1)

        self.lineEdit_xaxis_spacing_value = QLineEdit(self.parameter)
        self.lineEdit_xaxis_spacing_value.setObjectName(u"lineEdit_xaxis_spacing_value")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_xaxis_spacing_value.sizePolicy().hasHeightForWidth())
        self.lineEdit_xaxis_spacing_value.setSizePolicy(sizePolicy)
        self.lineEdit_xaxis_spacing_value.setMinimumSize(QSize(0, 25))
        self.lineEdit_xaxis_spacing_value.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_xaxis_spacing_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_xaxis_spacing_value, 7, 2, 1, 1)

        self.lineEdit_show_D1_value = QLineEdit(self.parameter)
        self.lineEdit_show_D1_value.setObjectName(u"lineEdit_show_D1_value")
        sizePolicy.setHeightForWidth(self.lineEdit_show_D1_value.sizePolicy().hasHeightForWidth())
        self.lineEdit_show_D1_value.setSizePolicy(sizePolicy)
        self.lineEdit_show_D1_value.setMinimumSize(QSize(0, 25))
        self.lineEdit_show_D1_value.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_show_D1_value.setMaxLength(100)
        self.lineEdit_show_D1_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_show_D1_value, 18, 1, 1, 1)

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

        self.gridLayout_2.addWidget(self.comboBox_show_hist_type, 5, 2, 1, 1)

        self.checkBox_show_cumulative = QCheckBox(self.parameter)
        self.checkBox_show_cumulative.setObjectName(u"checkBox_show_cumulative")
        self.checkBox_show_cumulative.setMinimumSize(QSize(90, 20))
        self.checkBox_show_cumulative.setMaximumSize(QSize(90, 20))
        self.checkBox_show_cumulative.setChecked(True)

        self.gridLayout_2.addWidget(self.checkBox_show_cumulative, 16, 3, 1, 1)

        self.label_data1_min_value = QLabel(self.parameter)
        self.label_data1_min_value.setObjectName(u"label_data1_min_value")
        self.label_data1_min_value.setMinimumSize(QSize(0, 20))
        self.label_data1_min_value.setMaximumSize(QSize(16777215, 20))
        self.label_data1_min_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_data1_min_value, 54, 1, 1, 1)

        self.label_data1_name = QLabel(self.parameter)
        self.label_data1_name.setObjectName(u"label_data1_name")
        self.label_data1_name.setMinimumSize(QSize(0, 20))
        self.label_data1_name.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_2.addWidget(self.label_data1_name, 48, 1, 1, 1)

        self.label_show_cumulative_fixed = QLabel(self.parameter)
        self.label_show_cumulative_fixed.setObjectName(u"label_show_cumulative_fixed")
        self.label_show_cumulative_fixed.setMinimumSize(QSize(170, 20))
        self.label_show_cumulative_fixed.setMaximumSize(QSize(170, 20))

        self.gridLayout_2.addWidget(self.label_show_cumulative_fixed, 16, 1, 1, 1)

        self.label_x_axis_max_unit = QLabel(self.parameter)
        self.label_x_axis_max_unit.setObjectName(u"label_x_axis_max_unit")
        self.label_x_axis_max_unit.setMinimumSize(QSize(0, 20))
        self.label_x_axis_max_unit.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_2.addWidget(self.label_x_axis_max_unit, 9, 3, 1, 1)

        self.checkBox_show_D6 = QCheckBox(self.parameter)
        self.checkBox_show_D6.setObjectName(u"checkBox_show_D6")
        self.checkBox_show_D6.setMinimumSize(QSize(0, 20))
        self.checkBox_show_D6.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_2.addWidget(self.checkBox_show_D6, 19, 3, 1, 1)

        self.label_data1_avg_value = QLabel(self.parameter)
        self.label_data1_avg_value.setObjectName(u"label_data1_avg_value")
        self.label_data1_avg_value.setMinimumSize(QSize(0, 20))
        self.label_data1_avg_value.setMaximumSize(QSize(16777215, 20))
        self.label_data1_avg_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_data1_avg_value, 52, 1, 1, 1)

        self.line_space2_3 = QFrame(self.parameter)
        self.line_space2_3.setObjectName(u"line_space2_3")
        self.line_space2_3.setMinimumSize(QSize(288, 1))
        self.line_space2_3.setMaximumSize(QSize(288, 1))
        self.line_space2_3.setAutoFillBackground(False)
        self.line_space2_3.setStyleSheet(u"background-color: rgb(113, 112, 111);")
        self.line_space2_3.setFrameShape(QFrame.Shape.HLine)
        self.line_space2_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_space2_3, 10, 1, 1, 1)

        self.label_show_boxplot_fixed = QLabel(self.parameter)
        self.label_show_boxplot_fixed.setObjectName(u"label_show_boxplot_fixed")
        self.label_show_boxplot_fixed.setMinimumSize(QSize(90, 20))
        self.label_show_boxplot_fixed.setMaximumSize(QSize(90, 20))

        self.gridLayout_2.addWidget(self.label_show_boxplot_fixed, 11, 1, 1, 1)

        self.checkBox_show_hist_value = QCheckBox(self.parameter)
        self.checkBox_show_hist_value.setObjectName(u"checkBox_show_hist_value")
        self.checkBox_show_hist_value.setMinimumSize(QSize(100, 20))
        self.checkBox_show_hist_value.setMaximumSize(QSize(100, 20))
        self.checkBox_show_hist_value.setChecked(False)

        self.gridLayout_2.addWidget(self.checkBox_show_hist_value, 6, 3, 1, 1)

        self.label_x_axis_min_fixed = QLabel(self.parameter)
        self.label_x_axis_min_fixed.setObjectName(u"label_x_axis_min_fixed")
        self.label_x_axis_min_fixed.setMinimumSize(QSize(90, 20))
        self.label_x_axis_min_fixed.setMaximumSize(QSize(90, 20))

        self.gridLayout_2.addWidget(self.label_x_axis_min_fixed, 8, 1, 1, 1)

        self.btn_update_name = QPushButton(self.parameter)
        self.btn_update_name.setObjectName(u"btn_update_name")
        sizePolicy.setHeightForWidth(self.btn_update_name.sizePolicy().hasHeightForWidth())
        self.btn_update_name.setSizePolicy(sizePolicy)
        self.btn_update_name.setMinimumSize(QSize(92, 25))
        self.btn_update_name.setMaximumSize(QSize(92, 25))
        font = QFont()
        font.setPointSize(11)
        self.btn_update_name.setFont(font)

        self.gridLayout_2.addWidget(self.btn_update_name, 49, 3, 1, 1)

        self.label_showhist_fixed = QLabel(self.parameter)
        self.label_showhist_fixed.setObjectName(u"label_showhist_fixed")
        self.label_showhist_fixed.setMinimumSize(QSize(90, 20))
        self.label_showhist_fixed.setMaximumSize(QSize(90, 20))

        self.gridLayout_2.addWidget(self.label_showhist_fixed, 5, 1, 1, 1)

        self.btn_change_mode = QPushButton(self.parameter)
        self.btn_change_mode.setObjectName(u"btn_change_mode")
        sizePolicy.setHeightForWidth(self.btn_change_mode.sizePolicy().hasHeightForWidth())
        self.btn_change_mode.setSizePolicy(sizePolicy)
        self.btn_change_mode.setMinimumSize(QSize(92, 25))
        self.btn_change_mode.setMaximumSize(QSize(92, 25))
        font1 = QFont()
        font1.setPointSize(12)
        self.btn_change_mode.setFont(font1)

        self.gridLayout_2.addWidget(self.btn_change_mode, 0, 3, 1, 1)

        self.label_data1_total = QLabel(self.parameter)
        self.label_data1_total.setObjectName(u"label_data1_total")
        self.label_data1_total.setMinimumSize(QSize(80, 20))
        self.label_data1_total.setMaximumSize(QSize(80, 20))
        self.label_data1_total.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_data1_total, 53, 3, 1, 1)

        self.lineEdit_data1_name = QLineEdit(self.parameter)
        self.lineEdit_data1_name.setObjectName(u"lineEdit_data1_name")
        self.lineEdit_data1_name.setMinimumSize(QSize(180, 0))
        self.lineEdit_data1_name.setMaximumSize(QSize(180, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_data1_name, 49, 1, 1, 1)

        self.comboBox_show_info_type = QComboBox(self.parameter)
        self.comboBox_show_info_type.addItem("")
        self.comboBox_show_info_type.setObjectName(u"comboBox_show_info_type")
        sizePolicy.setHeightForWidth(self.comboBox_show_info_type.sizePolicy().hasHeightForWidth())
        self.comboBox_show_info_type.setSizePolicy(sizePolicy)
        self.comboBox_show_info_type.setMinimumSize(QSize(90, 25))
        self.comboBox_show_info_type.setMaximumSize(QSize(90, 25))
        self.comboBox_show_info_type.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_show_info_type.setMinimumContentsLength(6)

        self.gridLayout_2.addWidget(self.comboBox_show_info_type, 1, 2, 1, 1)

        self.lineEdit_xaxis_min_value = QLineEdit(self.parameter)
        self.lineEdit_xaxis_min_value.setObjectName(u"lineEdit_xaxis_min_value")
        sizePolicy.setHeightForWidth(self.lineEdit_xaxis_min_value.sizePolicy().hasHeightForWidth())
        self.lineEdit_xaxis_min_value.setSizePolicy(sizePolicy)
        self.lineEdit_xaxis_min_value.setMinimumSize(QSize(0, 25))
        self.lineEdit_xaxis_min_value.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_xaxis_min_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_xaxis_min_value, 8, 2, 1, 1)

        self.btn_load_data1 = QPushButton(self.parameter)
        self.btn_load_data1.setObjectName(u"btn_load_data1")
        sizePolicy.setHeightForWidth(self.btn_load_data1.sizePolicy().hasHeightForWidth())
        self.btn_load_data1.setSizePolicy(sizePolicy)
        self.btn_load_data1.setMinimumSize(QSize(92, 25))
        self.btn_load_data1.setMaximumSize(QSize(92, 25))
        self.btn_load_data1.setFont(font1)

        self.gridLayout_2.addWidget(self.btn_load_data1, 50, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 55, 2, 2, 1)

        self.label_x_axis_spacing_unit = QLabel(self.parameter)
        self.label_x_axis_spacing_unit.setObjectName(u"label_x_axis_spacing_unit")
        self.label_x_axis_spacing_unit.setMinimumSize(QSize(0, 20))
        self.label_x_axis_spacing_unit.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_2.addWidget(self.label_x_axis_spacing_unit, 7, 3, 1, 1)

        self.btn_clear_data1 = QPushButton(self.parameter)
        self.btn_clear_data1.setObjectName(u"btn_clear_data1")
        sizePolicy.setHeightForWidth(self.btn_clear_data1.sizePolicy().hasHeightForWidth())
        self.btn_clear_data1.setSizePolicy(sizePolicy)
        self.btn_clear_data1.setMinimumSize(QSize(92, 25))
        self.btn_clear_data1.setMaximumSize(QSize(92, 25))
        self.btn_clear_data1.setFont(font1)

        self.gridLayout_2.addWidget(self.btn_clear_data1, 50, 2, 1, 1)

        self.checkBox_show_D5 = QCheckBox(self.parameter)
        self.checkBox_show_D5.setObjectName(u"checkBox_show_D5")
        self.checkBox_show_D5.setMinimumSize(QSize(0, 20))
        self.checkBox_show_D5.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_2.addWidget(self.checkBox_show_D5, 19, 2, 1, 1)

        self.checkBox_show_D3 = QCheckBox(self.parameter)
        self.checkBox_show_D3.setObjectName(u"checkBox_show_D3")
        self.checkBox_show_D3.setMinimumSize(QSize(0, 20))
        self.checkBox_show_D3.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_2.addWidget(self.checkBox_show_D3, 17, 3, 1, 1)

        self.label_data1_max_value = QLabel(self.parameter)
        self.label_data1_max_value.setObjectName(u"label_data1_max_value")
        self.label_data1_max_value.setMinimumSize(QSize(0, 20))
        self.label_data1_max_value.setMaximumSize(QSize(16777215, 20))
        self.label_data1_max_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_data1_max_value, 54, 2, 1, 1)

        self.label_title_fixed_3 = QLabel(self.parameter)
        self.label_title_fixed_3.setObjectName(u"label_title_fixed_3")
        self.label_title_fixed_3.setMinimumSize(QSize(150, 20))
        self.label_title_fixed_3.setMaximumSize(QSize(150, 20))

        self.gridLayout_2.addWidget(self.label_title_fixed_3, 6, 1, 1, 1)

        self.label_data1_median = QLabel(self.parameter)
        self.label_data1_median.setObjectName(u"label_data1_median")
        self.label_data1_median.setMinimumSize(QSize(80, 20))
        self.label_data1_median.setMaximumSize(QSize(80, 20))
        self.label_data1_median.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_data1_median, 51, 2, 1, 1)

        self.label_current_data = QLabel(self.parameter)
        self.label_current_data.setObjectName(u"label_current_data")
        self.label_current_data.setMinimumSize(QSize(170, 20))
        self.label_current_data.setMaximumSize(QSize(170, 20))

        self.gridLayout_2.addWidget(self.label_current_data, 24, 1, 1, 2)

        self.lineEdit_show_D6_value = QLineEdit(self.parameter)
        self.lineEdit_show_D6_value.setObjectName(u"lineEdit_show_D6_value")
        sizePolicy.setHeightForWidth(self.lineEdit_show_D6_value.sizePolicy().hasHeightForWidth())
        self.lineEdit_show_D6_value.setSizePolicy(sizePolicy)
        self.lineEdit_show_D6_value.setMinimumSize(QSize(0, 25))
        self.lineEdit_show_D6_value.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_show_D6_value.setMaxLength(100)
        self.lineEdit_show_D6_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_show_D6_value, 20, 3, 1, 1)

        self.checkBox_show_avg = QCheckBox(self.parameter)
        self.checkBox_show_avg.setObjectName(u"checkBox_show_avg")
        self.checkBox_show_avg.setMinimumSize(QSize(90, 20))
        self.checkBox_show_avg.setMaximumSize(QSize(90, 20))
        self.checkBox_show_avg.setChecked(False)

        self.gridLayout_2.addWidget(self.checkBox_show_avg, 12, 1, 1, 1)

        self.lineEdit_show_D3_value = QLineEdit(self.parameter)
        self.lineEdit_show_D3_value.setObjectName(u"lineEdit_show_D3_value")
        sizePolicy.setHeightForWidth(self.lineEdit_show_D3_value.sizePolicy().hasHeightForWidth())
        self.lineEdit_show_D3_value.setSizePolicy(sizePolicy)
        self.lineEdit_show_D3_value.setMinimumSize(QSize(0, 25))
        self.lineEdit_show_D3_value.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_show_D3_value.setMaxLength(100)
        self.lineEdit_show_D3_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_show_D3_value, 18, 3, 1, 1)

        self.line_space2_4 = QFrame(self.parameter)
        self.line_space2_4.setObjectName(u"line_space2_4")
        self.line_space2_4.setMinimumSize(QSize(288, 1))
        self.line_space2_4.setMaximumSize(QSize(288, 1))
        self.line_space2_4.setAutoFillBackground(False)
        self.line_space2_4.setStyleSheet(u"background-color: rgb(113, 112, 111);")
        self.line_space2_4.setFrameShape(QFrame.Shape.HLine)
        self.line_space2_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_space2_4, 14, 1, 1, 1)

        self.label_data1_avg = QLabel(self.parameter)
        self.label_data1_avg.setObjectName(u"label_data1_avg")
        self.label_data1_avg.setMinimumSize(QSize(80, 20))
        self.label_data1_avg.setMaximumSize(QSize(80, 20))
        self.label_data1_avg.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_data1_avg, 51, 1, 1, 1)

        self.label_x_axis_max_fixed = QLabel(self.parameter)
        self.label_x_axis_max_fixed.setObjectName(u"label_x_axis_max_fixed")
        self.label_x_axis_max_fixed.setMinimumSize(QSize(90, 20))
        self.label_x_axis_max_fixed.setMaximumSize(QSize(90, 20))

        self.gridLayout_2.addWidget(self.label_x_axis_max_fixed, 9, 1, 1, 1)

        self.checkBox_show_D4 = QCheckBox(self.parameter)
        self.checkBox_show_D4.setObjectName(u"checkBox_show_D4")
        self.checkBox_show_D4.setMinimumSize(QSize(0, 20))
        self.checkBox_show_D4.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_2.addWidget(self.checkBox_show_D4, 19, 1, 1, 1)

        self.lineEdit_show_D4_value = QLineEdit(self.parameter)
        self.lineEdit_show_D4_value.setObjectName(u"lineEdit_show_D4_value")
        sizePolicy.setHeightForWidth(self.lineEdit_show_D4_value.sizePolicy().hasHeightForWidth())
        self.lineEdit_show_D4_value.setSizePolicy(sizePolicy)
        self.lineEdit_show_D4_value.setMinimumSize(QSize(0, 25))
        self.lineEdit_show_D4_value.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_show_D4_value.setMaxLength(100)
        self.lineEdit_show_D4_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_show_D4_value, 20, 1, 1, 1)

        self.checkBox_show_box_plot = QCheckBox(self.parameter)
        self.checkBox_show_box_plot.setObjectName(u"checkBox_show_box_plot")
        self.checkBox_show_box_plot.setMinimumSize(QSize(90, 20))
        self.checkBox_show_box_plot.setMaximumSize(QSize(90, 20))
        self.checkBox_show_box_plot.setChecked(False)

        self.gridLayout_2.addWidget(self.checkBox_show_box_plot, 11, 2, 1, 1)

        self.label_data1_total_value = QLabel(self.parameter)
        self.label_data1_total_value.setObjectName(u"label_data1_total_value")
        self.label_data1_total_value.setMinimumSize(QSize(0, 20))
        self.label_data1_total_value.setMaximumSize(QSize(16777215, 20))
        self.label_data1_total_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_data1_total_value, 54, 3, 1, 1)

        self.checkBox_show_D1 = QCheckBox(self.parameter)
        self.checkBox_show_D1.setObjectName(u"checkBox_show_D1")
        self.checkBox_show_D1.setMinimumSize(QSize(0, 20))
        self.checkBox_show_D1.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_2.addWidget(self.checkBox_show_D1, 17, 1, 1, 1)

        self.label_data_unit = QLabel(self.parameter)
        self.label_data_unit.setObjectName(u"label_data_unit")
        self.label_data_unit.setMinimumSize(QSize(50, 20))
        self.label_data_unit.setMaximumSize(QSize(50, 20))
        self.label_data_unit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_data_unit, 1, 3, 1, 1)

        self.label_data1_std_value = QLabel(self.parameter)
        self.label_data1_std_value.setObjectName(u"label_data1_std_value")
        self.label_data1_std_value.setMinimumSize(QSize(0, 20))
        self.label_data1_std_value.setMaximumSize(QSize(16777215, 20))
        self.label_data1_std_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_data1_std_value, 52, 3, 1, 1)

        self.label_data1_min = QLabel(self.parameter)
        self.label_data1_min.setObjectName(u"label_data1_min")
        self.label_data1_min.setMinimumSize(QSize(80, 20))
        self.label_data1_min.setMaximumSize(QSize(80, 20))
        self.label_data1_min.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_data1_min, 53, 1, 1, 1)

        self.label_data1_std = QLabel(self.parameter)
        self.label_data1_std.setObjectName(u"label_data1_std")
        self.label_data1_std.setMinimumSize(QSize(80, 20))
        self.label_data1_std.setMaximumSize(QSize(80, 20))
        self.label_data1_std.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_data1_std, 51, 3, 1, 1)

        self.label_data1_median_value = QLabel(self.parameter)
        self.label_data1_median_value.setObjectName(u"label_data1_median_value")
        self.label_data1_median_value.setMinimumSize(QSize(0, 20))
        self.label_data1_median_value.setMaximumSize(QSize(16777215, 20))
        self.label_data1_median_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_data1_median_value, 52, 2, 1, 1)

        self.btn_update_histogram = QPushButton(self.parameter)
        self.btn_update_histogram.setObjectName(u"btn_update_histogram")
        sizePolicy.setHeightForWidth(self.btn_update_histogram.sizePolicy().hasHeightForWidth())
        self.btn_update_histogram.setSizePolicy(sizePolicy)
        self.btn_update_histogram.setMinimumSize(QSize(92, 25))
        self.btn_update_histogram.setMaximumSize(QSize(92, 25))
        self.btn_update_histogram.setFont(font1)

        self.gridLayout_2.addWidget(self.btn_update_histogram, 4, 3, 1, 1)

        self.line_space2_2 = QFrame(self.parameter)
        self.line_space2_2.setObjectName(u"line_space2_2")
        self.line_space2_2.setMinimumSize(QSize(288, 1))
        self.line_space2_2.setMaximumSize(QSize(288, 1))
        self.line_space2_2.setAutoFillBackground(False)
        self.line_space2_2.setStyleSheet(u"background-color: rgb(113, 112, 111);")
        self.line_space2_2.setFrameShape(QFrame.Shape.HLine)
        self.line_space2_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_space2_2, 3, 1, 1, 1)

        self.lineEdit_xaxis_max_value = QLineEdit(self.parameter)
        self.lineEdit_xaxis_max_value.setObjectName(u"lineEdit_xaxis_max_value")
        sizePolicy.setHeightForWidth(self.lineEdit_xaxis_max_value.sizePolicy().hasHeightForWidth())
        self.lineEdit_xaxis_max_value.setSizePolicy(sizePolicy)
        self.lineEdit_xaxis_max_value.setMinimumSize(QSize(0, 25))
        self.lineEdit_xaxis_max_value.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_xaxis_max_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_xaxis_max_value, 9, 2, 1, 1)

        self.line_space1_2 = QFrame(self.parameter)
        self.line_space1_2.setObjectName(u"line_space1_2")
        self.line_space1_2.setMinimumSize(QSize(288, 1))
        self.line_space1_2.setMaximumSize(QSize(288, 1))
        self.line_space1_2.setAutoFillBackground(False)
        self.line_space1_2.setStyleSheet(u"background-color: rgb(113, 112, 111);")
        self.line_space1_2.setFrameShape(QFrame.Shape.HLine)
        self.line_space1_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_space1_2, 22, 1, 1, 1)

        self.comboBox_current_data = QComboBox(self.parameter)
        self.comboBox_current_data.addItem("")
        self.comboBox_current_data.addItem("")
        self.comboBox_current_data.addItem("")
        self.comboBox_current_data.addItem("")
        self.comboBox_current_data.addItem("")
        self.comboBox_current_data.setObjectName(u"comboBox_current_data")
        self.comboBox_current_data.setMinimumSize(QSize(90, 25))
        self.comboBox_current_data.setMaximumSize(QSize(90, 25))

        self.gridLayout_2.addWidget(self.comboBox_current_data, 24, 3, 1, 1)

        self.label_data1_max = QLabel(self.parameter)
        self.label_data1_max.setObjectName(u"label_data1_max")
        self.label_data1_max.setMinimumSize(QSize(80, 20))
        self.label_data1_max.setMaximumSize(QSize(80, 20))
        self.label_data1_max.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_data1_max, 53, 2, 1, 1)

        self.checkBox_show_D2 = QCheckBox(self.parameter)
        self.checkBox_show_D2.setObjectName(u"checkBox_show_D2")
        self.checkBox_show_D2.setMinimumSize(QSize(0, 20))
        self.checkBox_show_D2.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_2.addWidget(self.checkBox_show_D2, 17, 2, 1, 1)

        self.label_histogram_fixed = QLabel(self.parameter)
        self.label_histogram_fixed.setObjectName(u"label_histogram_fixed")
        self.label_histogram_fixed.setMinimumSize(QSize(150, 20))
        self.label_histogram_fixed.setMaximumSize(QSize(150, 20))

        self.gridLayout_2.addWidget(self.label_histogram_fixed, 4, 1, 1, 1)

        self.label_show_image_fixed = QLabel(self.parameter)
        self.label_show_image_fixed.setObjectName(u"label_show_image_fixed")
        self.label_show_image_fixed.setMinimumSize(QSize(180, 20))
        self.label_show_image_fixed.setMaximumSize(QSize(180, 20))

        self.gridLayout_2.addWidget(self.label_show_image_fixed, 0, 1, 1, 1)

        self.checkBox_show_data = QCheckBox(self.parameter)
        self.checkBox_show_data.setObjectName(u"checkBox_show_data")

        self.gridLayout_2.addWidget(self.checkBox_show_data, 50, 3, 1, 1)

        self.checkBox_show_box_value = QCheckBox(self.parameter)
        self.checkBox_show_box_value.setObjectName(u"checkBox_show_box_value")
        self.checkBox_show_box_value.setMinimumSize(QSize(90, 20))
        self.checkBox_show_box_value.setMaximumSize(QSize(90, 20))

        self.gridLayout_2.addWidget(self.checkBox_show_box_value, 11, 3, 1, 1)

        self.lineEdit_show_D2_value = QLineEdit(self.parameter)
        self.lineEdit_show_D2_value.setObjectName(u"lineEdit_show_D2_value")
        sizePolicy.setHeightForWidth(self.lineEdit_show_D2_value.sizePolicy().hasHeightForWidth())
        self.lineEdit_show_D2_value.setSizePolicy(sizePolicy)
        self.lineEdit_show_D2_value.setMinimumSize(QSize(0, 25))
        self.lineEdit_show_D2_value.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_show_D2_value.setMaxLength(100)
        self.lineEdit_show_D2_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_show_D2_value, 18, 2, 1, 1)

        self.lineEdit_show_D5_value = QLineEdit(self.parameter)
        self.lineEdit_show_D5_value.setObjectName(u"lineEdit_show_D5_value")
        sizePolicy.setHeightForWidth(self.lineEdit_show_D5_value.sizePolicy().hasHeightForWidth())
        self.lineEdit_show_D5_value.setSizePolicy(sizePolicy)
        self.lineEdit_show_D5_value.setMinimumSize(QSize(0, 25))
        self.lineEdit_show_D5_value.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_show_D5_value.setMaxLength(100)
        self.lineEdit_show_D5_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_show_D5_value, 20, 2, 1, 1)

        self.label_x_axis_min_unit = QLabel(self.parameter)
        self.label_x_axis_min_unit.setObjectName(u"label_x_axis_min_unit")
        self.label_x_axis_min_unit.setMinimumSize(QSize(0, 20))
        self.label_x_axis_min_unit.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_2.addWidget(self.label_x_axis_min_unit, 8, 3, 1, 1)

        self.checkBox_show_multi_data = QCheckBox(self.parameter)
        self.checkBox_show_multi_data.setObjectName(u"checkBox_show_multi_data")

        self.gridLayout_2.addWidget(self.checkBox_show_multi_data, 48, 2, 1, 2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(HistogramBar)

        QMetaObject.connectSlotsByName(HistogramBar)
    # setupUi

    def retranslateUi(self, HistogramBar):
        HistogramBar.setWindowTitle(QCoreApplication.translate("HistogramBar", u"Form", None))
        self.label_x_axis_spacing_fixed.setText(QCoreApplication.translate("HistogramBar", u"Spacing:", None))
        self.label_showinfo_fixed.setText(QCoreApplication.translate("HistogramBar", u"Info Type", None))
        self.lineEdit_xaxis_spacing_value.setText(QCoreApplication.translate("HistogramBar", u"10", None))
        self.lineEdit_show_D1_value.setText(QCoreApplication.translate("HistogramBar", u"20", None))
        self.comboBox_show_hist_type.setItemText(0, QCoreApplication.translate("HistogramBar", u"Percent", None))
        self.comboBox_show_hist_type.setItemText(1, QCoreApplication.translate("HistogramBar", u"Number", None))

        self.checkBox_show_cumulative.setText(QCoreApplication.translate("HistogramBar", u"Show", None))
        self.label_data1_min_value.setText(QCoreApplication.translate("HistogramBar", u"-1", None))
        self.label_data1_name.setText(QCoreApplication.translate("HistogramBar", u"Data Name", None))
        self.label_show_cumulative_fixed.setText(QCoreApplication.translate("HistogramBar", u"Cumulative Distribution line", None))
        self.label_x_axis_max_unit.setText(QCoreApplication.translate("HistogramBar", u"\u03bcm", None))
        self.checkBox_show_D6.setText(QCoreApplication.translate("HistogramBar", u"Show D6", None))
        self.label_data1_avg_value.setText(QCoreApplication.translate("HistogramBar", u"-1", None))
        self.label_show_boxplot_fixed.setText(QCoreApplication.translate("HistogramBar", u"Box plot", None))
        self.checkBox_show_hist_value.setText(QCoreApplication.translate("HistogramBar", u"Show Value", None))
        self.label_x_axis_min_fixed.setText(QCoreApplication.translate("HistogramBar", u"MIN value:", None))
        self.btn_update_name.setText(QCoreApplication.translate("HistogramBar", u"Update Name", None))
        self.label_showhist_fixed.setText(QCoreApplication.translate("HistogramBar", u"Hist Type", None))
        self.btn_change_mode.setText(QCoreApplication.translate("HistogramBar", u"View Mode", None))
        self.label_data1_total.setText(QCoreApplication.translate("HistogramBar", u"Total", None))
        self.lineEdit_data1_name.setText("")
        self.comboBox_show_info_type.setItemText(0, QCoreApplication.translate("HistogramBar", u"Diameter", None))

        self.lineEdit_xaxis_min_value.setText(QCoreApplication.translate("HistogramBar", u"-1", None))
        self.btn_load_data1.setText(QCoreApplication.translate("HistogramBar", u"Load Data", None))
        self.label_x_axis_spacing_unit.setText(QCoreApplication.translate("HistogramBar", u"\u03bcm", None))
        self.btn_clear_data1.setText(QCoreApplication.translate("HistogramBar", u" Clear Data", None))
        self.checkBox_show_D5.setText(QCoreApplication.translate("HistogramBar", u"Show D5", None))
        self.checkBox_show_D3.setText(QCoreApplication.translate("HistogramBar", u"Show D3", None))
        self.label_data1_max_value.setText(QCoreApplication.translate("HistogramBar", u"-1", None))
        self.label_title_fixed_3.setText(QCoreApplication.translate("HistogramBar", u"X-axis", None))
        self.label_data1_median.setText(QCoreApplication.translate("HistogramBar", u"Median", None))
        self.label_current_data.setText(QCoreApplication.translate("HistogramBar", u"Current Show Data", None))
        self.lineEdit_show_D6_value.setText(QCoreApplication.translate("HistogramBar", u"80", None))
        self.checkBox_show_avg.setText(QCoreApplication.translate("HistogramBar", u"Show Avg", None))
        self.lineEdit_show_D3_value.setText(QCoreApplication.translate("HistogramBar", u"50", None))
        self.label_data1_avg.setText(QCoreApplication.translate("HistogramBar", u"Average ", None))
        self.label_x_axis_max_fixed.setText(QCoreApplication.translate("HistogramBar", u"MAX value:", None))
        self.checkBox_show_D4.setText(QCoreApplication.translate("HistogramBar", u"Show D4", None))
        self.lineEdit_show_D4_value.setText(QCoreApplication.translate("HistogramBar", u"70", None))
        self.checkBox_show_box_plot.setText(QCoreApplication.translate("HistogramBar", u"Show Box", None))
        self.label_data1_total_value.setText(QCoreApplication.translate("HistogramBar", u"-1", None))
        self.checkBox_show_D1.setText(QCoreApplication.translate("HistogramBar", u"Show D1", None))
        self.label_data_unit.setText(QCoreApplication.translate("HistogramBar", u"\u03bcm", None))
        self.label_data1_std_value.setText(QCoreApplication.translate("HistogramBar", u"-1", None))
        self.label_data1_min.setText(QCoreApplication.translate("HistogramBar", u"Min Value", None))
        self.label_data1_std.setText(QCoreApplication.translate("HistogramBar", u"STD", None))
        self.label_data1_median_value.setText(QCoreApplication.translate("HistogramBar", u"-1", None))
        self.btn_update_histogram.setText(QCoreApplication.translate("HistogramBar", u"Update", None))
        self.lineEdit_xaxis_max_value.setText(QCoreApplication.translate("HistogramBar", u"-1", None))
        self.comboBox_current_data.setItemText(0, QCoreApplication.translate("HistogramBar", u"Data 1", None))
        self.comboBox_current_data.setItemText(1, QCoreApplication.translate("HistogramBar", u"Data 2", None))
        self.comboBox_current_data.setItemText(2, QCoreApplication.translate("HistogramBar", u"Data 3", None))
        self.comboBox_current_data.setItemText(3, QCoreApplication.translate("HistogramBar", u"Data 4", None))
        self.comboBox_current_data.setItemText(4, QCoreApplication.translate("HistogramBar", u"Data 5", None))

        self.label_data1_max.setText(QCoreApplication.translate("HistogramBar", u"Max Value", None))
        self.checkBox_show_D2.setText(QCoreApplication.translate("HistogramBar", u"Show D2", None))
        self.label_histogram_fixed.setText(QCoreApplication.translate("HistogramBar", u"Histogram Setting", None))
        self.label_show_image_fixed.setText(QCoreApplication.translate("HistogramBar", u"Histogram Mode", None))
        self.checkBox_show_data.setText(QCoreApplication.translate("HistogramBar", u"Show Data", None))
        self.checkBox_show_box_value.setText(QCoreApplication.translate("HistogramBar", u"Show Value", None))
        self.lineEdit_show_D2_value.setText(QCoreApplication.translate("HistogramBar", u"30", None))
        self.lineEdit_show_D5_value.setText(QCoreApplication.translate("HistogramBar", u"75", None))
        self.label_x_axis_min_unit.setText(QCoreApplication.translate("HistogramBar", u"\u03bcm", None))
        self.checkBox_show_multi_data.setText(QCoreApplication.translate("HistogramBar", u"Compare Multiple Data", None))
    # retranslateUi

