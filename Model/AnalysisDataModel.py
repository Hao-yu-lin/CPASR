from PySide6.QtCore import QObject
from PySide6.QtCore import Signal
from Model.ImgDataModel import imgManager
from Model.ImgEngine import ImgEngine
import Model.MacroDefine as MacroDefine
import pandas as pd

class AnalysisDataModel(QObject):
    _instance = None
    I_EVT_ANALYSIS_FINISH = Signal()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        super().__init__()
        self.__lstRefPoint = []
        self.__lstROIPoint = []
        self.__lstContours = []
        self.__scaleRefObj = -1
        self.__threshold = -1
        self.maskImg = None
        self.dfContoursValue = None
        self.numContours = 0
        self.imgEngine = ImgEngine()
        self.bIsShowDoubleItem = False
        self.strDataName = ''

    def resetAnalysisData(self):
        self.__lstRefPoint = []
        self.__lstROIPoint = []
        self.__lstContours = []
        self.__scaleRefObj = -1
        self.__threshold = -1
        self.maskImg = None

    def bCanAnalysis(self):
        if self.__lstContours and self.__scaleRefObj > 0:
            return True
        else:
            return False

    @property
    def threshold(self):
        return self.__threshold

    @threshold.setter
    def threshold(self, value):
        if value < 0:
            self.__threshold = -1
        else:
            self.__threshold = value

    def getLstContours(self):
        return self.__lstContours

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
        if scaleRefObj < 0:
            self.__scaleRefObj = -1
        else:
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

    def getMaskImg(self, bReverse=False):
        self.produceMaskImg(bReverse=bReverse)
        return self.maskImg

    def produceMaskImg(self, bReverse=False):
        imgData = imgManager.getCurrentData()
        if imgData is None:
            return None
        width, height = imgData.widthImg, imgData.heightImg

        self.maskImg = self.imgEngine.produceMaskImg(width, height, self.getLstROIPoint(), color=(255, 255, 255), bReverse=bReverse)

    def findContours(self, threadhold=-1, bReverse=False):
        maskImg = self.getMaskImg(bReverse=bReverse)
        imgData = imgManager.getCurrentData()
        if imgData is None:
            return False

        self.strDataName = imgData.nameImg
        roiImg = imgData.srcImg
        roiImg[maskImg == 0] = 255
        self.__lstContours, self.threshold = self.imgEngine.contourDetect(roiImg, threadhold)
        if self.__lstContours:
            self.numContours = len(self.__lstContours)
            print('[AnalysisDataModel][findContours] Contours successfully detected')
            return True
        else:
            print('[AnalysisDataModel][findContours] Contours not detected')
            return False

    def analysisContours(self):
        lstContours = self.getLstContours()
        if not lstContours:
            return
        contour_list = []
        for i in range(len(lstContours)):
            area, diameter = self.imgEngine.calContorusArea(lstContours[i], self.__scaleRefObj)
            contour_list.append({
                MacroDefine.INT_INDEX           : i,
                MacroDefine.INT_AREA            : area,
                MacroDefine.INT_DIAMETER        : diameter,
            })
        dfContours = pd.DataFrame(contour_list)
        self.dfContoursValue = dfContours
        self.I_EVT_ANALYSIS_FINISH.emit()
        pass

    def delContoursPoint(self, pos):
        if not self.__lstContours:
            return

        self.__lstContours = self.imgEngine.deleteCountour(self.__lstContours, pos)

    def clearLstContours(self):
        self.__lstContours = []
        self.numContours = 0

    def saveContoursValue(self, filePath):
        self.dfContoursValue.to_csv(filePath, index=False)


analysisDataModel = AnalysisDataModel()