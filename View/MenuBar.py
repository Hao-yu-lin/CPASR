from UI.UI_MenuBar import Ui_MenuBar
from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Signal, QEvent
import math


class MenuBar(QWidget, Ui_MenuBar):
    I_EVT_SEL_IMG = Signal(str)
    I_EVT_SCALE_CHANGE = Signal(int)

    def __init__(self, widget):
        super().__init__()
        self.setupUi(widget)
        self.lstInitDisableBtn = [self.btn_save_image, self.btn_shadow_removal]
        self.initSetting()
        self.bindEvent()

    def initSetting(self):
        self.slider_zoom.setValue(0)
        self.label_ratio.setText(f"Ratio：{0} %")
        self.setScaleControllerState(bState=True)
        for btn in self.lstInitDisableBtn:
            self.updateButtonState(btn)



    def setScaleControllerState(self, bState=True):
        self.slider_zoom.setDisabled(bState)
        self.btn_zoom_out.setDisabled(bState)
        self.btn_zoom_in.setDisabled(bState)

    def bindEvent(self):
        self.btn_open_img.clicked.connect(self.openImg)
        self.btn_zoom_out.clicked.connect(lambda: self.onZoomChange(-5))
        self.btn_zoom_in.clicked.connect(lambda: self.onZoomChange(5))
        self.slider_zoom.sliderReleased.connect(self.onSliderBarChange)
        self.slider_zoom.installEventFilter(self)


    def openImg(self):
        filePath, _ = QFileDialog.getOpenFileName(
            self,
            "Select Image",
            "./",
            "Image (*.png *.jpg *.jpeg);;All Files(*)"
        )
        self.I_EVT_SEL_IMG.emit(filePath)

    def setZoomValueRate(self, value, ratio):
        self.slider_zoom.setValue(value)
        self.label_ratio.setText(f"Ratio：{int(100 * ratio)} %")

    def onZoomChange(self, v):
        oldValue = self.slider_zoom.value()
        value = min(100, max(0, oldValue + v))
        self.slider_zoom.setValue(value)
        ratio = self.calValueToRate(value)
        self.setZoomValueRate(value, ratio)
        self.I_EVT_SCALE_CHANGE.emit(value)

    def onSliderBarChange(self):
        value = self.slider_zoom.value()
        ratio = self.calValueToRate(value)
        self.setZoomValueRate(value, ratio)
        self.I_EVT_SCALE_CHANGE.emit(value)

    @staticmethod
    def calValueToRate(value):
        ratio = pow(10, (value - 50) / 50)
        return ratio

    @staticmethod
    def calRateToValue(rate):
        value = int(math.log(rate, 10) * 50 + 50)
        return value


    #Event Filter
    def eventFilter(self, source, event):
        if (event.type() == QEvent.Wheel and
                source is self.slider_zoom):
            return True
        return super(MenuBar, self).eventFilter(source, event)

    def updateButtonState(self, btn):
        if btn.isEnabled():
            btn.setStyleSheet("color: black;")
        else:
            btn.setStyleSheet("color: gray;")

