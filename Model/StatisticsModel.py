from PySide6.QtCore import QObject, Signal, Slot
import numpy as np
import matplotlib.pyplot as plt
import Model.MacroDefine as MacroDefine
import pandas as pd
from UI.UI_Viewer import Ui_Viewer
import math

dicColorMap = {
    'red'       : '#FF0000',
    'orange'    : '#FFA500',
    'yellow'    : '#FFFF00',
    'green'     : '#008000',
    'blue'      : '#0000FF',
    'indigo'    : '#4B0082',
    'purple'    : '#800080',
    'black'     : '#000000',
}

class StatisticsModel(QObject):
    def __init__(self):
        super().__init__()
        self.__dfContoursValue = None

    def drawHistogram(self):
        pass

    @property
    def dfContoursValue(self):
        return self.__dfContoursValue

    @dfContoursValue.setter
    def dfContoursValue(self, value):
        self.__dfContoursValue = value


    def plotSingleHistogram(self, dataInfo, ax):
        listDataInfo = dataInfo.get(MacroDefine.INPUT_PARAM_LST_DATA_INFO, [])
        infoType = dataInfo.get(MacroDefine.INPUT_PARAM_INT_INFO_TYPE, MacroDefine.DIAMETER_TYPE)
        histType = dataInfo.get(MacroDefine.INPUT_PARAM_INT_HIST_TYPE, MacroDefine.PERCENTAGE_TYPE)
        xSpacing = dataInfo.get(MacroDefine.INPUT_PARAM_INT_X_SPACING, 10)
        minX = dataInfo.get(MacroDefine.INPUT_PARAM_INT_X_MIN, -1)
        maxX = dataInfo.get(MacroDefine.INPUT_PARAM_INT_X_MAX, -1)
        bShowAvg = dataInfo.get(MacroDefine.INPUT_PARAM_BOOL_SHOW_AVG, False)
        bShowMedian = dataInfo.get(MacroDefine.INPUT_PARAM_BOOL_SHOW_MEDIAN, False)
        bShowStd = dataInfo.get(MacroDefine.INPUT_PARAM_BOOL_SHOW_STD, False)
        bShowCumLine = dataInfo.get(MacroDefine.INPUT_PARAM_BOOL_SHOW_CUMLINE, False)
        lstDataName = dataInfo.get(MacroDefine.INPUT_PARAM_LST_NAME, [])

        lstData = listDataInfo[0].lstData
        lstDataSize = len(lstData)
        groupData = {}
        groupStart = minX
        groupEnd = minX + xSpacing

        iterator = iter(lstData)
        currentValue = next(iterator, None)

        while groupStart < maxX and currentValue is not None:
            groupData[groupStart] = []

            while currentValue is not None and groupStart <= currentValue < groupEnd:
                groupData[groupStart].append(currentValue)
                currentValue = next(iterator, None)

            groupStart = groupEnd
            groupEnd = groupEnd + xSpacing

        lstCount = {key: len(value) for key, value in groupData.items()}

        counts = list(lstCount.values())

        ax.set_title(f'Histogram of {lstDataName[0]}')
        if infoType == MacroDefine.DIAMETER_TYPE:
            ax.set_xlabel('Diameter ( μm )')
        else:
            ax.set_xlabel('Surface')

        xValue = list(lstCount.keys())

        if histType == MacroDefine.PERCENTAGE_TYPE:
            perCounts = [(count/lstDataSize) * 100 for count in counts]
            ax.bar(xValue, perCounts, width=5, align='center', color=dicColorMap['blue'], edgecolor=dicColorMap['black'])
            ax.set_ylabel('Percentage')
            ax.set_xticks(xValue[::5])
            ax.set_xticklabels(xValue[::5])
            ax.set_xlim([minX, maxX])
        else:
            ax.bar(xValue, counts, width=5, align='center', color=dicColorMap['blue'], edgecolor=dicColorMap['black'])
            ax.set_ylabel('Count')
            ax.set_xticks(xValue[::5])
            ax.set_xticklabels(xValue[::5])
            ax.set_xlim([minX, maxX])
            ax.set_ylim([0, max(counts) + 1])
        ax.grid()

        if bShowAvg:
            avg = listDataInfo[0].average
            ax.axvline(avg, color=dicColorMap['green'], linestyle='--', label='Average: {:.2f}'.format(avg))

        if bShowMedian:
            median = listDataInfo[0].median
            ax.axvline(median, color=dicColorMap['orange'], linestyle='--', label='Median: {:.2f}'.format(median))

        if bShowCumLine:
            cumulativeCounts = np.cumsum(counts)
            cumulativePercentages = (cumulativeCounts / lstDataSize) * 100
            ax2 = ax.twinx()
            ax2.plot(xValue, cumulativePercentages, color='r', linestyle='-', label='Cumulative %')
            ax2.set_ylabel('Cumulative Percentage (%)', color='r')
            ax2.set_yticks([20, 40, 60, 80])
            ax2.set_ylim([0, 100])

            markerPercentages = [20, 40, 60, 80, 99]

            # Find the x-values where the cumulative percentages are close to the marker_percentages
            marker_x_values = []
            marker_y_values = []

            for percentage in markerPercentages:
                # Find the x-value closest to this percentage
                closest_index = (np.abs(cumulativePercentages - percentage)).argmin()
                marker_x_values.append(xValue[closest_index])
                marker_y_values.append(cumulativePercentages[closest_index])

            # Plot only the markers at the specific points
            ax2.plot(marker_x_values, marker_y_values, 'ro')  # Red circles for the markers
            ax2.tick_params(axis='y', labelcolor='r')

        if bShowAvg or bShowMedian:
            ax.legend(
                loc='upper left',
                fontsize=10,
                shadow=True,
                facecolor='#ccc',
                edgecolor='#000',
                title='test',
                title_fontsize=10,
                bbox_to_anchor=(-0.15, 1.15)
            )
        plt.tight_layout()

    def plotDoubleHistogram(self, dataInfo, ax):
        listDataInfo = dataInfo.get(MacroDefine.INPUT_PARAM_LST_DATA_INFO, [])
        infoType = dataInfo.get(MacroDefine.INPUT_PARAM_INT_INFO_TYPE, MacroDefine.DIAMETER_TYPE)
        histType = dataInfo.get(MacroDefine.INPUT_PARAM_INT_HIST_TYPE, MacroDefine.PERCENTAGE_TYPE)
        xSpacing = dataInfo.get(MacroDefine.INPUT_PARAM_INT_X_SPACING, 10)
        minX = dataInfo.get(MacroDefine.INPUT_PARAM_INT_X_MIN, -1)
        maxX = dataInfo.get(MacroDefine.INPUT_PARAM_INT_X_MAX, -1)
        bShowAvg = dataInfo.get(MacroDefine.INPUT_PARAM_BOOL_SHOW_AVG, False)
        bShowMedian = dataInfo.get(MacroDefine.INPUT_PARAM_BOOL_SHOW_MEDIAN, False)
        bShowStd = dataInfo.get(MacroDefine.INPUT_PARAM_BOOL_SHOW_STD, False)
        bShowCumLine = dataInfo.get(MacroDefine.INPUT_PARAM_BOOL_SHOW_CUMLINE, False)
        lstDataName = dataInfo.get(MacroDefine.INPUT_PARAM_LST_NAME, [])

        lstData1 = listDataInfo[0].lstData
        lstData2 = listDataInfo[1].lstData
        lstDataSize1 = len(lstData1)
        lstDataSize2 = len(lstData2)
        groupData1 = {}
        groupData2 = {}
        groupStart = minX
        groupEnd = minX + xSpacing

        iterator1 = iter(lstData1)
        iterator2 = iter(lstData2)
        currentValue1 = next(iterator1, None)
        currentValue2 = next(iterator2, None)
        xValue = []

        while groupStart < maxX and (currentValue1 is not None or currentValue2 is not None):
            xValue.append(groupStart)
            groupData1[groupStart] = []
            groupData2[groupStart] = []

            while currentValue1 is not None and groupStart <= currentValue1 < groupEnd:
                groupData1[groupStart].append(currentValue1)
                currentValue1 = next(iterator1, None)

            while currentValue2 is not None and groupStart <= currentValue2 < groupEnd:
                groupData2[groupStart].append(currentValue2)
                currentValue2 = next(iterator2, None)

            groupStart = groupEnd
            groupEnd = groupEnd + xSpacing

        lstCount1 = {key: len(value) for key, value in groupData1.items()}
        lstCount2 = {key: len(value) for key, value in groupData2.items()}

        counts1 = list(lstCount1.values())
        counts2 = list(lstCount2.values())
        ax.set_title(f'{lstDataName[0]} V.S. {lstDataName[1]}')
        ax.set_title(f'Histogram of {lstDataName[0]}')

        if infoType == MacroDefine.DIAMETER_TYPE:
            ax.set_xlabel('Diameter ( μm )')
        else:
            ax.set_xlabel('Surface')

        if histType == MacroDefine.PERCENTAGE_TYPE:
            perCounts1 = [(count/lstDataSize1) * 100 for count in counts1]
            perCounts2 = [(count/lstDataSize2) * 100 for count in counts2]
            ax.bar(xValue, perCounts1, width=5, align='center', color=dicColorMap['blue'], edgecolor=dicColorMap['black'], label=lstDataName[0])
            ax.bar(xValue, perCounts2, width=5, align='center', color=dicColorMap['red'], edgecolor=dicColorMap['black'], label=lstDataName[1])
            ax.set_ylabel('Percentage')
            ax.set_xticks(xValue[::5])
            ax.set_xticklabels(xValue[::5])
            ax.set_xlim([minX, maxX])
        else:
            ax.bar(xValue, counts1, width=5, align='center', color=dicColorMap['blue'], edgecolor=dicColorMap['black'], label=lstDataName[0])
            ax.bar(xValue, counts2, width=5, align='center', color=dicColorMap['red'], edgecolor=dicColorMap['black'], label=lstDataName[1])
            ax.set_ylabel('Count')
            ax.set_xticks(xValue[::5])
            ax.set_xticklabels(xValue[::5])
            ax.set_xlim([minX, maxX])
            ax.set_ylim([0, max(max(counts1), max(counts2)) + 1])

        if bShowAvg:
            avg1 = listDataInfo[0].average
            avg2 = listDataInfo[1].average
            ax.axvline(avg1, color=dicColorMap['green'], linestyle='--', label='Average: {:.2f}'.format(avg1))
            ax.axvline(avg2, color=dicColorMap['green'], linestyle='--', label='Average: {:.2f}'.format(avg2))

        if bShowMedian:
            median1 = listDataInfo[0].median
            median2 = listDataInfo[1].median
            ax.axvline(median1, color=dicColorMap['orange'], linestyle='--', label='Median: {:.2f}'.format(median1))
            ax.axvline(median2, color=dicColorMap['orange'], linestyle='--', label='Median: {:.2f}'.format(median2))

        if bShowCumLine:
            cumulativeCounts1 = np.cumsum(counts1)
            cumulativeCounts2 = np.cumsum(counts2)
            cumulativePercentages1 = (cumulativeCounts1 / lstDataSize1) * 100
            cumulativePercentages2 = (cumulativeCounts2 / lstDataSize2) * 100
            ax2 = ax.twinx()
            ax2.plot(xValue, cumulativePercentages1, color='b', linestyle='-', label='Cumulative % ' + lstDataName[0])
            ax2.plot(xValue, cumulativePercentages2, color='r', linestyle='-', label='Cumulative % ' + lstDataName[1])
            ax2.set_ylabel('Cumulative Percentage (%)', color='r')
            ax2.set_yticks([20, 40, 60, 80])
            ax2.set_ylim([0, 100])

            markerPercentages = [20, 40, 60, 80, 99]

            # Find the x-values where the cumulative percentages are close to the marker_percentages
            marker_x_values = []
            marker_y_values = []

            for percentage in markerPercentages:
                # Find the x-value closest to this percentage
                closest_index1 = (np.abs(cumulativePercentages1 - percentage)).argmin()
                closest_index2 = (np.abs(cumulativePercentages2 - percentage)).argmin()
                marker_x_values.append(xValue[closest_index1])
                marker_x_values.append(xValue[closest_index2])
                marker_y_values.append(cumulativePercentages1[closest_index1])
                marker_y_values.append(cumulativePercentages2[closest_index2])

            # Plot only the markers at the specific points
            ax2.plot(marker_x_values, marker_y_values, 'ro')

        ax.legend(
            loc='upper left',
            fontsize=10,
            shadow=True,
            facecolor='#ccc',
            edgecolor='#000',
            title='test',
            title_fontsize=10,
            bbox_to_anchor=(-0.15, 1.15)
        )
        plt.tight_layout()