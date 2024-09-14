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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_ContentBar(object):
    def setupUi(self, ContentBar):
        if not ContentBar.objectName():
            ContentBar.setObjectName(u"ContentBar")
        ContentBar.resize(316, 751)
        self.parameter = QWidget(ContentBar)
        self.parameter.setObjectName(u"parameter")
        self.parameter.setGeometry(QRect(0, 0, 300, 764))
        self.parameter.setMinimumSize(QSize(300, 0))
        self.parameter.setMaximumSize(QSize(300, 16777215))
        self.parameter.setStyleSheet(u"border-color: rgb(255, 46, 52);")
        self.gridLayout = QGridLayout(self.parameter)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_title_fixed = QLabel(self.parameter)
        self.label_title_fixed.setObjectName(u"label_title_fixed")
        self.label_title_fixed.setMinimumSize(QSize(180, 20))
        self.label_title_fixed.setMaximumSize(QSize(180, 20))

        self.gridLayout.addWidget(self.label_title_fixed, 3, 0, 1, 2)

        self.btn_save_contours = QPushButton(self.parameter)
        self.btn_save_contours.setObjectName(u"btn_save_contours")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save_contours.sizePolicy().hasHeightForWidth())
        self.btn_save_contours.setSizePolicy(sizePolicy)
        self.btn_save_contours.setMinimumSize(QSize(92, 25))
        self.btn_save_contours.setMaximumSize(QSize(92, 25))
        font = QFont()
        font.setPointSize(12)
        self.btn_save_contours.setFont(font)

        self.gridLayout.addWidget(self.btn_save_contours, 21, 2, 1, 1)

        self.labe_select_roi_fixed = QLabel(self.parameter)
        self.labe_select_roi_fixed.setObjectName(u"labe_select_roi_fixed")
        self.labe_select_roi_fixed.setMinimumSize(QSize(180, 20))
        self.labe_select_roi_fixed.setMaximumSize(QSize(180, 20))

        self.gridLayout.addWidget(self.labe_select_roi_fixed, 12, 0, 1, 2)

        self.btn_load_data2 = QPushButton(self.parameter)
        self.btn_load_data2.setObjectName(u"btn_load_data2")
        sizePolicy.setHeightForWidth(self.btn_load_data2.sizePolicy().hasHeightForWidth())
        self.btn_load_data2.setSizePolicy(sizePolicy)
        self.btn_load_data2.setMinimumSize(QSize(92, 25))
        self.btn_load_data2.setMaximumSize(QSize(92, 25))
        self.btn_load_data2.setFont(font)

        self.gridLayout.addWidget(self.btn_load_data2, 21, 1, 1, 1)

        self.btn_refer_obj = QPushButton(self.parameter)
        self.btn_refer_obj.setObjectName(u"btn_refer_obj")
        sizePolicy.setHeightForWidth(self.btn_refer_obj.sizePolicy().hasHeightForWidth())
        self.btn_refer_obj.setSizePolicy(sizePolicy)
        self.btn_refer_obj.setMinimumSize(QSize(92, 25))
        self.btn_refer_obj.setMaximumSize(QSize(92, 25))
        self.btn_refer_obj.setFont(font)

        self.gridLayout.addWidget(self.btn_refer_obj, 6, 0, 1, 1)

        self.label_bins_fixed = QLabel(self.parameter)
        self.label_bins_fixed.setObjectName(u"label_bins_fixed")
        self.label_bins_fixed.setMinimumSize(QSize(0, 20))
        self.label_bins_fixed.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.label_bins_fixed, 29, 0, 1, 2)

        self.label_contours = QLabel(self.parameter)
        self.label_contours.setObjectName(u"label_contours")
        self.label_contours.setMinimumSize(QSize(90, 0))
        self.label_contours.setMaximumSize(QSize(90, 20))

        self.gridLayout.addWidget(self.label_contours, 15, 0, 1, 1)

        self.checkBox_roi_reverse = QCheckBox(self.parameter)
        self.checkBox_roi_reverse.setObjectName(u"checkBox_roi_reverse")
        sizePolicy.setHeightForWidth(self.checkBox_roi_reverse.sizePolicy().hasHeightForWidth())
        self.checkBox_roi_reverse.setSizePolicy(sizePolicy)
        self.checkBox_roi_reverse.setMinimumSize(QSize(0, 25))
        self.checkBox_roi_reverse.setMaximumSize(QSize(16777215, 25))
        self.checkBox_roi_reverse.setCheckable(True)

        self.gridLayout.addWidget(self.checkBox_roi_reverse, 10, 0, 1, 1)

        self.label_objectlength_fixed = QLabel(self.parameter)
        self.label_objectlength_fixed.setObjectName(u"label_objectlength_fixed")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_objectlength_fixed.sizePolicy().hasHeightForWidth())
        self.label_objectlength_fixed.setSizePolicy(sizePolicy1)
        self.label_objectlength_fixed.setMinimumSize(QSize(90, 20))
        self.label_objectlength_fixed.setMaximumSize(QSize(90, 20))
        self.label_objectlength_fixed.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_objectlength_fixed, 5, 0, 1, 1)

        self.btn_refer_obj_rest = QPushButton(self.parameter)
        self.btn_refer_obj_rest.setObjectName(u"btn_refer_obj_rest")
        sizePolicy.setHeightForWidth(self.btn_refer_obj_rest.sizePolicy().hasHeightForWidth())
        self.btn_refer_obj_rest.setSizePolicy(sizePolicy)
        self.btn_refer_obj_rest.setMinimumSize(QSize(92, 25))
        self.btn_refer_obj_rest.setMaximumSize(QSize(92, 25))
        self.btn_refer_obj_rest.setFont(font)

        self.gridLayout.addWidget(self.btn_refer_obj_rest, 3, 2, 1, 1)

        self.label_pixel_scale = QLabel(self.parameter)
        self.label_pixel_scale.setObjectName(u"label_pixel_scale")
        sizePolicy1.setHeightForWidth(self.label_pixel_scale.sizePolicy().hasHeightForWidth())
        self.label_pixel_scale.setSizePolicy(sizePolicy1)
        self.label_pixel_scale.setMinimumSize(QSize(90, 20))
        self.label_pixel_scale.setMaximumSize(QSize(90, 20))

        self.gridLayout.addWidget(self.label_pixel_scale, 7, 0, 1, 1)

        self.lineEdit_data1_Name = QLineEdit(self.parameter)
        self.lineEdit_data1_Name.setObjectName(u"lineEdit_data1_Name")

        self.gridLayout.addWidget(self.lineEdit_data1_Name, 33, 1, 1, 2)

        self.btn_show_image = QPushButton(self.parameter)
        self.btn_show_image.setObjectName(u"btn_show_image")
        sizePolicy.setHeightForWidth(self.btn_show_image.sizePolicy().hasHeightForWidth())
        self.btn_show_image.setSizePolicy(sizePolicy)
        self.btn_show_image.setMinimumSize(QSize(92, 25))
        self.btn_show_image.setMaximumSize(QSize(92, 25))
        self.btn_show_image.setFont(font)

        self.gridLayout.addWidget(self.btn_show_image, 18, 0, 1, 1)

        self.line_space2 = QFrame(self.parameter)
        self.line_space2.setObjectName(u"line_space2")
        self.line_space2.setMinimumSize(QSize(288, 1))
        self.line_space2.setMaximumSize(QSize(288, 1))
        self.line_space2.setAutoFillBackground(False)
        self.line_space2.setStyleSheet(u"background-color: rgb(113, 112, 111);")
        self.line_space2.setFrameShape(QFrame.Shape.HLine)
        self.line_space2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_space2, 19, 0, 1, 1)

        self.btn_analysis_area = QPushButton(self.parameter)
        self.btn_analysis_area.setObjectName(u"btn_analysis_area")
        sizePolicy.setHeightForWidth(self.btn_analysis_area.sizePolicy().hasHeightForWidth())
        self.btn_analysis_area.setSizePolicy(sizePolicy)
        self.btn_analysis_area.setMinimumSize(QSize(92, 25))
        self.btn_analysis_area.setMaximumSize(QSize(92, 25))
        self.btn_analysis_area.setFont(font)

        self.gridLayout.addWidget(self.btn_analysis_area, 13, 1, 1, 1)

        self.btn_roi_select = QPushButton(self.parameter)
        self.btn_roi_select.setObjectName(u"btn_roi_select")
        sizePolicy.setHeightForWidth(self.btn_roi_select.sizePolicy().hasHeightForWidth())
        self.btn_roi_select.setSizePolicy(sizePolicy)
        self.btn_roi_select.setMinimumSize(QSize(92, 25))
        self.btn_roi_select.setMaximumSize(QSize(92, 25))
        self.btn_roi_select.setFont(font)

        self.gridLayout.addWidget(self.btn_roi_select, 13, 0, 1, 1)

        self.btn_draw_hist2 = QPushButton(self.parameter)
        self.btn_draw_hist2.setObjectName(u"btn_draw_hist2")
        sizePolicy.setHeightForWidth(self.btn_draw_hist2.sizePolicy().hasHeightForWidth())
        self.btn_draw_hist2.setSizePolicy(sizePolicy)
        self.btn_draw_hist2.setMinimumSize(QSize(92, 25))
        self.btn_draw_hist2.setMaximumSize(QSize(92, 25))
        self.btn_draw_hist2.setFont(font)

        self.gridLayout.addWidget(self.btn_draw_hist2, 26, 1, 1, 1)

        self.lineEdit_xaxis_spacing = QLineEdit(self.parameter)
        self.lineEdit_xaxis_spacing.setObjectName(u"lineEdit_xaxis_spacing")
        sizePolicy.setHeightForWidth(self.lineEdit_xaxis_spacing.sizePolicy().hasHeightForWidth())
        self.lineEdit_xaxis_spacing.setSizePolicy(sizePolicy)
        self.lineEdit_xaxis_spacing.setMinimumSize(QSize(0, 25))
        self.lineEdit_xaxis_spacing.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_xaxis_spacing.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_xaxis_spacing, 30, 2, 1, 1)

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

        self.gridLayout.addWidget(self.label_objectlength_fixed_2, 5, 2, 1, 1)

        self.btn_load_data1 = QPushButton(self.parameter)
        self.btn_load_data1.setObjectName(u"btn_load_data1")
        sizePolicy.setHeightForWidth(self.btn_load_data1.sizePolicy().hasHeightForWidth())
        self.btn_load_data1.setSizePolicy(sizePolicy)
        self.btn_load_data1.setMinimumSize(QSize(92, 25))
        self.btn_load_data1.setMaximumSize(QSize(92, 25))
        self.btn_load_data1.setFont(font)

        self.gridLayout.addWidget(self.btn_load_data1, 21, 0, 1, 1)

        self.lineEdit_rgb_value = QLineEdit(self.parameter)
        self.lineEdit_rgb_value.setObjectName(u"lineEdit_rgb_value")
        sizePolicy.setHeightForWidth(self.lineEdit_rgb_value.sizePolicy().hasHeightForWidth())
        self.lineEdit_rgb_value.setSizePolicy(sizePolicy)
        self.lineEdit_rgb_value.setMinimumSize(QSize(0, 25))
        self.lineEdit_rgb_value.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_rgb_value.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_rgb_value, 20, 2, 1, 1)

        self.lineEdit_data2_Name = QLineEdit(self.parameter)
        self.lineEdit_data2_Name.setObjectName(u"lineEdit_data2_Name")

        self.gridLayout.addWidget(self.lineEdit_data2_Name, 34, 1, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 35, 1, 1, 1)

        self.btn_erase_clusters = QPushButton(self.parameter)
        self.btn_erase_clusters.setObjectName(u"btn_erase_clusters")
        sizePolicy.setHeightForWidth(self.btn_erase_clusters.sizePolicy().hasHeightForWidth())
        self.btn_erase_clusters.setSizePolicy(sizePolicy)
        self.btn_erase_clusters.setMinimumSize(QSize(92, 25))
        self.btn_erase_clusters.setMaximumSize(QSize(92, 25))
        self.btn_erase_clusters.setFont(font)

        self.gridLayout.addWidget(self.btn_erase_clusters, 16, 1, 1, 1)

        self.btn_particle_reset = QPushButton(self.parameter)
        self.btn_particle_reset.setObjectName(u"btn_particle_reset")
        sizePolicy.setHeightForWidth(self.btn_particle_reset.sizePolicy().hasHeightForWidth())
        self.btn_particle_reset.setSizePolicy(sizePolicy)
        self.btn_particle_reset.setMinimumSize(QSize(92, 25))
        self.btn_particle_reset.setMaximumSize(QSize(92, 25))
        self.btn_particle_reset.setFont(font)

        self.gridLayout.addWidget(self.btn_particle_reset, 12, 2, 1, 1)

        self.label_histogram_fixed = QLabel(self.parameter)
        self.label_histogram_fixed.setObjectName(u"label_histogram_fixed")
        self.label_histogram_fixed.setMinimumSize(QSize(180, 20))
        self.label_histogram_fixed.setMaximumSize(QSize(180, 20))

        self.gridLayout.addWidget(self.label_histogram_fixed, 25, 0, 1, 1)

        self.line_space1 = QFrame(self.parameter)
        self.line_space1.setObjectName(u"line_space1")
        self.line_space1.setMinimumSize(QSize(288, 1))
        self.line_space1.setMaximumSize(QSize(288, 1))
        self.line_space1.setAutoFillBackground(False)
        self.line_space1.setStyleSheet(u"background-color: rgb(113, 112, 111);")
        self.line_space1.setFrameShape(QFrame.Shape.HLine)
        self.line_space1.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_space1, 8, 0, 1, 1)

        self.label_data2_Name_fixed = QLabel(self.parameter)
        self.label_data2_Name_fixed.setObjectName(u"label_data2_Name_fixed")

        self.gridLayout.addWidget(self.label_data2_Name_fixed, 34, 0, 1, 1)

        self.label_rgbandhsv_fixxed = QLabel(self.parameter)
        self.label_rgbandhsv_fixxed.setObjectName(u"label_rgbandhsv_fixxed")
        self.label_rgbandhsv_fixxed.setMinimumSize(QSize(180, 20))
        self.label_rgbandhsv_fixxed.setMaximumSize(QSize(180, 20))

        self.gridLayout.addWidget(self.label_rgbandhsv_fixxed, 20, 0, 1, 2)

        self.btn_refer_obj_calculate = QPushButton(self.parameter)
        self.btn_refer_obj_calculate.setObjectName(u"btn_refer_obj_calculate")
        self.btn_refer_obj_calculate.setEnabled(False)
        sizePolicy.setHeightForWidth(self.btn_refer_obj_calculate.sizePolicy().hasHeightForWidth())
        self.btn_refer_obj_calculate.setSizePolicy(sizePolicy)
        self.btn_refer_obj_calculate.setMinimumSize(QSize(92, 25))
        self.btn_refer_obj_calculate.setMaximumSize(QSize(92, 25))
        self.btn_refer_obj_calculate.setFont(font)

        self.gridLayout.addWidget(self.btn_refer_obj_calculate, 6, 2, 1, 1)

        self.btn_show_contours_img = QPushButton(self.parameter)
        self.btn_show_contours_img.setObjectName(u"btn_show_contours_img")
        sizePolicy.setHeightForWidth(self.btn_show_contours_img.sizePolicy().hasHeightForWidth())
        self.btn_show_contours_img.setSizePolicy(sizePolicy)
        self.btn_show_contours_img.setMinimumSize(QSize(92, 25))
        self.btn_show_contours_img.setMaximumSize(QSize(92, 25))

        self.gridLayout.addWidget(self.btn_show_contours_img, 18, 1, 1, 1)

        self.btn_draw_hist = QPushButton(self.parameter)
        self.btn_draw_hist.setObjectName(u"btn_draw_hist")
        sizePolicy.setHeightForWidth(self.btn_draw_hist.sizePolicy().hasHeightForWidth())
        self.btn_draw_hist.setSizePolicy(sizePolicy)
        self.btn_draw_hist.setMinimumSize(QSize(92, 25))
        self.btn_draw_hist.setMaximumSize(QSize(92, 25))
        self.btn_draw_hist.setFont(font)

        self.gridLayout.addWidget(self.btn_draw_hist, 26, 0, 1, 1)

        self.label_objdect_ratio_fixed = QLabel(self.parameter)
        self.label_objdect_ratio_fixed.setObjectName(u"label_objdect_ratio_fixed")
        self.label_objdect_ratio_fixed.setMinimumSize(QSize(70, 20))
        self.label_objdect_ratio_fixed.setMaximumSize(QSize(70, 20))
        self.label_objdect_ratio_fixed.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_objdect_ratio_fixed, 7, 2, 1, 1)

        self.label_data1_Name_fixed = QLabel(self.parameter)
        self.label_data1_Name_fixed.setObjectName(u"label_data1_Name_fixed")

        self.gridLayout.addWidget(self.label_data1_Name_fixed, 33, 0, 1, 1)

        self.label_show_image_fixed = QLabel(self.parameter)
        self.label_show_image_fixed.setObjectName(u"label_show_image_fixed")
        self.label_show_image_fixed.setMinimumSize(QSize(180, 20))
        self.label_show_image_fixed.setMaximumSize(QSize(180, 20))

        self.gridLayout.addWidget(self.label_show_image_fixed, 17, 0, 1, 2)

        self.lineEdit_pixel_scale_value = QLineEdit(self.parameter)
        self.lineEdit_pixel_scale_value.setObjectName(u"lineEdit_pixel_scale_value")
        sizePolicy.setHeightForWidth(self.lineEdit_pixel_scale_value.sizePolicy().hasHeightForWidth())
        self.lineEdit_pixel_scale_value.setSizePolicy(sizePolicy)
        self.lineEdit_pixel_scale_value.setMinimumSize(QSize(0, 25))
        self.lineEdit_pixel_scale_value.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_pixel_scale_value.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_pixel_scale_value, 7, 1, 1, 1)

        self.btn_find_contours = QPushButton(self.parameter)
        self.btn_find_contours.setObjectName(u"btn_find_contours")
        self.btn_find_contours.setMinimumSize(QSize(92, 25))
        self.btn_find_contours.setMaximumSize(QSize(92, 25))

        self.gridLayout.addWidget(self.btn_find_contours, 16, 0, 1, 1)

        self.label_x_axis_spacing_fixed = QLabel(self.parameter)
        self.label_x_axis_spacing_fixed.setObjectName(u"label_x_axis_spacing_fixed")

        self.gridLayout.addWidget(self.label_x_axis_spacing_fixed, 30, 0, 1, 2)

        self.lineEdit_nums_bins = QLineEdit(self.parameter)
        self.lineEdit_nums_bins.setObjectName(u"lineEdit_nums_bins")
        self.lineEdit_nums_bins.setMinimumSize(QSize(0, 25))
        self.lineEdit_nums_bins.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_nums_bins.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_nums_bins, 29, 2, 1, 1)

        self.lineEdit_object_length = QLineEdit(self.parameter)
        self.lineEdit_object_length.setObjectName(u"lineEdit_object_length")
        sizePolicy.setHeightForWidth(self.lineEdit_object_length.sizePolicy().hasHeightForWidth())
        self.lineEdit_object_length.setSizePolicy(sizePolicy)
        self.lineEdit_object_length.setMinimumSize(QSize(0, 25))
        self.lineEdit_object_length.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_object_length.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_object_length, 5, 1, 1, 1)

        self.btn_draw_comparehist = QPushButton(self.parameter)
        self.btn_draw_comparehist.setObjectName(u"btn_draw_comparehist")
        sizePolicy.setHeightForWidth(self.btn_draw_comparehist.sizePolicy().hasHeightForWidth())
        self.btn_draw_comparehist.setSizePolicy(sizePolicy)
        self.btn_draw_comparehist.setMinimumSize(QSize(92, 25))
        self.btn_draw_comparehist.setMaximumSize(QSize(92, 25))
        self.btn_draw_comparehist.setFont(font)

        self.gridLayout.addWidget(self.btn_draw_comparehist, 26, 2, 1, 1)

        self.comboBox_histstate = QComboBox(self.parameter)
        self.comboBox_histstate.addItem("")
        self.comboBox_histstate.addItem("")
        self.comboBox_histstate.addItem("")
        self.comboBox_histstate.addItem("")
        self.comboBox_histstate.addItem("")
        self.comboBox_histstate.setObjectName(u"comboBox_histstate")
        sizePolicy.setHeightForWidth(self.comboBox_histstate.sizePolicy().hasHeightForWidth())
        self.comboBox_histstate.setSizePolicy(sizePolicy)
        self.comboBox_histstate.setMinimumSize(QSize(190, 25))
        self.comboBox_histstate.setMaximumSize(QSize(180, 25))
        self.comboBox_histstate.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_histstate.setMinimumContentsLength(6)

        self.gridLayout.addWidget(self.comboBox_histstate, 25, 1, 1, 2)

        self.comboBox_show_contour = QComboBox(self.parameter)
        self.comboBox_show_contour.addItem("")
        self.comboBox_show_contour.addItem("")
        self.comboBox_show_contour.setObjectName(u"comboBox_show_contour")
        sizePolicy.setHeightForWidth(self.comboBox_show_contour.sizePolicy().hasHeightForWidth())
        self.comboBox_show_contour.setSizePolicy(sizePolicy)
        self.comboBox_show_contour.setMinimumSize(QSize(180, 0))
        self.comboBox_show_contour.setMaximumSize(QSize(180, 25))
        self.comboBox_show_contour.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_show_contour.setMinimumContentsLength(6)

        self.gridLayout.addWidget(self.comboBox_show_contour, 15, 1, 1, 1)


        self.retranslateUi(ContentBar)

        QMetaObject.connectSlotsByName(ContentBar)
    # setupUi

    def retranslateUi(self, ContentBar):
        ContentBar.setWindowTitle(QCoreApplication.translate("ContentBar", u"Form", None))
        self.label_title_fixed.setText(QCoreApplication.translate("ContentBar", u"Physical Scale of the Image", None))
        self.btn_save_contours.setText(QCoreApplication.translate("ContentBar", u"Save Data1", None))
        self.labe_select_roi_fixed.setText(QCoreApplication.translate("ContentBar", u"Select Region of Interest", None))
        self.btn_load_data2.setText(QCoreApplication.translate("ContentBar", u"Load Data2", None))
        self.btn_refer_obj.setText(QCoreApplication.translate("ContentBar", u"Select", None))
        self.label_bins_fixed.setText(QCoreApplication.translate("ContentBar", u"Nums Bins\uff1a", None))
        self.label_contours.setText(QCoreApplication.translate("ContentBar", u"Find / Erase", None))
        self.checkBox_roi_reverse.setText(QCoreApplication.translate("ContentBar", u"Reverse", None))
        self.label_objectlength_fixed.setText(QCoreApplication.translate("ContentBar", u"Object length", None))
        self.btn_refer_obj_rest.setText(QCoreApplication.translate("ContentBar", u"Reset", None))
        self.label_pixel_scale.setText(QCoreApplication.translate("ContentBar", u"Pixel Scale:", None))
        self.lineEdit_data1_Name.setText(QCoreApplication.translate("ContentBar", u"None1", None))
        self.btn_show_image.setText(QCoreApplication.translate("ContentBar", u"Image", None))
        self.btn_analysis_area.setText(QCoreApplication.translate("ContentBar", u"Analysis", None))
        self.btn_roi_select.setText(QCoreApplication.translate("ContentBar", u"Select", None))
        self.btn_draw_hist2.setText(QCoreApplication.translate("ContentBar", u"Hist Data2", None))
        self.lineEdit_xaxis_spacing.setText(QCoreApplication.translate("ContentBar", u"-1", None))
        self.label_objectlength_fixed_2.setText(QCoreApplication.translate("ContentBar", u" mm ", None))
        self.btn_load_data1.setText(QCoreApplication.translate("ContentBar", u"Load Data1", None))
        self.lineEdit_rgb_value.setText(QCoreApplication.translate("ContentBar", u"-1", None))
        self.lineEdit_data2_Name.setText(QCoreApplication.translate("ContentBar", u"None2", None))
        self.btn_erase_clusters.setText(QCoreApplication.translate("ContentBar", u"Erase", None))
        self.btn_particle_reset.setText(QCoreApplication.translate("ContentBar", u"Reset", None))
        self.label_histogram_fixed.setText(QCoreApplication.translate("ContentBar", u"Histogram", None))
        self.label_data2_Name_fixed.setText(QCoreApplication.translate("ContentBar", u"Data 2 Name", None))
        self.label_rgbandhsv_fixxed.setText(QCoreApplication.translate("ContentBar", u" Contours Value\uff1a", None))
        self.btn_refer_obj_calculate.setText(QCoreApplication.translate("ContentBar", u"Calculate", None))
        self.btn_show_contours_img.setText(QCoreApplication.translate("ContentBar", u"Contours", None))
        self.btn_draw_hist.setText(QCoreApplication.translate("ContentBar", u"Hist Data1", None))
        self.label_objdect_ratio_fixed.setText(QCoreApplication.translate("ContentBar", u"mm/pixel", None))
        self.label_data1_Name_fixed.setText(QCoreApplication.translate("ContentBar", u"Data 1 Name", None))
        self.label_show_image_fixed.setText(QCoreApplication.translate("ContentBar", u"Show Image or Contours", None))
        self.lineEdit_pixel_scale_value.setText("")
        self.btn_find_contours.setText(QCoreApplication.translate("ContentBar", u"Find", None))
        self.label_x_axis_spacing_fixed.setText(QCoreApplication.translate("ContentBar", u"X-axis spacing(mm)\uff1a", None))
        self.lineEdit_nums_bins.setText(QCoreApplication.translate("ContentBar", u"-1", None))
        self.lineEdit_object_length.setText("")
        self.btn_draw_comparehist.setText(QCoreApplication.translate("ContentBar", u"Compare", None))
        self.comboBox_histstate.setItemText(0, QCoreApplication.translate("ContentBar", u"Surface with Percent", None))
        self.comboBox_histstate.setItemText(1, QCoreApplication.translate("ContentBar", u"Surface with Number", None))
        self.comboBox_histstate.setItemText(2, QCoreApplication.translate("ContentBar", u"Diameter with Percent", None))
        self.comboBox_histstate.setItemText(3, QCoreApplication.translate("ContentBar", u"Diameter with Number", None))
        self.comboBox_histstate.setItemText(4, "")

        self.comboBox_show_contour.setItemText(0, QCoreApplication.translate("ContentBar", u"Show Border", None))
        self.comboBox_show_contour.setItemText(1, QCoreApplication.translate("ContentBar", u"Show Fill", None))

        self.comboBox_show_contour.setCurrentText(QCoreApplication.translate("ContentBar", u"Show Border", None))
    # retranslateUi

