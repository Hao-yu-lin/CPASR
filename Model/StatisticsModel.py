from PySide6.QtCore import QObject
import numpy as np
import matplotlib.pyplot as plt
import Model.MacroDefine as MacroDefine


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
        minX = dataInfo.get(MacroDefine.INPUT_PARAM_INT_X_MIN, -1)
        maxX = dataInfo.get(MacroDefine.INPUT_PARAM_INT_X_MAX, -1)
        bShowAvg = dataInfo.get(MacroDefine.INPUT_PARAM_BOOL_SHOW_AVG, False)
        bShowBoxPlot = dataInfo.get(MacroDefine.INPUT_PARAM_BOOL_SHOW_BOXPLOT, False)
        bShowCumLine = dataInfo.get(MacroDefine.INPUT_PARAM_BOOL_SHOW_CUMLINE, False)
        lstDataName = dataInfo.get(MacroDefine.INPUT_PARAM_LST_NAME, [])
        bShowValue = dataInfo.get(MacroDefine.INPUT_PARAM_BOOL_SHOW_VALUE, False)
        lstShowCumulative = dataInfo.get(MacroDefine.INPUT_PARAM_LST_SHOW_CUMULATIVE, [])

        lstFilterData = listDataInfo[0].getLstFilterData()
        if not lstFilterData:
            return
        lstCount = [(key, len(value)) for key, value in lstFilterData]
        lstCount = sorted(lstCount, key=lambda x: x[0])
        lstCount.insert(0, (minX, 0))
        counts = [count for key, count in lstCount]
        # lstDataSize is the total number of counts
        lstDataSize = sum(counts)

        xValue = [key for key, count in lstCount]

        ax.set_title(f'Histogram of {lstDataName[0]}')
        ax.set_xlabel('Diameter ( μm )' if infoType == MacroDefine.DIAMETER_TYPE else 'Surface')

        total_width = ax.bbox.width # 控制 bar 的總寬度佔據比例
        bar_width = total_width / (len(xValue) + 1)

        if histType == MacroDefine.PERCENTAGE_TYPE:
            perCounts = [(count/lstDataSize) * 100 for count in counts]
            bars = ax.bar(xValue, perCounts, width=bar_width, align='edge', color=dicColorMap['blue'], edgecolor=dicColorMap['blue'])
            ax.set_ylabel('Percentage')
        else:
            bars = ax.bar(xValue, counts, width=bar_width, align='edge', color=dicColorMap['blue'], edgecolor=dicColorMap['blue'])
            ax.set_ylabel('Count')
            ax.set_ylim([0, max(counts) + 1])

        max_ticks = 14
        if len(xValue) > max_ticks:
            step = len(xValue) // max_ticks
            xticks = [xValue[0]] + xValue[step:-step:step] + [xValue[-1]]
            ax.set_xticks(xticks)
            ax.set_xticklabels(xticks, rotation=45)
        else:
            ax.set_xticks(xValue)
            ax.set_xticklabels(xValue, rotation=45)

        ax.set_xlim([minX, maxX])
        # ax.grid()

        if bShowValue:
            for bar in bars:
                height = bar.get_height()
                ax.text(
                    bar.get_x() + bar.get_width() / 2,
                    height,
                    f'{height:.2f}',
                    ha='center',
                    va='bottom'
                )

        if bShowBoxPlot:
            ax_box = ax.twinx()  # 創建一個共享 x 軸的副 y 軸
            tmpLstData = []
            for _, data in lstFilterData:
                tmpLstData.extend(data)
            box = ax_box.boxplot(tmpLstData, vert=False, patch_artist=True,
                           widths=0.1, showfliers=False, manage_ticks=True,
                           boxprops=dict(facecolor="lightblue", color="blue"),
                           medianprops=dict(color="red", linestyle='--'),
                           showmeans=bShowAvg, meanline=bShowAvg,
                           )

            # 提取 boxplot 中的元素
            q1 = box['boxes'][0].get_path().vertices[0, 0]  # 第一四分位數
            q3 = box['boxes'][0].get_path().vertices[2, 0]  # 第三四分位數
            median = box['medians'][0].get_xdata()[0]  # 中位數
            whiskers = [whisker.get_xdata()[1] for whisker in box['whiskers']]  # 兩端的鬚（最小值和最大值）

            _, maxY = ax.get_ylim()
            yPosL = maxY * 0.47
            yPosH = maxY * 0.53

            ax.text(median, yPosL, f'{median:.2f}', va='center', ha='center', color='black', fontsize=10, bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.3'))
            ax.text(q1, yPosH, f'{q1:.2f}', va='center', ha='center', color='black', fontsize=10, bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.3'))
            ax.text(q3, yPosH, f'{q3:.2f}', va='center', ha='center', color='black', fontsize=10, bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.3'))
            ax.text(whiskers[0], yPosL, f'{whiskers[0]:.2f}', va='center', ha='left', color='black', fontsize=10, bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.3'))
            ax.text(whiskers[1], yPosL, f'{whiskers[1]:.2f}', va='center', ha='right', color='black', fontsize=10, bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.3'))

            if bShowAvg:
                avg = box['means'][0].get_xdata()[0]
                ax.text(avg, yPosH, f'{whiskers[1]:.2f}', va='center', ha='center', color='black', fontsize=10,
                        bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.3'))

            ax_box.set_yticks([])
            ax_box.set_ylabel('')

        if bShowAvg:
            avg = listDataInfo[0].average
            ax.axvline(avg, color=dicColorMap['green'], linestyle='--', label='Average')

        if bShowCumLine or lstShowCumulative:
            tmpLstData = []
            for _, data in lstFilterData:
                tmpLstData.extend(data)
            tmpLstData = sorted(tmpLstData)
            cumulativeCounts = np.cumsum(counts)
            cumulativePercentages = (cumulativeCounts / lstDataSize) * 100
            ax2 = ax.twinx()
            ax2.plot(xValue, cumulativePercentages, color='r', linestyle='-', label='Cumulative %')
            ax2.set_ylabel('Cumulative Percentage (%)', color='r')
            ax2.set_yticks([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
            ax2.set_ylim([0, 100])

            # Find the x-values where the cumulative percentages are close to the marker_percentages
            marker_x_values = []
            marker_y_values = []

            for percentage in lstShowCumulative:
                # Find the x-value closest to this percentage
                closest_index = (np.abs(cumulativePercentages - percentage)).argmin()
                index = int(len(tmpLstData) * (percentage / 100)) - 1
                index = min(index, len(tmpLstData) - 1)
                percentageValue = tmpLstData[index]
                marker_x_values.append(xValue[closest_index])
                marker_y_values.append(cumulativePercentages[closest_index])

                ax2.plot(xValue[closest_index], cumulativePercentages[closest_index], 'wo', markersize=8)
                ax2.text(xValue[closest_index], cumulativePercentages[closest_index],
                         f'D{percentage}:{percentageValue:.3f}', color='r', fontsize=9, ha='right', va='bottom',
                         bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.3'))

            # Plot only the markers at the specific points
            ax2.plot(marker_x_values, marker_y_values, 'ro')  # Red circles for the markers
            ax2.tick_params(axis='y', labelcolor='r')

        if bShowAvg:
            ax.legend(
                loc='upper left',
                fontsize=10,
                shadow=True,
                facecolor='#ccc',
                edgecolor='#000',
                title_fontsize=10,
                bbox_to_anchor=(-0.15, 1.15)
            )
        plt.tight_layout()

    def plotDoubleHistogram(self, dataInfo, ax):
        pass
        # listDataInfo = dataInfo.get(MacroDefine.INPUT_PARAM_LST_DATA_INFO, [])
        # infoType = dataInfo.get(MacroDefine.INPUT_PARAM_INT_INFO_TYPE, MacroDefine.DIAMETER_TYPE)
        # histType = dataInfo.get(MacroDefine.INPUT_PARAM_INT_HIST_TYPE, MacroDefine.PERCENTAGE_TYPE)
        # xSpacing = dataInfo.get(MacroDefine.INPUT_PARAM_INT_X_SPACING, 10)
        # minX = dataInfo.get(MacroDefine.INPUT_PARAM_INT_X_MIN, -1)
        # maxX = dataInfo.get(MacroDefine.INPUT_PARAM_INT_X_MAX, -1)
        # bShowAvg = dataInfo.get(MacroDefine.INPUT_PARAM_BOOL_SHOW_AVG, False)
        # bShowStd = dataInfo.get(MacroDefine.INPUT_PARAM_BOOL_SHOW_STD, False)
        # bShowCumLine = dataInfo.get(MacroDefine.INPUT_PARAM_BOOL_SHOW_CUMLINE, False)
        # lstDataName = dataInfo.get(MacroDefine.INPUT_PARAM_LST_NAME, [])
        #
        # lstData1 = listDataInfo[0].lstData
        # lstData2 = listDataInfo[1].lstData
        # lstDataSize1 = len(lstData1)
        # lstDataSize2 = len(lstData2)
        # groupData1 = {}
        # groupData2 = {}
        # groupStart = minX
        # groupEnd = minX + xSpacing
        #
        # iterator1 = iter(lstData1)
        # iterator2 = iter(lstData2)
        # currentValue1 = next(iterator1, None)
        # currentValue2 = next(iterator2, None)
        # xValue = []
        #
        # while groupStart < maxX and (currentValue1 is not None or currentValue2 is not None):
        #     xValue.append(groupStart)
        #     groupData1[groupStart] = []
        #     groupData2[groupStart] = []
        #
        #     while currentValue1 is not None and groupStart <= currentValue1 < groupEnd:
        #         groupData1[groupStart].append(currentValue1)
        #         currentValue1 = next(iterator1, None)
        #
        #     while currentValue2 is not None and groupStart <= currentValue2 < groupEnd:
        #         groupData2[groupStart].append(currentValue2)
        #         currentValue2 = next(iterator2, None)
        #
        #     groupStart = groupEnd
        #     groupEnd = groupEnd + xSpacing
        #
        # lstCount1 = {key: len(value) for key, value in groupData1.items()}
        # lstCount2 = {key: len(value) for key, value in groupData2.items()}
        #
        # counts1 = list(lstCount1.values())
        # counts2 = list(lstCount2.values())
        # ax.set_title(f'{lstDataName[0]} V.S. {lstDataName[1]}')
        # ax.set_title(f'Histogram of {lstDataName[0]}')
        #
        # if infoType == MacroDefine.DIAMETER_TYPE:
        #     ax.set_xlabel('Diameter ( μm )')
        # else:
        #     ax.set_xlabel('Surface')
        #
        # if histType == MacroDefine.PERCENTAGE_TYPE:
        #     perCounts1 = [(count/lstDataSize1) * 100 for count in counts1]
        #     perCounts2 = [(count/lstDataSize2) * 100 for count in counts2]
        #     ax.bar(xValue, perCounts1, width=5, align='center', color=dicColorMap['blue'], edgecolor=dicColorMap['black'], label=lstDataName[0])
        #     ax.bar(xValue, perCounts2, width=5, align='center', color=dicColorMap['red'], edgecolor=dicColorMap['black'], label=lstDataName[1])
        #     ax.set_ylabel('Percentage')
        #     ax.set_xticks(xValue[::5])
        #     ax.set_xticklabels(xValue[::5])
        #     ax.set_xlim([minX, maxX])
        # else:
        #     ax.bar(xValue, counts1, width=5, align='center', color=dicColorMap['blue'], edgecolor=dicColorMap['black'], label=lstDataName[0])
        #     ax.bar(xValue, counts2, width=5, align='center', color=dicColorMap['red'], edgecolor=dicColorMap['black'], label=lstDataName[1])
        #     ax.set_ylabel('Count')
        #     ax.set_xticks(xValue[::5])
        #     ax.set_xticklabels(xValue[::5])
        #     ax.set_xlim([minX, maxX])
        #     ax.set_ylim([0, max(max(counts1), max(counts2)) + 1])
        #
        # if bShowAvg:
        #     avg1 = listDataInfo[0].average
        #     avg2 = listDataInfo[1].average
        #     ax.axvline(avg1, color=dicColorMap['green'], linestyle='--', label='Average: {:.2f}'.format(avg1))
        #     ax.axvline(avg2, color=dicColorMap['green'], linestyle='--', label='Average: {:.2f}'.format(avg2))
        #
        # if bShowCumLine:
        #     cumulativeCounts1 = np.cumsum(counts1)
        #     cumulativeCounts2 = np.cumsum(counts2)
        #     cumulativePercentages1 = (cumulativeCounts1 / lstDataSize1) * 100
        #     cumulativePercentages2 = (cumulativeCounts2 / lstDataSize2) * 100
        #     ax2 = ax.twinx()
        #     ax2.plot(xValue, cumulativePercentages1, color='b', linestyle='-', label='Cumulative % ' + lstDataName[0])
        #     ax2.plot(xValue, cumulativePercentages2, color='r', linestyle='-', label='Cumulative % ' + lstDataName[1])
        #     ax2.set_ylabel('Cumulative Percentage (%)', color='r')
        #     ax2.set_yticks([20, 40, 60, 80])
        #     ax2.set_ylim([0, 100])
        #
        #     markerPercentages = [20, 40, 60, 80, 99]
        #
        #     # Find the x-values where the cumulative percentages are close to the marker_percentages
        #     marker_x_values = []
        #     marker_y_values = []
        #
        #     for percentage in markerPercentages:
        #         # Find the x-value closest to this percentage
        #         closest_index1 = (np.abs(cumulativePercentages1 - percentage)).argmin()
        #         closest_index2 = (np.abs(cumulativePercentages2 - percentage)).argmin()
        #         marker_x_values.append(xValue[closest_index1])
        #         marker_x_values.append(xValue[closest_index2])
        #         marker_y_values.append(cumulativePercentages1[closest_index1])
        #         marker_y_values.append(cumulativePercentages2[closest_index2])
        #
        #     # Plot only the markers at the specific points
        #     ax2.plot(marker_x_values, marker_y_values, 'ro')
        #
        # ax.legend(
        #     loc='upper left',
        #     fontsize=10,
        #     shadow=True,
        #     facecolor='#ccc',
        #     edgecolor='#000',
        #     title='test',
        #     title_fontsize=10,
        #     bbox_to_anchor=(-0.15, 1.15)
        # )
        # plt.tight_layout()

