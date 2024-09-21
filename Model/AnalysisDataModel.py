from PySide6.QtCore import QObject
from Model.ImgDataModel import imgManager
from Model.ImgEngine import ImgEngine



class AnalysisDataModel(QObject):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        super().__init__()
        self.__lstRefPoint = []
        self.__lstROIPoint = []
        self.__scaleRefObj = -1
        self.maskImg = None
        self.imgEngine = ImgEngine()

    def restAnalysisData(self):
        self.__lstRefPoint = []
        self.__lstROIPoint = []
        self.__scaleRefObj = -1

    # for LstRefPoint
    def setLstRefPoint(self, lstRefPoint):
        lstTmp = list(lstRefPoint)
        self.__lstRefPoint = lstTmp
        print('[AnalysisDataModel][setLstRefPoint]')

    def getLstRefPoint(self):
        return self.__lstRefPoint

    def clearLstRefPoint(self):
        self.__lstRefPoint.clear()
        print('[AnalysisDataModel][clearLstRefPoint]')

    # for scalRefObj
    def setScaleRefObj(self, scaleRefObj):
        self.__scaleRefObj = scaleRefObj
        print('[AnalysisDataModel][setScaleRefObj] __scaleRefObj:', self.__scaleRefObj)

    def getScaleRefObj(self):
        return self.__scaleRefObj

    def clearScaleRefObj(self):
        self.__scaleRefObj = -1
        print('[AnalysisDataModel][clearScaleRefObj] __scaleRefObj cleared')

    # for lstROIPoint
    def setLstROIPoint(self, lstROIPoint):
        lstTmp = list(lstROIPoint)
        self.__lstROIPoint = lstTmp
        print('[AnalysisDataModel][setLstROIPoint]')

    def getLstROIPoint(self):
        return self.__lstROIPoint

    def clearLstROIPoint(self):
        self.__lstROIPoint.clear()
        print('[AnalysisDataModel][clearLstROIPoint]')

    def getMaskImg(self):
        self.produceMaskImg()
        return self.maskImg

    def produceMaskImg(self):
        currData = imgManager.getCurrentData()
        if currData is None:
            return None
        width, height = currData.widthImg, currData.heightImg

        self.maskImg = self.imgEngine.produceMaskImg(width, height, self.getLstROIPoint(), color=(255, 255, 255))


analysisDataModel = AnalysisDataModel()