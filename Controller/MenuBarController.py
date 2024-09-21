from PySide6.QtCore import QObject, Slot, Signal
from Model.ImgDataModel import imgManager


class MenuBarController(QObject):
    I_EVT_CREATE_FINISH = Signal()
    I_EVT_SCALE_CHANGE = Signal(int)

    def __init__(self, MenuBar):
        super().__init__()
        self.MenuBar = MenuBar
        self.value = -1
        self.bindEvent()

    def bindEvent(self):
        self.MenuBar.I_EVT_SEL_IMG.connect(self.createImgData)
        self.MenuBar.I_EVT_SCALE_CHANGE.connect(self.updateView)

    @Slot(str)
    def createImgData(self, filePath):
        imgManager.createImgData(filePath)
        self.I_EVT_CREATE_FINISH.emit()

    def setZoomValueRate(self, value, ratio):
        self.MenuBar.setZoomValueRate(value, ratio)

    @Slot(int)
    def updateView(self, value):
        self.I_EVT_SCALE_CHANGE.emit(value)

    def setScaleControllerState(self, bState=True):
        self.MenuBar.setScaleControllerState(bState=bState)

