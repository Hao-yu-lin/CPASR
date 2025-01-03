import math
from Controller.MenuBarController import MenuBarController
from PySide6.QtCore import QObject, Slot
from Controller.ImgEditCenter import imgEditCenter
import Model.MacroDefine as MacroDefine


class MainController(QObject):
    def __init__(self, MainWindow):
        super().__init__()
        self.MainWindow = MainWindow
        self.MenuBarController = MenuBarController(self.MainWindow.menuBar)
        self.Viewer = self.MainWindow.viewer
        self.CntBar = self.MainWindow.contentBar
        self.imgEditCenter = imgEditCenter
        self.bImgExist = False
        self.bindEvent()

    def bindEvent(self):
        self.MenuBarController.I_EVT_CREATE_FINISH.connect(self.decodeImg)
        self.MenuBarController.I_EVT_SAVE_HISTOGRAM.connect(self.Viewer.saveHistogram)
        # self.Viewer.I_EVT_SCALE_CHANGE.connect(self.syncRatioToValue)
        self.Viewer.I_EVT_ENABLE_SAVE_HISTOGRAM.connect(self.MenuBarController.enableSaveHistogram)
        self.MenuBarController.I_EVT_SCALE_CHANGE.connect(self.updateView)
        self.imgEditCenter.I_EVT_SET_POINTS.connect(self.onSetPoints)
        self.imgEditCenter.I_EVT_CHANGE_VIEW_MODE.connect(self.Viewer.changeView)
        self.CntBar.I_EVT_ENABLE_SAVE_DATA.connect(self.MenuBarController.enableSaveData)

    @Slot()
    def decodeImg(self):
        self.imgEditCenter.decodeImg(self.Viewer.initImg)
        # self.MenuBarController.setScaleControllerState(bState=False)

    @Slot(int)
    def updateView(self, value):
        ratio = self.calValueToRate(value)
        self.Viewer.setScaleImg(ratio)
        if self.imgEditCenter.currViewMode == MacroDefine.VIEW_HISTOGRAM_MODE:
            self.Viewer.drawHistogram()
        else:
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
        if not self.imgEditCenter.bImgExist:
            return

        if self.imgEditCenter.currMode in MacroDefine.LST_NEED_MOUSE_TRACKING:
            self.Viewer.label_view.setMouseTracking(True)
            self.Viewer.bindMouseEvent()
        else:
            self.Viewer.label_view.setMouseTracking(False)
            self.Viewer.unbindMouseEvent()
