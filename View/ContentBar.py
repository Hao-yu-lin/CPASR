from UI.UI_ContentBar import Ui_ContentBar
from PySide6.QtWidgets import QWidget, QPushButton
from PySide6.QtCore import Signal, QEvent
from Controller.ImgEditCenter import imgEditCenter
from Model.AnalysisDataModel import analysisDataModel
import Model.MacroDefine as MacroDefine
import math


class ContentBar(QWidget, Ui_ContentBar):
    I_EVT_ENABLE_SAVE_DATA = Signal(bool)
    def __init__(self, widget):
        super().__init__()
        self.setupUi(widget)
        self.imgEditCenter = imgEditCenter
        self.updateAllBtnStatus = [self.updateBtnViewStatus,
                                   self.updateBtnRefStatus,
                                   ]
        self.bindEvent()
        self.onInitUI()
        self.updateBtnViewStatus()


    def onInitUI(self):
        for fun in self.updateAllBtnStatus:
            fun()
        self.lstROIDisablebtn = [self.btn_show_contours, self.btn_roi_analysis, self.btn_contours_eraser]
        for btn in self.lstROIDisablebtn:
            btn.setEnabled(False)
            self.updateButtonState(btn)


    def bindEvent(self):
        self.btn_refer_select.clicked.connect(self.onSetRefPoints)
        self.btn_refer_reset.clicked.connect(self.onResetRefPoints)
        self.btn_refer_calculate.clicked.connect(self.onCalRefObj)

        self.lineEdit_object_length.textChanged.connect(self.updateBtnRefStatus)
        self.lineEdit_pixel_scale_value.textChanged.connect(self.updateScaleValue)

        self.btn_contours_find.clicked.connect(self.findContours)
        self.btn_roi_select.clicked.connect(self.onSetROIPoints)
        self.btn_show_image.clicked.connect(lambda: self.setViewMode(MacroDefine.VIEW_ORIGIN_MODE))
        self.btn_show_mask.clicked.connect(lambda: self.setViewMode(MacroDefine.VIEW_MASK_MODE))
        self.btn_show_contours.clicked.connect(lambda: self.setViewMode(MacroDefine.VIEW_CONTOURS_MODE))
        self.btn_change_mode.clicked.connect(lambda: self.setViewMode(MacroDefine.VIEW_HISTOGRAM_MODE))
        self.btn_roi_analysis.clicked.connect(self.analysisContours)

        self.btn_contours_eraser.clicked.connect(self.onEraseContours)
        self.btn_roi_reset.clicked.connect(self.onROIReset)
        self.checkBox_roi_reverse.stateChanged.connect(self.reverseMask)

    def setViewMode(self, mode):
        self.imgEditCenter.currViewMode = mode
        self.updateBtnViewStatus()


    def onSetRefPoints(self):
        if not self.imgEditCenter.bImgExist:
            return
        currMode = self.imgEditCenter.currMode

        if currMode == MacroDefine.REF_MODE:
            self.btn_refer_select.setText("Select")
            print('[ContentBar][onSetRefPoints] Set Mode: NONE_MODE')
            self.imgEditCenter.setRefPoints()
            lstRefPoint = analysisDataModel.getLstRefPoint()
            self.imgEditCenter.drawLstPoint(lstRefPoint, bDrawPoint=True, bDrawLine=True)
            self.imgEditCenter.currMode = MacroDefine.NONE_MODE
            self.imgEditCenter.prevMode = MacroDefine.REF_MODE
            self.updateBtnRefStatus()
        else:
            self.btn_refer_select.setText("Finish")
            print('[ContentBar][onSetRefPoints] Set Mode: REF_MODE')
            self.imgEditCenter.clearRefPoint()
            if self.imgEditCenter.prevMode != MacroDefine.REF_MODE:
                self.imgEditCenter.clearTmpPoint()
                self.imgEditCenter.setSrcImg()
            else:
                self.imgEditCenter.drawTmpPoint()
            self.imgEditCenter.currMode = MacroDefine.REF_MODE

    def onSetROIPoints(self):
        if not self.imgEditCenter.bImgExist:
            return
        print('[ContentBar][onSetRoi] Set ROI')
        currMode = self.imgEditCenter.currMode

        if currMode == MacroDefine.ROI_MODE:
            self.btn_roi_select.setText("Select")
            print('[ContentBar][onSetRoi] Set Mode: NONE_MODE')
            self.imgEditCenter.setROIPoints()
            lstROIPoint = analysisDataModel.getLstROIPoint()
            self.imgEditCenter.drawLstPoint(lstROIPoint, bDrawPoint=True, bDrawLine=True)
            self.imgEditCenter.currMode = MacroDefine.NONE_MODE
            self.imgEditCenter.prevMode = MacroDefine.ROI_MODE

        else:
            self.btn_roi_select.setText("Finish")
            print('[ContentBar][onSetRoi] Set Mode: ROI_MODE')
            self.imgEditCenter.clearROIPoint()
            if self.imgEditCenter.prevMode != MacroDefine.ROI_MODE:
                self.imgEditCenter.clearTmpPoint()
                self.imgEditCenter.setSrcImg()
            else:
                self.imgEditCenter.drawTmpPoint()
            self.imgEditCenter.currMode = MacroDefine.ROI_MODE

    def onResetRefPoints(self):
        if not self.imgEditCenter.bImgExist:
            return
        print('[ContentBar][onResetRefPoints] Reset Ref Points')
        self.imgEditCenter.clearRefPoint()
        self.imgEditCenter.clearTmpPoint()
        self.btn_refer_select.setText("Select")
        self.lineEdit_pixel_scale_value.setText('')
        self.updateBtnRefStatus()
        self.restSrcImg()

    def onResetROIPoints(self):
        if not self.imgEditCenter.bImgExist:
            return
        print('[ContentBar][onResetROIPoints] Reset ROI Points')
        self.imgEditCenter.clearROIPoint()
        self.imgEditCenter.clearTmpPoint()
        self.imgEditCenter.clearContours()
        self.btn_roi_select.setText("Select")
        self.btn_contours_eraser.setText("Eraser")
        self.btn_contours_find.setText("Find")
        self.label_number_contours.setText('0')

        for btn in self.lstROIDisablebtn:
            btn.setEnabled(False)
            self.updateButtonState(btn)

        self.restSrcImg()

    def restSrcImg(self):
        if not self.imgEditCenter.bImgExist:
            return
        print('[ContentBar][restSrcImg] Reset Src Img')
        self.imgEditCenter.currMode = MacroDefine.NONE_MODE
        self.imgEditCenter.prevMode = MacroDefine.NONE_MODE
        self.imgEditCenter.restSrcImg()
        self.imgEditCenter.I_EVT_UPDATE_IMG.emit()

    def onCalRefObj(self):
        lstRefPoint = analysisDataModel.getLstRefPoint()
        if len(lstRefPoint) < 2:
            print('[ContentBar][onCalRefObj] Need two reference object point')
            return

        actualDist = self.lineEdit_object_length.text()
        if actualDist == '':
            print('[ContentBar][onCalRefObj] Need actual distance')
            return

        actualDist = float(actualDist)

        x1, y1 = lstRefPoint[0]
        x2, y2 = lstRefPoint[1]
        refPixelDis = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        scalRefObj = actualDist / refPixelDis

        analysisDataModel.setScaleRefObj(scalRefObj)
        text = f"{scalRefObj:.3f}"
        self.lineEdit_pixel_scale_value.setText(text)

    def updateBtnRefStatus(self):
        lstRefPoint = analysisDataModel.getLstRefPoint()
        if len(lstRefPoint) == 2:
            bPoint = True
        else:
            print('[ContentBar][updateBtnRefStatus] Need two reference object point')
            bPoint = False

        phyValue = self.lineEdit_object_length.text()
        if phyValue != '':
            bPhyValue = True
        else:
            print('[ContentBar][updateBtnRefStatus] Need actual distance')
            bPhyValue = False

        if bPoint and bPhyValue:
            self.btn_refer_calculate.setEnabled(True)

        else:
            self.btn_refer_calculate.setEnabled(False)

        self.updateButtonState(self.btn_refer_calculate)

    def updateBtnViewStatus(self):
        if self.imgEditCenter.currViewMode == MacroDefine.VIEW_ORIGIN_MODE and self.imgEditCenter.currMode == MacroDefine.NONE_MODE:
            self.btn_show_image.setText('Image')
        elif self.imgEditCenter.currViewMode == MacroDefine.VIEW_HISTOGRAM_MODE:
            self.btn_show_image.setText('Image')
        else:
            self.btn_show_image.setText('Last Image')

        self.updateButtonState(self.btn_show_image)


    def updateBtnAnalysisStatus(self):
        bCanAnalysis = analysisDataModel.bCanAnalysis()
        self.btn_roi_analysis.setEnabled(bCanAnalysis)
        self.updateButtonState(self.btn_roi_analysis)


    def updateButtonState(self, btn):
        if btn.isEnabled():
            btn.setStyleSheet("color: black;")
        else:
            btn.setStyleSheet("color: gray;")

    def findContours(self):
        print('[ContentBar][findContours] Find Contours Start')
        threadhold = int(self.lineEdit_contours_value.text())
        bReverse = self.checkBox_roi_reverse.isChecked()
        res = analysisDataModel.findContours(threadhold, bReverse)

        lstSyncBtn = [self.btn_show_contours, self.btn_contours_eraser]

        self.label_number_contours.setText(str(analysisDataModel.numContours))
        self.lineEdit_contours_value.setText(str(analysisDataModel.threshold))

        for btn in lstSyncBtn:
            btn.setEnabled(res)
            self.updateButtonState(btn)

        self.imgEditCenter.currMode = MacroDefine.NONE_MODE
        self.imgEditCenter.currViewMode = MacroDefine.VIEW_CONTOURS_MODE
        self.updateBtnAnalysisStatus()

    def updateScaleValue(self, value):
        if not value:
            value = -1

        analysisDataModel.setScaleRefObj(float(value))
        self.updateBtnAnalysisStatus()

    def analysisContours(self):
        analysisDataModel.analysisContours()
        self.setViewMode(MacroDefine.VIEW_HISTOGRAM_MODE)
        self.I_EVT_ENABLE_SAVE_DATA.emit(True)

    def onEraseContours(self):
        if not self.imgEditCenter.bImgExist:
            return

        lstSyncBtn = [self.btn_show_contours, self.btn_roi_analysis, self.btn_contours_find]
        if self.imgEditCenter.currMode != MacroDefine.DEL_MODE:
            self.imgEditCenter.currMode = MacroDefine.DEL_MODE
            self.btn_contours_eraser.setText('Finish')
            for btn in lstSyncBtn:
                btn.setEnabled(False)
                self.updateButtonState(btn)
        else:
            self.imgEditCenter.currMode = MacroDefine.NONE_MODE
            self.btn_contours_eraser.setText('Eraser')
            for btn in lstSyncBtn:
                btn.setEnabled(True)
                self.updateButtonState(btn)

    def onROIReset(self):
        self.onResetROIPoints()
        self.imgEditCenter.currViewMode = MacroDefine.VIEW_ORIGIN_MODE
        self.updateBtnViewStatus()
        self.updateBtnAnalysisStatus()
        self.imgEditCenter.I_EVT_UPDATE_IMG.emit()

    def reverseMask(self):
        self.imgEditCenter.bReverseMask = self.checkBox_roi_reverse.isChecked()