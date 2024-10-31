from UI.UI_HistogramBar import Ui_HistogramBar
from PySide6.QtWidgets import QWidget, QFileDialog
from Controller.DataEditCenter import dataEditCenter
from Model.AnalysisDataModel import analysisDataModel
from Controller.ImgEditCenter import imgEditCenter
import Model.MacroDefine as MacroDefine
from PySide6.QtCore import Slot

class HistogramBar(QWidget, Ui_HistogramBar):
    def __init__(self, widget):
        super().__init__()
        self.setupUi(widget)
        self.dataEditCenter = dataEditCenter
        self.imgEditCenter = imgEditCenter
        self.analysisDataModel = analysisDataModel
        self.initSetting()

    def initSetting(self):
        self.bindEvent()
        self.dictDatatoLabel = {
            MacroDefine.STR_DATA_NAME   : [self.lineEdit_data1_name],
        }

    def bindEvent(self):
        self.lineEdit_data1_name.textChanged.connect(lambda: self.setDataName(0))
        self.btn_load_data1.clicked.connect(lambda: self.loadData(0))
        self.btn_clear_data1.clicked.connect(lambda: self.dataEditCenter.clearData(0))
        self.btn_update_histogram.clicked.connect(self.updateHistogram)
        self.btn_change_mode.clicked.connect(lambda: self.setViewMode(MacroDefine.VIEW_ORIGIN_MODE))
        self.dataEditCenter.I_EVT_UPDATE_DATA_INFO.connect(self.prepareUpdateDataInfo)
        self.comboBox_show_info_type.currentIndexChanged.connect(self.updateUnit)

    def setViewMode(self, mode):
        self.imgEditCenter.currViewMode = mode

    def updateButtonState(self, btn):
        if btn.isEnabled():
            btn.setStyleSheet("color: black;")
        else:
            btn.setStyleSheet("color: gray;")

    def setDataName(self, idx):
        if idx == 0:
            strName = self.lineEdit_data1_name.text()
        else:
            strName = ''
        self.dataEditCenter.setStrName(idx, strName)

    def loadData(self, idx):
        strFilePath, _ = QFileDialog.getOpenFileName(
            self,
            "Select Data",
            "./",
            "Image (*.csv)"
        )
        if not strFilePath:
            return
        self.dataEditCenter.loadData(idx, strFilePath)

    @Slot(int)
    def prepareUpdateDataInfo(self, idx):
        bHasData = self.dataEditCenter.bHasData(idx)
        self.updateDataInfo(idx)

    def updateDataInfo(self, idx):
        showInfoType = int(self.comboBox_show_info_type.currentIndex())
        dataItem = self.dataEditCenter.getSingleDataItem(idx)
        dataInfo = dataItem.getDataInfo(showInfoType)

        strNameText = self.dictDatatoLabel[MacroDefine.STR_DATA_NAME][idx].text()
        if strNameText == '':
            strDataName = dataItem.strName
            self.dictDatatoLabel[MacroDefine.STR_DATA_NAME][idx].setText(strDataName)

    def updateHistogram(self):
        bShowAvg        = self.checkBox_show_avg.isChecked()
        bShowBoxplot    = self.checkBox_show_boxplot.isChecked()
        bShowCumLine    = self.checkBox_show_cumulative.isChecked()
        bShowValue      = self.checkBox_show_value.isChecked()
        showInfoType    = int(self.comboBox_show_info_type.currentIndex())
        showHistType    = int(self.comboBox_show_hist_type.currentIndex())

        spacingValue = float(self.lineEdit_xaxis_spacing_value.text())
        minXValue = float(self.lineEdit_xaxis_min_value.text())
        maxXValue = float(self.lineEdit_xaxis_max_value.text())

        showType = MacroDefine.SHOW_HIST_TYPE_DATA1
        strDATAName = self.dictDatatoLabel[MacroDefine.STR_DATA_NAME][0].text()


        lstDataName = [strDATAName]


        # for D point
        lstShowCumulative = []
        bShowD1 = self.checkBox_show_D1.isChecked()
        if bShowD1:
            lstShowCumulative.append(int(self.lineEdit_show_D1_value.text()))
        bShowD2 = self.checkBox_show_D2.isChecked()
        if bShowD2:
            lstShowCumulative.append(int(self.lineEdit_show_D2_value.text()))
        bShowD3 = self.checkBox_show_D3.isChecked()
        if bShowD3:
            lstShowCumulative.append(int(self.lineEdit_show_D3_value.text()))
        bShowD4 = self.checkBox_show_D4.isChecked()
        if bShowD4:
            lstShowCumulative.append(int(self.lineEdit_show_D4_value.text()))
        bShowD5 = self.checkBox_show_D5.isChecked()
        if bShowD5:
            lstShowCumulative.append(int(self.lineEdit_show_D5_value.text()))
        bShowD6 = self.checkBox_show_D6.isChecked()
        if bShowD6:
            lstShowCumulative.append(int(self.lineEdit_show_D6_value.text()))

        inputParam = {
            MacroDefine.INPUT_PARAM_INT_X_SPACING       : spacingValue,
            MacroDefine.INPUT_PARAM_INT_X_MIN           : minXValue,
            MacroDefine.INPUT_PARAM_INT_X_MAX           : maxXValue,
            MacroDefine.INPUT_PARAM_LST_NAME            : lstDataName,
            MacroDefine.INPUT_PARAM_BOOL_SHOW_AVG       : bShowAvg,
            MacroDefine.INPUT_PARAM_BOOL_SHOW_BOXPLOT   : bShowBoxplot,
            MacroDefine.INPUT_PARAM_BOOL_SHOW_CUMLINE   : bShowCumLine,
            MacroDefine.INPUT_PARAM_INT_INFO_TYPE       : showInfoType,
            MacroDefine.INPUT_PARAM_INT_HIST_TYPE       : showHistType,
            MacroDefine.INPUT_PARAM_BOOL_SHOW_VALUE     : bShowValue,
            MacroDefine.INPUT_PARAM_LST_SHOW_CUMULATIVE : lstShowCumulative,
        }

        self.dataEditCenter.updateHistogram(showType, inputParam)

        if minXValue == -1:
            minXValue = self.dataEditCenter.minXValue

        if maxXValue == -1:
            maxXValue = self.dataEditCenter.maxXValue

        self.lineEdit_xaxis_min_value.setText(f'{minXValue:.3f} ')
        self.lineEdit_xaxis_max_value.setText(f'{maxXValue:.3f} ')

    def updateUnit(self):
        showInfoType = int(self.comboBox_show_info_type.currentIndex())
        strUnitText = MacroDefine.dicStrUintText[showInfoType]
        lstSetUintLabel = [self.label_data_unit, self.label_x_axis_spacing_unit, self.label_x_axis_min_unit, self.label_x_axis_max_unit]
        for label in lstSetUintLabel:
            label.setText(strUnitText)

        if self.dataEditCenter.bHasData(0):
            self.updateDataInfo(0)
        if self.dataEditCenter.bHasData(1):
            self.updateDataInfo(1)
