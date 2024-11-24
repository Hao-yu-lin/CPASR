from PySide6.QtCore import QObject
import numpy as np
import matplotlib.pyplot as plt
import Model.MacroDefine as MacroDefine

listColorMap = [
    ['#FF0000', '#E60000', '#CC0000', '#B30000', '#990000', '#800000', '#660000'],  # red
    ['#FFA500', '#E59400', '#CC8400', '#B37400', '#996400', '#805300', '#664300'],  # orange
    ['#FFFF00', '#E5E500', '#CCCC00', '#B2B200', '#999900', '#808000', '#666600'],  # yellow
    ['#008000', '#007300', '#006600', '#005900', '#004C00', '#004000', '#003300'],  # green
    ['#0000FF', '#0000E5', '#0000CC', '#0000B2', '#000099', '#000080', '#000066'],  # blue
    ['#4B0082', '#440075', '#3D0069', '#36005C', '#2F004F', '#280042', '#210036'],  # indigo
    ['#800080', '#730073', '#660066', '#590059', '#4C004C', '#400040', '#330033'],  # purple
    ['#000000', '#1A1A1A', '#333333', '#4D4D4D', '#666666', '#808080', '#999999'],  # black
]


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
        listDataInfo      = dataInfo.get(MacroDefine.INPUT_PARAM_LST_DATA_INFO, [])
        infoType          = dataInfo.get(MacroDefine.INPUT_PARAM_INT_INFO_TYPE, MacroDefine.DIAMETER_TYPE)
        histType          = dataInfo.get(MacroDefine.INPUT_PARAM_INT_HIST_TYPE, MacroDefine.PERCENTAGE_TYPE)
        minX              = dataInfo.get(MacroDefine.INPUT_PARAM_INT_X_MIN, -1)
        maxX              = dataInfo.get(MacroDefine.INPUT_PARAM_INT_X_MAX, -1)
        bShowAvg          = dataInfo.get(MacroDefine.INPUT_PARAM_BOOL_SHOW_AVG, False)
        bShowBoxPlot      = dataInfo.get(MacroDefine.INPUT_PARAM_BOOL_SHOW_BOXPLOT, False)
        bShowCumLine      = dataInfo.get(MacroDefine.INPUT_PARAM_BOOL_SHOW_CUMLINE, False)
        lstDataName       = dataInfo.get(MacroDefine.INPUT_PARAM_LST_NAME, [])
        bShowHistValue    = dataInfo.get(MacroDefine.INPUT_PARAM_BOOL_SHOW_HIST_VALUE, False)
        bShowBoxValue     = dataInfo.get(MacroDefine.INPUT_PARAM_BOOL_SHOW_BOX_VALUE, False)
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

        bar_width = 800 / (len(xValue) + 1)

        if histType == MacroDefine.PERCENTAGE_TYPE:
            perCounts = [(count/lstDataSize) * 100 for count in counts]
            bars = ax.bar(xValue, perCounts, width=bar_width, align='edge', color=listColorMap[4][0], edgecolor=listColorMap[4][4])
            ax.set_ylabel('Percentage')
        else:
            bars = ax.bar(xValue, counts, width=bar_width, align='edge', color=listColorMap[4][0], edgecolor=listColorMap[4][4])
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

        if bShowHistValue:
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
                           boxprops=dict(facecolor=listColorMap[2][3], color=listColorMap[7][3]),
                           medianprops=dict(color=listColorMap[6][0], linestyle='--'),
                           showmeans=bShowAvg, meanline=bShowAvg,
                           )

            # 提取 boxplot 中的元素
            q1 = box['boxes'][0].get_path().vertices[0, 0]  # 第一四分位數
            q3 = box['boxes'][0].get_path().vertices[2, 0]  # 第三四分位數
            median = box['medians'][0].get_xdata()[0]  # 中位數
            whiskers = [whisker.get_xdata()[1] for whisker in box['whiskers']]  # 兩端的鬚（最小值和最大值）

            if bShowBoxValue:
                _, maxY = ax.get_ylim()
                yPosL = maxY * 0.43
                yPosH = maxY * 0.57

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
            ax.axvline(avg, color=listColorMap[3][0], linestyle='--', label='Average')

        if bShowCumLine or lstShowCumulative:
            tmpLstData = []
            for _, data in lstFilterData:
                tmpLstData.extend(data)
            tmpLstData = sorted(tmpLstData)
            cumulativeCounts = np.cumsum(counts)
            cumulativePercentages = (cumulativeCounts / lstDataSize) * 100
            ax2 = ax.twinx()
            ax2.plot(xValue, cumulativePercentages, color=listColorMap[1][0], linestyle='-', label='Cumulative %')
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
                         f'D{percentage}:{percentageValue:.3f}', color=listColorMap[1][4], fontsize=9, ha='right', va='bottom',
                         bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.3'))

            # Plot only the markers at the specific points
            ax2.plot(marker_x_values, marker_y_values, 'ro')  # Red circles for the markers
            ax2.tick_params(axis='y', labelcolor=listColorMap[1][3])

        if bShowAvg:
            ax.legend(
                loc='upper left',
                fontsize=10,
                shadow=True,
                facecolor='#FFFFFF',
                edgecolor='#000',
                title_fontsize=10,
                bbox_to_anchor=(-0.15, 1.15)
            )
        plt.tight_layout()

    def plotMultiistogram(self, dataInfo, ax):
        pass
