import os
import copy
from PySide6.QtCore import QObject

class ImgManager(QObject):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        super().__init__()
        self.__currentData = None

    def createImgData(self, path):
        imgDataBase = ImgDataBase(path)
        self.__currentData = imgDataBase

    def getCurrentData(self):
        return self.__currentData


imgManager = ImgManager()

class ImgDataBase:
    def __init__(self, filePath):
        self.__filePath = filePath
        self.nameImg = os.path.splitext(os.path.basename(filePath))[0]
        self.__widthImg = -1
        self.__heightImg = -1
        self.__channelImg = -1
        self.__bytePerLine = -1
        self.__srcImg = None


    @property
    def filePath(self):
        return self.__filePath

    @property
    def widthImg(self):
        return self.__widthImg

    @widthImg.setter
    def widthImg(self, width):
        self.__widthImg = width
        self.__bytePerLine = 3 * width

    @property
    def heightImg(self):
        return self.__heightImg

    @heightImg.setter
    def heightImg(self, height):
        self.__heightImg = height

    @property
    def channelImg(self):
        return self.__channelImg

    @channelImg.setter
    def channelImg(self, channel):
        self.__channelImg = channel

    @property
    def srcImg(self):
        srcImg = copy.deepcopy(self.__srcImg)
        return srcImg

    @srcImg.setter
    def srcImg(self, src):
        self.__srcImg = src


