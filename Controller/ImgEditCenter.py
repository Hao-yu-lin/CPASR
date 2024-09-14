from Model.ImgDataModel import dictImg
from Model.ImgEngine import ImgEngine
from PySide6.QtCore import Signal, Slot, QObject
from Model.AnalysisDataModel import analysisDataModel
from Model.MacroDefine import NONE_MODE, REF_MODE, ROI_MODE


class ImgEditCenter(QObject):
    _instance = None
    I_EVT_UPDATE_IMG = Signal()
    I_EVT_SET_POINTS = Signal()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        super().__init__()
        self.ImgEngine = ImgEngine()
        self.imgSrc = None
        self.widthImg = -1
        self.heightImg = -1
        self.channelImg = -1
        self.bytePerLine = -1
        self.imgPath = ''
        self.bImgExist = False
        self.__lstRefPoint = []
        self.__lstTmpPoint = []
        self.__currMode = NONE_MODE

    def decodeImg(self, cbFunction=None):
        imgData = dictImg.getCurrentData()
        if imgData is None:
            return
        self.imgPath = imgData.filePath
        self.imgSrc = self.ImgEngine.decodeImg(self.imgPath)
        if self.imgSrc is not None:
            self.heightImg, self.widthImg, self.channelImg = self.imgSrc.shape
            imgData.widthImg = self.widthImg
            imgData.heightImg = self.heightImg
            imgData.channelImg = self.channelImg
            imgData.srcImg = self.imgSrc
            self.bytePerLine = 3 * self.widthImg

            if cbFunction:
                cbFunction()
            self.bImgExist = True

    def getImgShape(self):
        return self.widthImg, self.heightImg, self.bytePerLine

    def getImgData(self):
        return self.imgSrc.data

    def restSrcImg(self):
        imgData = dictImg.getCurrentData()
        self.imgSrc = imgData.srcImg

    def setRefPoints(self):
        if len(self.__lstTmpPoint) == 2:
            analysisDataModel.setLstRefPoint(self.__lstTmpPoint)

    def setROIPoints(self):
        if len(self.__lstTmpPoint) > 2:
            if self.__lstTmpPoint[-1] != self.__lstTmpPoint[0]:
                self.__lstTmpPoint.append(self.__lstTmpPoint[0])
            analysisDataModel.setLstROIPoint(self.__lstTmpPoint)

    def drawLstPoint(self, bDrawPoint=True, bDrawLine=True):
        imgData = dictImg.getCurrentData()
        if self.currMode == REF_MODE:
            lstDrawPoint = analysisDataModel.getLstRefPoint()
        elif self.currMode == ROI_MODE:
            lstDrawPoint = analysisDataModel.getLstROIPoint()
        else:
            return
        self.imgSrc = self.ImgEngine.updatePtsOnView(imgData.srcImg, lstDrawPoint, bDrawPoint, bDrawLine,
                                                     color=(255, 0, 0))
        self.I_EVT_UPDATE_IMG.emit()

    def drawSrcPoint(self):
        imgData = dictImg.getCurrentData()
        self.imgSrc = self.ImgEngine.updatePtsOnView(imgData.srcImg, None, bDrawPoint=True, bDrawLine=True)
        self.I_EVT_UPDATE_IMG.emit()

    def setTmpPoint(self, points):
        if self.currMode == REF_MODE:
            if len(self.__lstTmpPoint) < 2:
                self.__lstTmpPoint.append(points)
            else:
                self.__lstTmpPoint[1] = points

        elif self.currMode == ROI_MODE:
            if points == (-1, -1):
                if len(self.__lstTmpPoint) > 2:
                    points = self.__lstTmpPoint[0]
                else:
                    return
            self.__lstTmpPoint.append(points)

    def popTmpPoint(self):
        self.__lstTmpPoint.pop()

    def drawTmpPoint(self, bDrawPoint=True, bDrawLine=True):
        imgData = dictImg.getCurrentData()
        self.imgSrc = self.ImgEngine.updatePtsOnView(imgData.srcImg, self.__lstTmpPoint, bDrawPoint, bDrawLine,
                                                     color=(0, 255, 0))
        self.I_EVT_UPDATE_IMG.emit()

    def clearTmpPoint(self):
        self.__lstTmpPoint = []

    def clearRefPoint(self):
        analysisDataModel.clearLstRefPoint()
        self.drawSrcPoint()

    def clearROIPoint(self):
        analysisDataModel.clearLstROIPoint()
        self.drawSrcPoint()

    @property
    def currMode(self):
        return self.__currMode

    @currMode.setter
    def currMode(self, mode):
        self.__currMode = mode
        self.I_EVT_SET_POINTS.emit()


imgEditCenter = ImgEditCenter()
