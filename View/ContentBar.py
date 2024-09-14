from UI.UI_ContentBar import Ui_ContentBar
from PySide6.QtWidgets import QWidget, QPushButton
from PySide6.QtCore import Signal, QEvent
from Controller.ImgEditCenter import imgEditCenter
from Model.AnalysisDataModel import analysisDataModel
from Model.MacroDefine import NONE_MODE, REF_MODE, ROI_MODE
import math


class ContentBar(QWidget, Ui_ContentBar):

    def __init__(self, widget):
        super().__init__()
        self.setupUi(widget)
        self.lstInitDisableBtn = [self.btn_refer_calculate, self.btn_roi_analysis]
        self.bindEvent()
        self.onInitUI()


    def onInitUI(self):
        for btn in self.lstInitDisableBtn:
            btn.setEnabled(False)
            self.updateButtonState(btn)


    def bindEvent(self):
        self.btn_refer_select.clicked.connect(self.onSetRefPoints)
        self.btn_refer_reset.clicked.connect(self.onResetRefPoints)
        self.btn_refer_calculate.clicked.connect(self.onCalRefObj)

        self.lineEdit_object_length.textChanged.connect(self.updateBtnRefStatus)
        self.lineEdit_pixel_scale_value.textChanged.connect(self.updateBtnROIStatus)

        self.btn_roi_select.clicked.connect(self.onSetROIPoints)
        self.btn_roi_reset.clicked.connect(self.onResetROIPoints)

    def onSetRefPoints(self):
        if not imgEditCenter.bImgExist:
            return
        currMode = imgEditCenter.currMode
        if currMode == NONE_MODE:
            self.btn_refer_select.setText("Finish")
            print('[ContentBar][onSetRefPoints] Set Mode: REF_MODE')
            imgEditCenter.clearTmpPoint()
            imgEditCenter.clearRefPoint()
            imgEditCenter.currMode = REF_MODE
        else:
            self.btn_refer_select.setText("Select")
            print('[ContentBar][onSetRefPoints] Set Mode: NONE_MODE')
            imgEditCenter.setRefPoints()
            imgEditCenter.drawLstPoint(bDrawPoint=True, bDrawLine=True)
            imgEditCenter.currMode = NONE_MODE
            self.updateBtnRefStatus()


    def onSetROIPoints(self):
        if not imgEditCenter.bImgExist:
            return
        print('[ContentBar][onSetRoi] Set ROI')
        currMode = imgEditCenter.currMode
        if currMode == NONE_MODE:
            self.btn_roi_select.setText("Finish")
            print('[ContentBar][onSetRoi] Set Mode: ROI_MODE')
            imgEditCenter.clearTmpPoint()
            imgEditCenter.clearROIPoint()
            imgEditCenter.currMode = ROI_MODE
        else:
            self.btn_roi_select.setText("Select")
            print('[ContentBar][onSetRoi] Set Mode: NONE_MODE')
            imgEditCenter.setROIPoints()
            imgEditCenter.drawLstPoint(bDrawPoint=True, bDrawLine=True)
            imgEditCenter.currMode = NONE_MODE
            self.updateBtnROIStatus()


    def onResetRefPoints(self):
        if not imgEditCenter.bImgExist:
            return
        print('[ContentBar][onResetRefPoints] Reset Ref Points')
        imgEditCenter.clearRefPoint()
        imgEditCenter.clearTmpPoint()
        self.btn_refer_select.setText("Select")
        self.lineEdit_pixel_scale_value.setText('')
        self.updateBtnRefStatus()
        self.restSrcImg()

    def onResetROIPoints(self):
        if not imgEditCenter.bImgExist:
            return
        print('[ContentBar][onResetROIPoints] Reset ROI Points')
        imgEditCenter.clearROIPoint()
        imgEditCenter.clearTmpPoint()
        self.btn_roi_select.setText("Select")
        self.updateBtnROIStatus()
        self.restSrcImg()

    def restSrcImg(self):
        if not imgEditCenter.bImgExist:
            return
        print('[ContentBar][restSrcImg] Reset Src Img')
        imgEditCenter.currMode = NONE_MODE
        imgEditCenter.restSrcImg()
        imgEditCenter.I_EVT_UPDATE_IMG.emit()

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
            self.btn_refer_select.setEnabled(False)
        else:
            print('[ContentBar][updateBtnRefStatus] Need two reference object point')
            bPoint = False
            self.btn_refer_select.setEnabled(True)

        self.updateButtonState(self.btn_refer_select)

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

    def updateBtnROIStatus(self):
        lstROIPoint = analysisDataModel.getLstROIPoint()
        if len(lstROIPoint) > 2:
            bPoint = True
            self.btn_roi_select.setEnabled(False)
        else:
            print('[ContentBar][updateBtnROIStatus] Need more than two ROI points')
            bPoint = False
            self.btn_roi_select.setEnabled(True)

        phyValue = self.lineEdit_pixel_scale_value.text()
        if phyValue != '':
            bPhyValue = True
        else:
            print('[ContentBar][updateBtnROIStatus] Need Pixel Scale')
            bPhyValue = False

        if bPoint and bPhyValue:
            self.btn_roi_analysis.setEnabled(True)
        else:
            self.btn_roi_analysis.setEnabled(False)

        self.updateButtonState(self.btn_roi_analysis)
        self.updateButtonState(self.btn_roi_select)


    def updateButtonState(self, btn):
        if btn.isEnabled():
            btn.setStyleSheet("color: black;")
        else:
            btn.setStyleSheet("color: gray;")



