from UI.UI_HistogramBar import Ui_HistogramBar
from PySide6.QtWidgets import QWidget, QFileDialog
from Controller.DataEditCenter import dataEditCenter
from Model.AnalysisDataModel import analysisDataModel
from Controller.ImgEditCenter import imgEditCenter
import Model.MacroDefine as MacroDefine
from PySide6.QtCore import Signal, Slot, QObject

class HistogramBar(QWidget, Ui_HistogramBar):
    def __init__(self, widget):
        super().__init__()
        self.setupUi(widget)
        self.dataEditCenter = dataEditCenter
        self.imgEditCenter = imgEditCenter
        self.analysisDataModel = analysisDataModel
        self.lstInitDisableBtn = [self.checkBox_show_data1, self.checkBox_show_data2]
        self.initSetting()

    def initSetting(self):
        for btn in self.lstInitDisableBtn:
            btn.setEnabled(False)
            self.updateButtonState(btn)
        self.bindEvent()
        self.dictDatatoLabel = {
            MacroDefine.INT_MIN         : [self.label_data1_min_value, self.label_data2_min_value],
            MacroDefine.INT_MAX         : [self.label_data1_max_value, self.label_data2_max_value],
            MacroDefine.INT_AVERAGE     : [self.label_data1_avg_value, self.label_data2_avg_value],
            MacroDefine.INT_STD         : [self.label_data1_std_value, self.label_data2_std_value],
            MacroDefine.INT_TOTAL       : [self.label_data1_total_value, self.label_data2_total_value],
            MacroDefine.STR_DATA_NAME   : [self.lineEdit_data1_name, self.lineEdit_data2_name],
            MacroDefine.INT_MEDIAN      : [self.label_data1_median_value, self.label_data2_median_value],
        }

    def bindEvent(self):
        self.lineEdit_data1_name.textChanged.connect(lambda: self.setDataName(0))
        self.lineEdit_data2_name.textChanged.connect(lambda: self.setDataName(1))
        self.btn_load_data1.clicked.connect(lambda: self.loadData(0))
        self.btn_load_data2.clicked.connect(lambda: self.loadData(1))
        self.btn_clear_data1.clicked.connect(lambda: self.dataEditCenter.clearData(0))
        self.btn_clear_data2.clicked.connect(lambda: self.dataEditCenter.clearData(1))
        self.btn_update_histogram.clicked.connect(self.updateHistogram)
        self.btn_change_mode.clicked.connect(lambda: self.setViewMode(MacroDefine.VIEW_ORIGIN_MODE))
        self.dataEditCenter.I_EVT_UPDATE_DATA_INFO.connect(self.prepareUpdateDataInfo)
        self.comboBox_show_info_type.currentIndexChanged.connect(self.updateUnitText)

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
        elif idx == 1:
            strName = self.lineEdit_data2_name.text()
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

        if idx == 0:
            self.checkBox_show_data1.setEnabled(bHasData)
            self.checkBox_show_data1.setChecked(bHasData)
            self.updateButtonState(self.checkBox_show_data1)
        elif idx == 1:
            self.checkBox_show_data2.setEnabled(bHasData)
            self.checkBox_show_data1.setChecked(bHasData)
            self.updateButtonState(self.checkBox_show_data2)

        self.updateDataInfo(idx, MacroDefine.DIAMETER_TYPE)

    def updateDataInfo(self, idx, dataType):
        dataItem = self.dataEditCenter.getSingleDataItem(idx)
        dataInfo = dataItem.getDataInfo(dataType)

        # dataInfo.average is a float, just want to show .3f
        avgValue = dataInfo.average
        strAvgValue = f'{avgValue:.3f} '
        self.dictDatatoLabel[MacroDefine.INT_AVERAGE][idx].setText(strAvgValue)

        medianValue = dataInfo.median
        strMedianValue = f'{medianValue:.3f} '
        self.dictDatatoLabel[MacroDefine.INT_MEDIAN][idx].setText(strMedianValue)

        stdValue = dataInfo.std
        strStdValue = f'{stdValue:.3f} '
        self.dictDatatoLabel[MacroDefine.INT_STD][idx].setText(strStdValue)

        minValue = dataInfo.min
        strMinValue = f'{minValue:.3f} '
        self.dictDatatoLabel[MacroDefine.INT_MIN][idx].setText(strMinValue)

        maxValue = dataInfo.max
        strMaxValue = f'{maxValue:.3f} '
        self.dictDatatoLabel[MacroDefine.INT_MAX][idx].setText(strMaxValue)

        strTotalValue = str(dataInfo.total)
        self.dictDatatoLabel[MacroDefine.INT_TOTAL][idx].setText(strTotalValue)

        strNameText = self.dictDatatoLabel[MacroDefine.STR_DATA_NAME][idx].text()
        if strNameText == '':
            strDataName = dataItem.strName
            self.dictDatatoLabel[MacroDefine.STR_DATA_NAME][idx].setText(strDataName)

    def updateHistogram(self):
        bIsShowData1    = self.checkBox_show_data1.isChecked()
        bIsShowData2    = self.checkBox_show_data2.isChecked()
        bShowAvg        = self.checkBox_show_avg.isChecked()
        bShowMedian     = self.checkBox_show_median.isChecked()
        bShowStd        = self.checkBox_show_std.isChecked()
        bShowCumLine    = self.checkBox_show_cumulative.isChecked()
        showInfoType    = int(self.comboBox_show_info_type.currentIndex())
        showHistType    = int(self.comboBox_show_hist_type.currentIndex())

        spacingValue = float(self.lineEdit_xaxis_spacing_value.text())
        minXValue = float(self.lineEdit_xaxis_min_value.text())
        maxXValue = float(self.lineEdit_xaxis_max_value.text())

        if bIsShowData1 and bIsShowData2:
            showType = MacroDefine.SHOW_HIST_TYPE_BOTH
        elif bIsShowData1:
            showType = MacroDefine.SHOW_HIST_TYPE_DATA1
        elif bIsShowData2:
            showType = MacroDefine.SHOW_HIST_TYPE_DATA2
        else:
            showType = MacroDefine.SHOW_HIST_TYPE_NONE
            return

        lstDataName = []

        if showType == MacroDefine.SHOW_HIST_TYPE_BOTH:
            strDATA1Name = self.dictDatatoLabel[MacroDefine.STR_DATA_NAME][0].text()
            strDATA2Name = self.dictDatatoLabel[MacroDefine.STR_DATA_NAME][1].text()
            lstDataName = [strDATA1Name, strDATA2Name]

        else:
            strDATAName = ''
            if showType == MacroDefine.SHOW_HIST_TYPE_DATA1:
                strDATAName = self.dictDatatoLabel[MacroDefine.STR_DATA_NAME][0].text()
            elif showType == MacroDefine.SHOW_HIST_TYPE_DATA2:
                strDATAName = self.dictDatatoLabel[MacroDefine.STR_DATA_NAME][1].text()

            lstDataName = [strDATAName]

        inputParam = {
            MacroDefine.INPUT_PARAM_INT_X_SPACING       : spacingValue,
            MacroDefine.INPUT_PARAM_INT_X_MIN           : minXValue,
            MacroDefine.INPUT_PARAM_INT_X_MAX           : maxXValue,
            MacroDefine.INPUT_PARAM_LST_NAME            : lstDataName,
            MacroDefine.INPUT_PARAM_BOOL_SHOW_AVG       : bShowAvg,
            MacroDefine.INPUT_PARAM_BOOL_SHOW_MEDIAN    : bShowMedian,
            MacroDefine.INPUT_PARAM_BOOL_SHOW_STD       : bShowStd,
            MacroDefine.INPUT_PARAM_BOOL_SHOW_CUMLINE   : bShowCumLine,
            MacroDefine.INPUT_PARAM_INT_INFO_TYPE       : showInfoType,
            MacroDefine.INPUT_PARAM_INT_HIST_TYPE       : showHistType
        }

        self.dataEditCenter.updateHistogram(showType, inputParam)

        if minXValue == -1:
            minXValue = self.dataEditCenter.minXValue

        if maxXValue == -1:
            maxXValue = self.dataEditCenter.maxXValue

        self.lineEdit_xaxis_min_value.setText(f'{minXValue:.3f} ')
        self.lineEdit_xaxis_max_value.setText(f'{maxXValue:.3f} ')

    def updateUnitText(self):
        showInfoType = int(self.comboBox_show_info_type.currentIndex())
        strUnitText = MacroDefine.dicStrUintText[showInfoType]
        lstSetUintLabel = [self.label_data_unit, self.label_x_axis_spacing_unit, self.label_x_axis_min_unit, self.label_x_axis_max_unit]
        for label in lstSetUintLabel:
            label.setText(strUnitText)

