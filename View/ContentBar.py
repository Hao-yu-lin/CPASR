from UI.UI_ContentBar import Ui_ContentBar
from PySide6.QtWidgets import QWidget, QPushButton
from PySide6.QtCore import Signal, QEvent
from Controller.ImgEditCenter import imgEditCenter
from Model.AnalysisDataModel import analysisDataModel
from Model.MacroDefine import NONE_MODE, REF_MODE, ROI_MODE, VIEW_ORIGIN_MODE, VIEW_MASK_MODE, VIEW_CONTOURS_MODE
import math


class ContentBar(QWidget, Ui_ContentBar):

    def __init__(self, widget):
        super().__init__()
        self.setupUi(widget)
        self.editCenter = imgEditCenter
        self.updateAllBtnStatus = [self.updateBtnViewStatus,
                                   self.updateBtnRefStatus,
                                   ]
        self.bindEvent()
        self.onInitUI()
        self.updateBtnViewStatus()


    def onInitUI(self):
        for fun in self.updateAllBtnStatus:
            fun()
        lstDisablebtn = [self.btn_show_contours, self.btn_roi_analysis]
        for btn in lstDisablebtn:
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
        self.btn_show_image.clicked.connect(lambda: self.setViewMode(VIEW_ORIGIN_MODE))
        self.btn_show_mask.clicked.connect(lambda: self.setViewMode(VIEW_MASK_MODE))

    def setViewMode(self, mode):
        self.editCenter.currViewMode = mode
        self.updateBtnViewStatus()


    def onSetRefPoints(self):
        if not self.editCenter.bImgExist:
            return
        currMode = self.editCenter.currMode

        if currMode == REF_MODE:
            self.btn_refer_select.setText("Select")
            print('[ContentBar][onSetRefPoints] Set Mode: NONE_MODE')
            self.editCenter.setRefPoints()
            lstRefPoint = analysisDataModel.getLstRefPoint()
            self.editCenter.drawLstPoint(lstRefPoint, bDrawPoint=True, bDrawLine=True)
            self.editCenter.currMode = NONE_MODE
            self.editCenter.prevMode = REF_MODE
            self.updateBtnRefStatus()
        else:
            self.btn_refer_select.setText("Finish")
            print('[ContentBar][onSetRefPoints] Set Mode: REF_MODE')
            self.editCenter.clearRefPoint()
            if self.editCenter.prevMode != REF_MODE:
                self.editCenter.clearTmpPoint()
                self.editCenter.setSrcImg()
            else:
                self.editCenter.drawTmpPoint()
            self.editCenter.currMode = REF_MODE

    def onSetROIPoints(self):
        if not self.editCenter.bImgExist:
            return
        print('[ContentBar][onSetRoi] Set ROI')
        currMode = self.editCenter.currMode

        if currMode == ROI_MODE:
            self.btn_roi_select.setText("Select")
            print('[ContentBar][onSetRoi] Set Mode: NONE_MODE')
            self.editCenter.setROIPoints()
            lstROIPoint = analysisDataModel.getLstROIPoint()
            self.editCenter.drawLstPoint(lstROIPoint, bDrawPoint=True, bDrawLine=True)
            self.editCenter.currMode = NONE_MODE
            self.editCenter.prevMode = ROI_MODE

        else:
            self.btn_roi_select.setText("Finish")
            print('[ContentBar][onSetRoi] Set Mode: ROI_MODE')
            self.editCenter.clearROIPoint()
            if self.editCenter.prevMode != ROI_MODE:
                self.editCenter.clearTmpPoint()
                self.editCenter.setSrcImg()
            else:
                self.editCenter.drawTmpPoint()
            self.editCenter.currMode = ROI_MODE

    def onResetRefPoints(self):
        if not self.editCenter.bImgExist:
            return
        print('[ContentBar][onResetRefPoints] Reset Ref Points')
        self.editCenter.clearRefPoint()
        self.editCenter.clearTmpPoint()
        self.btn_refer_select.setText("Select")
        self.lineEdit_pixel_scale_value.setText('')
        self.updateBtnRefStatus()
        self.restSrcImg()

    def onResetROIPoints(self):
        if not self.editCenter.bImgExist:
            return
        print('[ContentBar][onResetROIPoints] Reset ROI Points')
        self.editCenter.clearROIPoint()
        self.editCenter.clearTmpPoint()
        self.btn_roi_select.setText("Select")
        self.restSrcImg()

    def restSrcImg(self):
        if not self.editCenter.bImgExist:
            return
        print('[ContentBar][restSrcImg] Reset Src Img')
        self.editCenter.currMode = NONE_MODE
        self.editCenter.prevMode = NONE_MODE
        self.editCenter.restSrcImg()
        self.editCenter.I_EVT_UPDATE_IMG.emit()

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
        if self.editCenter.currViewMode == VIEW_MASK_MODE:
            self.btn_show_image.setEnabled(True)
            self.btn_show_contours.setEnabled(False)

            if self.editCenter.prevMode == ROI_MODE:
                self.btn_show_image.setText('Last Image')

        else:
            self.btn_show_image.setEnabled(True)
            self.btn_show_contours.setEnabled(False)
            self.btn_show_image.setText('Image')

        self.updateButtonState(self.btn_show_image)
        self.updateButtonState(self.btn_show_contours)

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
        res = analysisDataModel.findContours(threadhold)
        self.lineEdit_contours_value.setText(str(analysisDataModel.threshold))
        self.btn_show_contours.setEnabled(res)
        self.updateButtonState(self.btn_show_contours)
        self.editCenter.currViewMode = VIEW_CONTOURS_MODE
        self.updateBtnAnalysisStatus()

    def updateScaleValue(self, value):
        analysisDataModel.setScaleRefObj(float(value))
        self.updateBtnAnalysisStatus()


