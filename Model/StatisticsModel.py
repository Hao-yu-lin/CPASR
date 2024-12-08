from PySide6.QtCore import QObject
import numpy as np
import Model.MacroDefine as MacroDefine

LST_COLOR_MAP = [
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
        setDataKeys       = dataInfo.get(MacroDefine.INPUT_PARAM_SET_DATA_KEYS, [])

        lstFilterData = listDataInfo[0].getLstFilterData()
        if not lstFilterData:
            return

        print('[StatisticsModel] plotSingleHistogram lstDataName:', lstDataName)

        lstCount = [(key, len(value)) for key, value in lstFilterData if key in setDataKeys]
        lstCount = sorted(lstCount, key=lambda x: x[0])
        lstCount.insert(0, (minX, 0))
        counts = [count for key, count in lstCount]
        # lstDataSize is the total number of counts
        lstDataSize = sum(counts)

        xValue = sorted(list(setDataKeys))
        xValue.insert(0, minX)

        ax.set_title(f'Histogram of {lstDataName[0]}')
        ax.set_xlabel('Diameter ( μm )' if infoType == MacroDefine.DIAMETER_TYPE else 'Surface')

        bar_width = 800 / (len(xValue) + 1)

        if histType == MacroDefine.PERCENTAGE_TYPE:
            perCounts = [(count/lstDataSize) * 100 for count in counts]
            bars = ax.bar(xValue, perCounts, width=bar_width, align='edge', color=LST_COLOR_MAP[4][0], edgecolor=LST_COLOR_MAP[4][4])
            ax.set_ylabel('Percentage')
        else:
            bars = ax.bar(xValue, counts, width=bar_width, align='edge', color=LST_COLOR_MAP[4][0], edgecolor=LST_COLOR_MAP[4][4])
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
                           boxprops=dict(facecolor=LST_COLOR_MAP[2][3], color=LST_COLOR_MAP[7][3]),
                           medianprops=dict(color=LST_COLOR_MAP[6][0], linestyle='--'),
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
            ax.axvline(avg, color=LST_COLOR_MAP[3][0], linestyle='--', label='Average')

        if bShowCumLine or lstShowCumulative:
            tmpLstData = []
            for _, data in lstFilterData:
                tmpLstData.extend(data)
            tmpLstData = sorted(tmpLstData)
            cumulativeCounts = np.cumsum(counts)
            cumulativePercentages = (cumulativeCounts / lstDataSize) * 100
            ax2 = ax.twinx()
            ax2.plot(xValue, cumulativePercentages, color=LST_COLOR_MAP[1][0], linestyle='-', label='Cumulative %')
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
                         f'D{percentage}:{percentageValue:.3f}', color=LST_COLOR_MAP[1][4], fontsize=9, ha='right', va='bottom',
                         bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.3'))

            # Plot only the markers at the specific points
            ax2.plot(marker_x_values, marker_y_values, 'ro')  # Red circles for the markers
            ax2.tick_params(axis='y', labelcolor=LST_COLOR_MAP[1][3])

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

    def plotMultiHistogram(self, dataInfo, ax):
        listDataInfo = dataInfo.get(MacroDefine.INPUT_PARAM_LST_DATA_INFO, [])
        infoType = dataInfo.get(MacroDefine.INPUT_PARAM_INT_INFO_TYPE, MacroDefine.DIAMETER_TYPE)
        histType = dataInfo.get(MacroDefine.INPUT_PARAM_INT_HIST_TYPE, MacroDefine.PERCENTAGE_TYPE)
        minX = dataInfo.get(MacroDefine.INPUT_PARAM_INT_X_MIN, -1)
        maxX = dataInfo.get(MacroDefine.INPUT_PARAM_INT_X_MAX, -1)
        bShowAvg = dataInfo.get(MacroDefine.INPUT_PARAM_BOOL_SHOW_AVG, False)
        bShowBoxPlot = dataInfo.get(MacroDefine.INPUT_PARAM_BOOL_SHOW_BOXPLOT, False)
        bShowCumLine = dataInfo.get(MacroDefine.INPUT_PARAM_BOOL_SHOW_CUMLINE, False)
        lstDataName = dataInfo.get(MacroDefine.INPUT_PARAM_LST_NAME, [])
        bShowHistValue = dataInfo.get(MacroDefine.INPUT_PARAM_BOOL_SHOW_HIST_VALUE, False)
        bShowBoxValue = dataInfo.get(MacroDefine.INPUT_PARAM_BOOL_SHOW_BOX_VALUE, False)
        lstShowCumulative = dataInfo.get(MacroDefine.INPUT_PARAM_LST_SHOW_CUMULATIVE, [])
        setDataKeys = dataInfo.get(MacroDefine.INPUT_PARAM_SET_DATA_KEYS, [])

        print('[StatisticsModel] plotMultiistogram lstDataName:', lstDataName)

        multiLstCount = []
        multiLstDataSize = []
        cntLstData = len(listDataInfo)
        for i in range(cntLstData):
            lstCount = [(key, len(value)) for key, value in listDataInfo[i].getLstFilterData() if
                        key in setDataKeys]
            lstCount = sorted(lstCount, key=lambda x: x[0])
            lstCount.insert(0, (minX, 0))
            counts = [count for _, count in lstCount]
            DataSize = sum(counts)
            multiLstCount.append(counts)
            multiLstDataSize.append(DataSize)

        xValue = sorted(list(setDataKeys))  # 確保唯一性
        xValue.insert(0, minX)

        ax.set_title(f'Histogram of Multi Data')
        ax.set_xlabel('Diameter ( μm )' if infoType == MacroDefine.DIAMETER_TYPE else 'Surface')

        bar_width = ((800 / cntLstData) * 0.8 / (len(xValue) + 1))  # 每個條形圖的寬度
        bar_offset = bar_width / 2  # 條形圖之間的偏移

        for i in range(cntLstData):
            color_series = LST_COLOR_MAP[i + 3 % len(LST_COLOR_MAP)]
            if histType == MacroDefine.PERCENTAGE_TYPE:
                perCounts = [(count / multiLstDataSize[i]) * 100 for count in multiLstCount[i]]

                if cntLstData == 2:
                    bars = ax.bar(
                        [x + i * bar_width + bar_offset for x in xValue],
                        perCounts,
                        width=bar_width,
                        align='center',
                        color=color_series[0],
                        edgecolor=color_series[4],
                        label=lstDataName[i]
                    )
                else:
                    ax.plot(
                        xValue,
                        perCounts,
                        linestyle='-',
                        color=color_series[0],
                        label=lstDataName[i],
                        marker='o'
                    )
                ax.set_ylabel('Percentage')
            else:
                if cntLstData == 2:
                    bars = ax.bar(
                        [x + i * bar_width + bar_offset for x in xValue],
                        multiLstCount[i],
                        width=bar_width,
                        align='center',
                        color=color_series[0],
                        edgecolor=color_series[4],
                        label=lstDataName[i]
                    )
                else:
                    ax.plot(
                        xValue,
                        multiLstCount[i],
                        linestyle='-',
                        color=color_series[0],
                        label=lstDataName[i],
                        marker='o'
                    )
                ax.set_ylabel('Count')
                ax.set_ylim([0, max(sum(multiLstCount, [])) + 1])

            if bShowHistValue:
                if cntLstData == 2:
                    for bar in bars:
                        height = bar.get_height()
                        ax.text(
                            bar.get_x() + bar.get_width() / 2,
                            height,
                            f'{height:.2f}',
                            ha='center',
                            va='bottom'
                        )
                else:
                    for x, y in zip(xValue, multiLstCount[i]):
                        ax.text(
                            x,
                            y,
                            f'{y:.2f}',
                            ha='center',
                            va='bottom'
                        )

        max_ticks = 14
        step = max(1, len(xValue) // max_ticks)
        xticks = [xValue[0]] + xValue[step::step]
        ax.set_xticks(xticks)
        ax.set_xticklabels(xticks, rotation=45)
        ax.set_xlim([minX, maxX])

        if bShowBoxPlot:
            ax_box = ax.twinx()

            for i in range(cntLstData):
                tmpLstData = []

                # 收集要繪製的數據
                for _, data in listDataInfo[i].getLstFilterData():
                    tmpLstData.extend(data)

                # 使用 positions 將 boxplot 在 y 軸的不同位置繪製 (1, 2, 3, ...)
                y_position = i + 1  # 每一個 boxplot 繪製在 y 軸的 1, 2, 3, ...

                box = ax_box.boxplot(
                    tmpLstData,
                    vert=False,  # 水平的 boxplot
                    patch_artist=True,
                    widths=0.1,  # 宽度
                    positions=[y_position],  # 設定 y 軸位置
                    showfliers=False,
                    manage_ticks=True,
                    boxprops=dict(facecolor=LST_COLOR_MAP[2][3], color=LST_COLOR_MAP[7][3]),
                    medianprops=dict(color=LST_COLOR_MAP[6][0], linestyle='--'),
                    showmeans=bShowAvg,
                    meanline=bShowAvg
                )

                # 提取 boxplot 中的元素
                q1 = box['boxes'][0].get_path().vertices[0, 0]  # 第一四分位數
                q3 = box['boxes'][0].get_path().vertices[2, 0]  # 第三四分位數
                median = box['medians'][0].get_xdata()[0]
                whiskers = [whisker.get_xdata()[1] for whisker in box['whiskers']]

                if bShowBoxValue:
                    _, maxY = ax.get_ylim()
                    yPosL = maxY * 0.43
                    yPosH = maxY * 0.57

                    ax.text(median, y_position, f'{median:.2f}', va='center', ha='center', color='black', fontsize=10,
                            bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.3'))
                    ax.text(q1, y_position, f'{q1:.2f}', va='center', ha='center', color='black', fontsize=10,
                            bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.3'))
                    ax.text(q3, y_position, f'{q3:.2f}', va='center', ha='center', color='black', fontsize=10,
                            bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.3'))
                    ax.text(whiskers[0], y_position, f'{whiskers[0]:.2f}', va='center', ha='left', color='black',
                            fontsize=10, bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.3'))
                    ax.text(whiskers[1], y_position, f'{whiskers[1]:.2f}', va='center', ha='right', color='black',
                            fontsize=10, bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.3'))

                ax_box.set_yticks(range(1, cntLstData + 1))  # 設定 y 軸的標籤位置
                ax_box.set_yticklabels([f'Data {i + 1}' for i in range(cntLstData)])  # 設定 y 軸標籤名稱
                ax_box.set_ylabel('Data Sets')

        if bShowAvg:
            for i in range(cntLstData):
                avg = listDataInfo[i].average
                ax.axvline(avg, color=LST_COLOR_MAP[i + 3 % len(LST_COLOR_MAP)][0], linestyle='--',
                           label=f'Average of {lstDataName[i]}')

        if bShowCumLine or lstShowCumulative:
            for i in range(cntLstData):
                tmpLstData = []
                for _, data in listDataInfo[i].getLstFilterData():
                    tmpLstData.extend(data)
                tmpLstData = sorted(tmpLstData)

                cumulativeCounts = np.cumsum(multiLstCount[i])
                cumulativePercentages = (cumulativeCounts / multiLstDataSize[i]) * 100

                ax2 = ax.twinx()
                color_series = LST_COLOR_MAP[i + 3 % len(LST_COLOR_MAP)]

                ax2.plot(xValue, cumulativePercentages, color=color_series[0], linestyle='-',
                         label=f'Cumulative % ({lstDataName[i]})')
                ax2.set_ylabel('Cumulative Percentage (%)', color='r')
                ax2.set_yticks([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
                ax2.set_ylim([0, 100])

                marker_x_values = []
                marker_y_values = []

                for percentage in lstShowCumulative:
                    closest_index = (np.abs(cumulativePercentages - percentage)).argmin()
                    index = int(len(tmpLstData) * (percentage / 100)) - 1
                    index = min(index, len(tmpLstData) - 1)
                    percentageValue = tmpLstData[index]
                    marker_x_values.append(xValue[closest_index])
                    marker_y_values.append(cumulativePercentages[closest_index])

                    ax2.plot(xValue[closest_index], cumulativePercentages[closest_index], 'wo', markersize=8)
                    ax2.text(xValue[closest_index], cumulativePercentages[closest_index],
                             f'D{percentage}:{percentageValue:.3f}', color=color_series[4], fontsize=9, ha='right',
                             va='bottom',
                             bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.3'))

                ax2.plot(marker_x_values, marker_y_values, 'ro')
                ax2.tick_params(axis='y', labelcolor=color_series[3])

        ax.legend(
            loc='upper left',
            fontsize=10,
            shadow=True,
            facecolor='#FFFFFF',
            edgecolor='#000',
            title_fontsize=10,
            bbox_to_anchor=(-0.15, 1.15)
        )