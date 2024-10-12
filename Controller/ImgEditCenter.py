from Model.ImgDataModel import imgManager
from Model.ImgEngine import ImgEngine
from PySide6.QtCore import Signal, QObject
from Model.AnalysisDataModel import analysisDataModel
import Model.MacroDefine as MacroDefine

class ImgEditCenter(QObject):
    _instance = None
    I_EVT_UPDATE_IMG = Signal()
    I_EVT_SET_POINTS = Signal()
    I_EVT_CHANGE_VIEW_MODE = Signal()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        super().__init__()
        self.imgEngine = ImgEngine()
        self.imgSrc = None
        self.prevImg = None

        self.widthImg = -1
        self.heightImg = -1
        self.channelImg = -1
        self.bytePerLine = -1
        self.imgPath = ''
        self.bImgExist = False
        self.bReverseMask = False
        self.__lstRefPoint = []
        self.__lstTmpPoint = []
        self.__currMode = MacroDefine.NONE_MODE
        self.__prevMode = MacroDefine.NONE_MODE
        self.__currViewMode = MacroDefine.VIEW_ORIGIN_MODE

    def decodeImg(self, cbFunction=None):
        imgData = imgManager.getCurrentData()
        if imgData is None:
            return
        self.imgPath = imgData.filePath
        self.imgSrc = self.imgEngine.decodeImg(self.imgPath)
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
        imgData = imgManager.getCurrentData()
        self.imgSrc = imgData.srcImg

    def setRefPoints(self):
        if len(self.__lstTmpPoint) == 2:
            analysisDataModel.setLstRefPoint(self.getTmpPoint())

    def setROIPoints(self):
        if len(self.__lstTmpPoint) > 2:
            if self.__lstTmpPoint[-1] != self.__lstTmpPoint[0]:
                self.__lstTmpPoint.append(self.__lstTmpPoint[0])

            analysisDataModel.setLstROIPoint(self.getTmpPoint())

    def drawLstPoint(self, lstDrawPoint, bDrawPoint=True, bDrawLine=True):
        imgData = imgManager.getCurrentData()
        self.imgSrc = self.imgEngine.updatePtsOnView(imgData.srcImg, lstDrawPoint, bDrawPoint, bDrawLine,
                                                     color=(255, 0, 0))
        self.I_EVT_UPDATE_IMG.emit()

    def setTmpPoint(self, points):
        if self.currMode == MacroDefine.REF_MODE:
            if len(self.__lstTmpPoint) < 2:
                self.__lstTmpPoint.append(points)
            else:
                self.__lstTmpPoint[1] = points

        elif self.currMode == MacroDefine.ROI_MODE:
            if points == (-1, -1):
                if len(self.__lstTmpPoint) > 2:
                    points = self.__lstTmpPoint[0]
                else:
                    return
            self.__lstTmpPoint.append(points)

    def popTmpPoint(self):
        self.__lstTmpPoint.pop()

    def drawTmpPoint(self, bDrawPoint=True, bDrawLine=True):
        imgData = imgManager.getCurrentData()
        self.imgSrc = self.imgEngine.updatePtsOnView(imgData.srcImg, self.__lstTmpPoint, bDrawPoint, bDrawLine,
                                                     color=(0, 255, 0))
        self.I_EVT_UPDATE_IMG.emit()

    def clearTmpPoint(self):
        self.__lstTmpPoint = []

    def getTmpPoint(self):
        return self.__lstTmpPoint

    def clearRefPoint(self):
        analysisDataModel.clearLstRefPoint()

    def clearROIPoint(self):
        analysisDataModel.clearLstROIPoint()
        self.setSrcImg()

    def clearContours(self):
        analysisDataModel.clearLstContours()
        self.setContoursImg()

    @property
    def currMode(self):
        return self.__currMode

    @currMode.setter
    def currMode(self, mode):
        self.__currMode = mode
        self.I_EVT_SET_POINTS.emit()

    @property
    def prevMode(self):
        return self.__prevMode

    @prevMode.setter
    def prevMode(self, mode):
        self.__prevMode = mode

    @property
    def currViewMode(self):
        return self.__currViewMode

    @currViewMode.setter
    def currViewMode(self, mode):
        self.__currViewMode = mode
        if mode != MacroDefine.VIEW_HISTOGRAM_MODE:
            self.drawImg()
        else:
            self.currMode = MacroDefine.NONE_MODE

        self.I_EVT_CHANGE_VIEW_MODE.emit()

    def drawImg(self):
        if not self.bImgExist:
            return

        if self.currViewMode == MacroDefine.VIEW_MASK_MODE:
            self.setMaskImg()
        elif self.currViewMode == MacroDefine.VIEW_CONTOURS_MODE:
            self.setContoursImg()
        else:
            self.setSrcImg()

        self.I_EVT_UPDATE_IMG.emit()

    def setSrcImg(self):
        if not self.bImgExist:
            return

        if self.prevImg is not None and self.prevMode != MacroDefine.NONE_MODE:
            self.imgSrc = self.prevImg
            self.prevImg = None
        else:
            imgData = imgManager.getCurrentData()
            self.imgSrc = self.imgEngine.updatePtsOnView(imgData.srcImg, None, bDrawPoint=True, bDrawLine=True)

    def setMaskImg(self):
        if not self.bImgExist:
            return
        self.prevImg = self.imgSrc
        lstROIPoint = analysisDataModel.getLstROIPoint()
        imgData = imgManager.getCurrentData()
        if lstROIPoint:
            prevImg = self.imgEngine.updatePtsOnView(imgData.srcImg, lstROIPoint, True, True,
                                                     color=(255, 0, 0))
            maskImg = analysisDataModel.getMaskImg(bReverse=self.bReverseMask)
            self.imgSrc = self.imgEngine.blendImg(prevImg, 1,  maskImg, 0.3, color=(255, 0, 0))
        else:
            maskImg = analysisDataModel.getMaskImg(bReverse=self.bReverseMask)
            self.imgSrc = self.imgEngine.blendImg(imgData.srcImg, 1, maskImg, 0.3, color=(255, 0, 0))

    def setContoursImg(self):
        if not self.bImgExist:
            return

        self.prevImg = self.imgSrc
        imgData = imgManager.getCurrentData()
        lstContours = analysisDataModel.getLstContours()
        if lstContours:
            self.imgSrc = self.imgEngine.updateContoursOnView(imgData.srcImg, lstContours)


imgEditCenter = ImgEditCenter()
