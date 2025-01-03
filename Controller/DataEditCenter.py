import os
import pandas as pd
import numpy as np
from PySide6.QtCore import Signal, Slot, QObject
from Model.AnalysisDataModel import analysisDataModel
import Model.MacroDefine as MacroDefine


def roundDownToNearest(number):
    return int(np.floor(number / 10.0)) * 10


def roundUpToNearest(number):
    return int(np.ceil(number / 10.0)) * 10

def checkDataValid(df):
    required_columns = {'index', 'area', 'diameter'}
    return required_columns.issubset(df.columns)


class dataAnalysisBasic:
    def __init__(self):
        self._lstData = []
        self.lstFilterData = []
        self.average = -1
        self.min = -1
        self.max = -1
        self.std = -1
        self.total = -1
        self.median = -1

    def restData(self):
        self._lstData = []
        self.lstFilterData = []
        self.average = -1
        self.min = -1
        self.max = -1
        self.std = -1
        self.total = -1
        self.median = -1

    def setData(self, lstData):
        self._lstData.extend(lstData)
        self._lstData.sort()
        self.analysisLstData()

    @property
    def lstData(self):
        return self._lstData

    def analysisLstData(self):
        if self._lstData is None:
            return
        self.min = min(self._lstData)
        self.max = max(self._lstData)
        self.average = np.mean(self._lstData)
        self.std = np.std(self._lstData)
        self.total = len(self._lstData)
        self.median = np.median(self._lstData)


    def setLstFilterData(self, lstFilterData):
        if lstFilterData:
            self.lstFilterData = lstFilterData
            tmpLstData = []
            for _, data in lstFilterData:
                tmpLstData.extend(data)

            if tmpLstData:
                self.min = min(tmpLstData)
                self.max = max(tmpLstData)
                self.average = np.mean(tmpLstData)
                self.std = np.std(tmpLstData)
                self.total = len(tmpLstData)
                self.median = np.median(tmpLstData)
                pass

    def getLstFilterData(self):
        return self.lstFilterData

class DataItem:
    def __init__(self):
        self.__strName = ''
        self.diameterData = dataAnalysisBasic()
        self.areaData = dataAnalysisBasic()
        self._bHasData = False

    def restDataItem(self):
        self.__strName = ''
        self.diameterData.restData()
        self.areaData.restData()
        self._bHasData = False

    def setDfContoursValue(self, dfData):
        if dfData is None:
            return

        lstDiameter = self.getListDataWithKey(MacroDefine.INT_DIAMETER, dfData)
        if lstDiameter:
            self.diameterData.setData(lstDiameter)

        lstArea = self.getListDataWithKey(MacroDefine.INT_AREA, dfData)
        if lstArea:
            self.areaData.setData(lstArea)

        if lstDiameter or lstArea:
            self._bHasData = True
        pass

    def getDataInfo(self, dataType):
        if dataType == MacroDefine.DIAMETER_TYPE:
            return self.diameterData
        elif dataType == MacroDefine.AREA_TYPE:
            return self.areaData
        else:
            return None

    def getListDataWithKey(self, key, dfData):
        # Remove outliers
        try:
            Q1 = dfData[key].quantile(0.25)
            Q3 = dfData[key].quantile(0.75)
            IQR = Q3 - Q1
            lowerBound = max(Q1 - 1.5 * IQR, 0)
            upperBound = Q3 + 1.5 * IQR
            minX = roundDownToNearest(lowerBound)
            maxX = roundUpToNearest(upperBound)
            filterData = dfData[(dfData[key] > minX) & (dfData[key] < maxX)].copy()
            lstData = filterData.sort_values(by=key)[key].tolist()
        except:
            lstData = None
        return lstData

    @property
    def strName(self):
        return self.__strName

    @strName.setter
    def strName(self, name):
        self.__strName = name

    @property
    def bHasData(self):
        return self._bHasData


class DataEditCenter(QObject):
    _instance = None
    I_EVT_UPDATE_HISTOGRAM = Signal()
    I_EVT_UPDATE_DATA_INFO = Signal(int)

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        super().__init__()
        self.lstDataItem = [DataItem(), DataItem(), DataItem(), DataItem(), DataItem()]
        self.showType = False
        self.__dicDataParam = None
        self.minXValue = -1
        self.maxXValue = -1
        self.bindEvent()

    def bindEvent(self):
        analysisDataModel.I_EVT_ANALYSIS_FINISH.connect(self.loadAnalysisData)

    def setDfData(self, idx, df):
        self.lstDataItem[idx].setDfContoursValue(df)

    def setStrName(self, idx, name):
        self.lstDataItem[idx].strName = name

    def getSingleDataItem(self, idx):
        return self.lstDataItem[idx]

    def bHasData(self, idx):
        return self.lstDataItem[idx].bHasData

    def loadData(self, idx, strFilePath):
        # read csv data
        try:
            df = pd.read_csv(strFilePath)
            validData = checkDataValid(df)
            if validData:
                self.setDfData(idx, df)
                strDataName, _ = os.path.splitext(os.path.basename(strFilePath))
                self.setStrName(idx, strDataName)
                self.I_EVT_UPDATE_DATA_INFO.emit(idx)
        except Exception as e:
            # 若讀取檔案失敗或發生其他錯誤，返回 False
            print(f"Error reading file: {e}")

    def clearData(self, idx):
        self.lstDataItem[idx].restDataItem()

    def updateHistogram(self, showHistTypeData, inputParam):
        self.showType = showHistTypeData
        infoType = inputParam.get(MacroDefine.INPUT_PARAM_INT_INFO_TYPE, MacroDefine.DIAMETER_TYPE)
        histType = inputParam.get(MacroDefine.INPUT_PARAM_INT_HIST_TYPE, MacroDefine.PERCENTAGE_TYPE)


        lstDataName = []
        lstDataInfo = []
        currDataIdx = inputParam.get(MacroDefine.INPUT_PARAM_INT_DATA_INDEX, 0)
        if showHistTypeData == MacroDefine.SHOW_HIST_TYPE_NONE:
            return
        elif showHistTypeData == MacroDefine.SHOW_HIST_TYPE_DATA1:
            lstDataInfo.append(self.lstDataItem[currDataIdx].getDataInfo(infoType))
            lstDataName.append(self.lstDataItem[currDataIdx].strName)
        elif showHistTypeData == MacroDefine.SHOW_HIST_TYPE_BOTH:
            lstCheckShowData = inputParam.get(MacroDefine.INPUT_PARAM_LST_SHOW_DATA, [])

            for idx, value in enumerate(lstCheckShowData):
                if value:
                    lstDataInfo.append(self.lstDataItem[idx].getDataInfo(infoType))
                    lstDataName.append(self.lstDataItem[idx].strName)

        minXValue = inputParam.get(MacroDefine.INPUT_PARAM_INT_X_MIN, -1)
        maxXValue = inputParam.get(MacroDefine.INPUT_PARAM_INT_X_MAX, -1)

        xSpacing = inputParam.get(MacroDefine.INPUT_PARAM_INT_X_SPACING, -1)

        if minXValue == -1:
            minXValue = min([data.min for data in lstDataInfo])
        self.minXValue = minXValue

        if maxXValue == -1:
            maxXValue = max([data.max for data in lstDataInfo])
        self.maxXValue = maxXValue

        if xSpacing == -1:
            if infoType == MacroDefine.DIAMETER_TYPE:
                xSpacing = 10
            elif infoType == MacroDefine.AREA_TYPE:
                xSpacing = 0.01

        setDataKeys = set()

        if showHistTypeData == MacroDefine.SHOW_HIST_TYPE_DATA1:
            lstData = lstDataInfo[0].lstData
            lstFilterData, sorted_keys = self.getlstFilterData(lstData, self.minXValue, self.maxXValue, xSpacing)
            lstDataInfo[0].setLstFilterData(lstFilterData)
            setDataKeys.update(sorted_keys)
        elif showHistTypeData == MacroDefine.SHOW_HIST_TYPE_BOTH:
            for data in lstDataInfo:
                lstData = data.lstData
                lstFilterData, sorted_keys = self.getlstFilterData(lstData, self.minXValue, self.maxXValue, xSpacing)
                data.setLstFilterData(lstFilterData)
                setDataKeys.update(sorted_keys)

        self.__dicDataParam = {
            MacroDefine.INPUT_PARAM_INT_X_MIN               : self.minXValue,
            MacroDefine.INPUT_PARAM_INT_X_MAX               : self.maxXValue,
            MacroDefine.INPUT_PARAM_LST_NAME                : lstDataName,
            MacroDefine.INPUT_PARAM_BOOL_SHOW_AVG           : inputParam.get(MacroDefine.INPUT_PARAM_BOOL_SHOW_AVG, False),
            MacroDefine.INPUT_PARAM_BOOL_SHOW_BOXPLOT       : inputParam.get(MacroDefine.INPUT_PARAM_BOOL_SHOW_BOXPLOT, False),
            MacroDefine.INPUT_PARAM_BOOL_SHOW_CUMLINE       : inputParam.get(MacroDefine.INPUT_PARAM_BOOL_SHOW_CUMLINE, False),
            MacroDefine.INPUT_PARAM_LST_DATA_INFO           : lstDataInfo,
            MacroDefine.INPUT_PARAM_INT_INFO_TYPE           : infoType,
            MacroDefine.INPUT_PARAM_INT_HIST_TYPE           : histType,
            MacroDefine.INPUT_PARAM_BOOL_SHOW_HIST_VALUE    : inputParam.get(MacroDefine.INPUT_PARAM_BOOL_SHOW_HIST_VALUE, False),
            MacroDefine.INPUT_PARAM_BOOL_SHOW_BOX_VALUE     : inputParam.get(MacroDefine.INPUT_PARAM_BOOL_SHOW_BOX_VALUE, False),
            MacroDefine.INPUT_PARAM_LST_SHOW_CUMULATIVE     : inputParam.get(MacroDefine.INPUT_PARAM_LST_SHOW_CUMULATIVE, []),
            MacroDefine.INPUT_PARAM_SET_DATA_KEYS           : setDataKeys
        }

        self.I_EVT_UPDATE_HISTOGRAM.emit()

    def getHistogramInfo(self):
        return self.__dicDataParam

    def loadAnalysisData(self):
        strDataName = analysisDataModel.strDataName
        dfData = analysisDataModel.dfContoursValue
        self.setDfData(0, dfData)
        self.setStrName(0, strDataName)
        self.I_EVT_UPDATE_DATA_INFO.emit(0)

    def getlstFilterData(self, lstData, minX, maxX, xSpacing):
        groupData = {}
        groupStart = minX + xSpacing

        # [value < minX, value < minX + xSpacing,  value < minX + 2*xSpacing, ... ,  < minX + n*xSpacing, < maxX, > maxX]
        while groupStart < maxX:
            groupData[groupStart] = []
            groupStart += xSpacing

        sorted_keys = sorted(groupData.keys())

        if not lstData:
            return [], sorted_keys


        for value in lstData:
            if value > maxX:
                continue

            if value < minX:
                continue

            if value <= 0.0:
                continue

            for key in sorted_keys:
                if value < key:
                    groupData[key].append(value)
                    break

        lstFilterData = [(key, value) for key, value in groupData.items()]

        return lstFilterData, sorted_keys




dataEditCenter = DataEditCenter()
