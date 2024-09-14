from UI.UI_ContentBar import Ui_ContentBar
from PySide6.QtWidgets import QWidget, QPushButton
from PySide6.QtCore import Signal, QEvent
from Controller.ImgEditCenter import imgEditCenter, NONE_MODE, REF_MODE
from Model.AnalysisDataModel import analysisDataModel
import math


class ContentBar(QWidget, Ui_ContentBar):
    I_EVT_REF_POINTS = Signal()

    def __init__(self, widget):
        super().__init__()
        self.setupUi(widget)
        self.lstInitDisableBtn = [self.btn_refer_obj_calculate]
        self.bindEvent()
        self.onInitUI()


    def onInitUI(self):
        for btn in self.lstInitDisableBtn:
            btn.setEnabled(False)
            self.updateButtonState(btn)


    def bindEvent(self):
        self.btn_refer_obj.clicked.connect(self.onSetRefPoints)
        self.btn_refer_obj_rest.clicked.connect(self.onResetRefPoints)
        self.btn_refer_obj_calculate.clicked.connect(self.onCalRefObj)
        self.lineEdit_object_length.textChanged.connect(self.changeCalStatus)

    def onSetRefPoints(self):
        if not imgEditCenter.bImgExist:
            return
        currState = imgEditCenter.currMode
        if currState == NONE_MODE:
            self.btn_refer_obj.setText("Finish")
            imgEditCenter.currMode = REF_MODE
            imgEditCenter.clearTmpPint()
        else:
            self.btn_refer_obj.setText("Select")
            imgEditCenter.currMode = NONE_MODE
            imgEditCenter.setRefPoint()
            imgEditCenter.drawRefPoint(bDrawPoint=True, bDrawLine=True)
            self.changeCalStatus()
        self.I_EVT_REF_POINTS.emit()

    def onResetRefPoints(self):
        if not imgEditCenter.bImgExist:
            return
        print('[ContentBar][onResetRefPoints] Reset Ref Points')
        imgEditCenter.clearRefPoint()
        imgEditCenter.clearTmpPint()
        self.btn_refer_obj.setText("Select")
        self.changeCalStatus()
        self.restSrcImg()

    def restSrcImg(self):
        if not imgEditCenter.bImgExist:
            return
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

    def changeCalStatus(self):
        lstRefPoint = analysisDataModel.getLstRefPoint()
        if len(lstRefPoint) == 2:
            bPoint = True
        else:
            print('[ContentBar][changeCalStatus] Need two reference object point')
            bPoint = False

        phyValue = self.lineEdit_object_length.text()
        if phyValue != '':
            bPhyValue = True
        else:
            print('[ContentBar][changeCalStatus] Need actual distance')
            bPhyValue = False

        if bPoint and bPhyValue:
            self.btn_refer_obj_calculate.setEnabled(True)
        else:
            self.btn_refer_obj_calculate.setEnabled(False)

        self.updateButtonState(self.btn_refer_obj_calculate)

    def updateButtonState(self, btn):
        if btn.isEnabled():
            btn.setStyleSheet("color: black;")
        else:
            btn.setStyleSheet("color: gray;")

