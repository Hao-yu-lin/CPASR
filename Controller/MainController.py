import math
from Controller.MenuBarController import MenuBarController
from PySide6.QtCore import QObject, Slot
from Controller.ImgEditCenter import imgEditCenter
from Model.MacroDefine import LST_NEED_MOUSE_TRACKING


class MainController(QObject):
    def __init__(self, MainWindow):
        super().__init__()
        self.MainWindow = MainWindow
        self.MenuBarController = MenuBarController(self.MainWindow.menuBar)
        self.Viewer = self.MainWindow.viewer
        self.CntBar = self.MainWindow.contentBar
        self.editCenter = imgEditCenter
        self.bImgExist = False
        self.bindEvent()

    def bindEvent(self):
        self.MenuBarController.I_EVT_CREATE_FINISH.connect(self.decodeImg)
        self.Viewer.I_EVT_SCALE_CHANGE.connect(self.syncRatioToValue)
        self.MenuBarController.I_EVT_SCALE_CHANGE.connect(self.updateView)
        self.editCenter.I_EVT_SET_POINTS.connect(self.onSetPoints)
        self.editCenter.I_EVT_CHANGE_VIEW_MODE.connect(self.Viewer.changeView)

    @Slot()
    def decodeImg(self):
        self.editCenter.decodeImg(self.Viewer.initImg)
        self.MenuBarController.setScaleControllerState(bState=False)

    @Slot(int)
    def updateView(self, value):
        ratio = self.calValueToRate(value)
        self.Viewer.setScaleImg(ratio)
        self.Viewer.drawImg()


    @Slot()
    def syncRatioToValue(self):
        value = self.calRateToValue(self.Viewer.currentRatio)
        self.MenuBarController.setZoomValueRate(value, self.Viewer.currentRatio)

    """
           10%   ratio value = 0
           100%  ratio value = 50
           1000% ratio value = 100
           we get the formula that ratio rate = 10^((ratio_value-50)/50)
    """

    @staticmethod
    def calValueToRate(value):
        ratio = pow(10, (value - 50) / 50)
        return ratio

    @staticmethod
    def calRateToValue(rate):
        value = int(math.log(rate, 10) * 50 + 50)
        return value

    @Slot()
    def onSetPoints(self):
        if not self.editCenter.bImgExist:
            return

        if self.editCenter.currMode in LST_NEED_MOUSE_TRACKING:
            self.Viewer.label_view.setMouseTracking(True)
            self.Viewer.bindMouseEvent()
        else:
            self.Viewer.label_view.setMouseTracking(False)
            self.Viewer.unbindMouseEvent()
