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
        self.lstCheckShowData = [False, False, False, False, False]

    def initSetting(self):
        self.bindEvent()
        self.dictDatatoLabel = {
            MacroDefine.STR_DATA_NAME   : self.lineEdit_data1_name,
            MacroDefine.INT_AVERAGE     : self.label_data1_avg_value,
            MacroDefine.INT_MIN         : self.label_data1_min_value,
            MacroDefine.INT_MAX         : self.label_data1_max_value,
            MacroDefine.INT_STD         : self.label_data1_std_value,
            MacroDefine.INT_TOTAL       : self.label_data1_total_value,
            MacroDefine.INT_MEDIAN      : self.label_data1_median_value,
            MacroDefine.BOOL_SHOW_DATA  : self.checkBox_show_data,
        }

    def bindEvent(self):
        self.btn_load_data1.clicked.connect(self.loadData)
        self.btn_clear_data1.clicked.connect(self.clearData)
        self.btn_update_histogram.clicked.connect(self.updateHistogram)
        self.btn_update_name.clicked.connect(self.setDataName)
        self.btn_change_mode.clicked.connect(lambda: self.setViewMode(MacroDefine.VIEW_ORIGIN_MODE))
        self.dataEditCenter.I_EVT_UPDATE_DATA_INFO.connect(self.prepareUpdateDataInfo)
        self.comboBox_show_info_type.currentIndexChanged.connect(self.updateUnit)
        self.comboBox_current_data.currentIndexChanged.connect(self.changeDataInfo)
        self.checkBox_show_data.clicked.connect(self.updateShowData)

    def setViewMode(self, mode):
        self.imgEditCenter.currViewMode = mode

    def clearData(self):
        idx = self.comboBox_current_data.currentIndex()
        self.dataEditCenter.clearData(idx)
        self.updateDataInfo(idx)
        self.updateHistogram()


    def updateButtonState(self, btn):
        if btn.isEnabled():
            btn.setStyleSheet("color: black;")
        else:
            btn.setStyleSheet("color: gray;")

    def setDataName(self):
        strName = self.lineEdit_data1_name.text()
        idx = self.comboBox_current_data.currentIndex()
        self.dataEditCenter.setStrName(idx, strName)

    def loadData(self):
        strFilePath, _ = QFileDialog.getOpenFileName(
            self,
            "Select Data",
            "./",
            "Image (*.csv)"
        )
        if not strFilePath:
            return
        idx = self.comboBox_current_data.currentIndex()
        self.dataEditCenter.loadData(idx, strFilePath)
        self.updateHistogram()

    @Slot(int)
    def prepareUpdateDataInfo(self, idx):
        bHasData = self.dataEditCenter.bHasData(idx)
        self.updateDataInfo(idx)

    def updateDataInfo(self, idx):
        showInfoType = int(self.comboBox_show_info_type.currentIndex())
        dataItem = self.dataEditCenter.getSingleDataItem(idx)
        dataInfo = dataItem.getDataInfo(showInfoType)

        strNameText = self.dictDatatoLabel[MacroDefine.STR_DATA_NAME].text()
        if strNameText == '':
            strDataName = dataItem.strName if dataItem.strName != '' else f'Data {idx + 1}'
            self.dictDatatoLabel[MacroDefine.STR_DATA_NAME].setText(strDataName)

        self.dictDatatoLabel[MacroDefine.INT_AVERAGE].setText(f'{dataInfo.average:.3f}')
        self.dictDatatoLabel[MacroDefine.INT_MIN].setText(f'{dataInfo.min:.3f}')
        self.dictDatatoLabel[MacroDefine.INT_MAX].setText(f'{dataInfo.max:.3f}')
        self.dictDatatoLabel[MacroDefine.INT_STD].setText(f'{dataInfo.std:.3f}')
        self.dictDatatoLabel[MacroDefine.INT_TOTAL].setText(f'{dataInfo.total:.3f}')
        self.dictDatatoLabel[MacroDefine.INT_MEDIAN].setText(f'{dataInfo.median:.3f}')
        self.dictDatatoLabel[MacroDefine.BOOL_SHOW_DATA].setChecked(self.lstCheckShowData[idx])
        self.updateButtonMultiData()
        pass

    def updateHistogram(self):
        bShowAvg        = self.checkBox_show_avg.isChecked()
        bShowBoxplot    = self.checkBox_show_box_plot.isChecked()
        bShowCumLine    = self.checkBox_show_cumulative.isChecked()
        bShowHistValue  = self.checkBox_show_hist_value.isChecked()
        bShowBoxValue   = self.checkBox_show_box_value.isChecked()
        showInfoType    = int(self.comboBox_show_info_type.currentIndex())
        showHistType    = int(self.comboBox_show_hist_type.currentIndex())

        spacingValue = float(self.lineEdit_xaxis_spacing_value.text())
        minXValue = float(self.lineEdit_xaxis_min_value.text())
        maxXValue = float(self.lineEdit_xaxis_max_value.text())

        if self.checkBox_show_multi_data.isChecked():
            showType = MacroDefine.SHOW_HIST_TYPE_BOTH
        else:
            showType = MacroDefine.SHOW_HIST_TYPE_DATA1

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
            MacroDefine.INPUT_PARAM_BOOL_SHOW_AVG       : bShowAvg,
            MacroDefine.INPUT_PARAM_BOOL_SHOW_BOXPLOT   : bShowBoxplot,
            MacroDefine.INPUT_PARAM_BOOL_SHOW_CUMLINE   : bShowCumLine,
            MacroDefine.INPUT_PARAM_INT_INFO_TYPE       : showInfoType,
            MacroDefine.INPUT_PARAM_INT_HIST_TYPE       : showHistType,
            MacroDefine.INPUT_PARAM_BOOL_SHOW_HIST_VALUE: bShowHistValue,
            MacroDefine.INPUT_PARAM_BOOL_SHOW_BOX_VALUE : bShowBoxValue,
            MacroDefine.INPUT_PARAM_LST_SHOW_CUMULATIVE : lstShowCumulative,
            MacroDefine.INPUT_PARAM_INT_DATA_INDEX      : self.comboBox_current_data.currentIndex(),
            MacroDefine.INPUT_PARAM_LST_SHOW_DATA       : self.lstCheckShowData,
        }

        self.dataEditCenter.updateHistogram(showType, inputParam)

        if minXValue == -1:
            minXValue = self.dataEditCenter.minXValue

        if maxXValue == -1:
            maxXValue = self.dataEditCenter.maxXValue

        self.lineEdit_xaxis_min_value.setText(f'{minXValue:.3f} ')
        self.lineEdit_xaxis_max_value.setText(f'{maxXValue:.3f} ')

        if spacingValue == -1:
            if showInfoType == MacroDefine.DIAMETER_TYPE:
                spacingValue = 10
            elif showInfoType == MacroDefine.AREA_TYPE:
                spacingValue = 0.01
            self.lineEdit_xaxis_spacing_value.setText(f'{spacingValue:.3f} ')

        idx = self.comboBox_current_data.currentIndex()
        self.updateDataInfo(idx)

    def updateUnit(self):
        showInfoType = int(self.comboBox_show_info_type.currentIndex())
        strUnitText = MacroDefine.dicStrUintText[showInfoType]
        lstSetUintLabel = [self.label_data_unit, self.label_x_axis_spacing_unit, self.label_x_axis_min_unit, self.label_x_axis_max_unit]
        for label in lstSetUintLabel:
            label.setText(strUnitText)
        self.changeDataInfo()
        self.lineEdit_xaxis_spacing_value.setText('-1')
        self.lineEdit_xaxis_min_value.setText('-1')
        self.lineEdit_xaxis_max_value.setText('-1')
        # if self.dataEditCenter.bHasData(1):
        #     self.updateDataInfo(1)

    def changeDataInfo(self):
        idx = self.comboBox_current_data.currentIndex()
        self.dictDatatoLabel[MacroDefine.STR_DATA_NAME].setText('')
        if self.dataEditCenter.bHasData(idx):
            self.updateDataInfo(idx)

        else:
            self.dictDatatoLabel[MacroDefine.STR_DATA_NAME].setText(f'Data {idx + 1}')
            self.dictDatatoLabel[MacroDefine.INT_AVERAGE].setText('-1')
            self.dictDatatoLabel[MacroDefine.INT_MIN].setText('-1')
            self.dictDatatoLabel[MacroDefine.INT_MAX].setText('-1')
            self.dictDatatoLabel[MacroDefine.INT_STD].setText('-1')
            self.dictDatatoLabel[MacroDefine.INT_TOTAL].setText('-1')
            self.dictDatatoLabel[MacroDefine.INT_MEDIAN].setText('-1')
            self.dictDatatoLabel[MacroDefine.BOOL_SHOW_DATA].setChecked(False)
        self.updateHistogram()

    def updateShowData(self):
        idx = self.comboBox_current_data.currentIndex()
        self.lstCheckShowData[idx] = self.checkBox_show_data.isChecked()
        self.updateButtonMultiData()
        pass

    def updateButtonMultiData(self):
        count = 0
        for i in range(5):
            if self.dataEditCenter.bHasData(i):
                count += 1

        if count > 1 and self.lstCheckShowData.count(True) > 1:
            self.checkBox_show_multi_data.setEnabled(True)
        else:
            self.checkBox_show_multi_data.setChecked(False)
            self.checkBox_show_multi_data.setEnabled(False)

        self.updateButtonState(self.checkBox_show_multi_data)
