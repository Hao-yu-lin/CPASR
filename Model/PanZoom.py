from PySide6.QtCore import QObject, Signal


class PanZoom(QObject):
    I_EVT_SCALE_CHANGE = Signal()

    def __init__(self):
        super().__init__()
        self.currentRatio = -1
        self.scaleFitRatio = -1
        self.showWidth = -1
        self.showHeight = -1

    def onInitFit(self):
        self.calculateScaleFit()
        self.setScaleImg(self.scaleFitRatio)
        self.I_EVT_SCALE_CHANGE.emit()

    def calculateScaleFit(self):
        widthView, heightView = self.getViewSize()
        widthImg, heightImg = self.getImgSize()
        self.scaleFitRatio = min(1.0 * widthView / widthImg, 1.0 * heightView / heightImg)

    def setScaleImg(self, ratio):
        self.currentRatio = ratio
        widthImg, heightImg = self.getImgSize()
        self.showWidth = self.currentRatio * widthImg
        self.showHeight = self.currentRatio * heightImg

    def posToImg(self, pos):
        x, y = pos
        x = x / self.currentRatio
        y = y / self.currentRatio
        return x, y

    # -----------------------------------------------------------------------
    # function need to override
    # -----------------------------------------------------------------------

    def getImgSize(self):
        return 1, 1

    def getViewSize(self):
        return 1, 1
