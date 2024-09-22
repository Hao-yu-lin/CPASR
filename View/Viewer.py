from PySide6.QtCore import Qt, Slot, QEvent, QRect, QSize
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QWidget, QStackedWidget

from Controller.ImgEditCenter import imgEditCenter
from Model.PanZoom import PanZoom
from Model.MacroDefine import VIEW_HISTOGRAM_MODE
from Model.AnalysisDataModel import analysisDataModel
from UI.UI_Viewer import Ui_Viewer
from Model.MacroDefine import REF_MODE, ROI_MODE, MOUSE_STATE_NONE, MOUSE_STATE_DRAW_POINTS

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import pandas as pd


# self.scrollAreaWidgetContents = QWidget()
# self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
# self.scrollAreaWidgetContents.setGeometry(QRect(-2, 0, 1036, 597))
# self.scrollAreaWidgetContents.setMinimumSize(QSize(1036, 597))
# self.scrollAreaWidgetContents.setAutoFillBackground(False)
# self.label_view = QLabel()
# self.scrollArea.setWidget(self.label_view)


class Viewer(QWidget, Ui_Viewer, PanZoom):
    def __init__(self, widget):
        super().__init__()
        self.widget = widget
        self.setupUi(widget)
        self.initComplete(widget)
        self.editCenter = imgEditCenter
        self.widthImg = -1
        self.heightImg = -1
        self.qpImg = None
        self.mouseState = MOUSE_STATE_NONE
        self.bindEvent()


    def initComplete(self, widget):
        self.stackedWidget = QStackedWidget(widget)
        self.stackedWidget.setMinimumSize(QSize(1036, 597))
        # Matplotlib FigureCanvas for histogram or chart
        self.cvHistogram = FigureCanvas(plt.Figure())
        self.cvHistogram.setGeometry(QRect(12, 12, 1036, 597))
        self.cvHistogram.setMinimumSize(QSize(1036, 597))

        # Add both widgets (image and chart) to the stacked widget
        self.stackedWidget.addWidget(self.label_view)  # Index 0
        self.stackedWidget.addWidget(self.cvHistogram)  # Index 1

        # Add both widgets to the layout but show one at a time
        self.scrollArea.setWidget(self.stackedWidget)  # Initially set the image view

    def bindEvent(self):
        self.editCenter.I_EVT_UPDATE_IMG.connect(self.updateQImg)

    def bindMouseEvent(self):
        self.label_view.mousePressEvent = self.onMouseDown
        self.label_view.mouseMoveEvent = self.onMouseMove

    def unbindMouseEvent(self):
        self.label_view.mousePressEvent = self.doNotingEvent
        self.label_view.mouseMoveEvent = self.doNotingEvent

    def initImg(self):
        self.widthImg, self.heightImg, bytesPerline = self.editCenter.getImgShape()
        qImg = QImage(self.editCenter.getImgData(), self.widthImg, self.heightImg, bytesPerline, QImage.Format_RGB888)
        self.qpImg = QPixmap.fromImage(qImg)
        self.onInitFit()
        self.drawImg()

    def drawImg(self):
        qpImg = self.qpImg.scaled(self.showWidth, self.showHeight)
        self.label_view.setPixmap(qpImg)
        self.label_view.resize(self.showWidth + 10, self.showHeight + 10)
        # self.scrollArea.resize(self.showWidth, self.showHeight)
        # self.widget.resize(self.showWidth, self.showHeight)

        self.label_view.setAlignment(Qt.AlignLeft | Qt.AlignTop)

    @Slot()
    def updateQImg(self):
        self.widthImg, self.heightImg, bytesPerline = self.editCenter.getImgShape()
        qImg = QImage(self.editCenter.getImgData(), self.widthImg, self.heightImg, bytesPerline, QImage.Format_RGB888)
        self.qpImg = QPixmap.fromImage(qImg)
        self.drawImg()

    def getImgSize(self):
        return self.widthImg, self.heightImg

    def getViewSize(self):
        return self.label_view.width(), self.label_view.height()

    def onMouseDown(self, event):
        if not self.editCenter.bImgExist:
            return

        if event.button() == Qt.RightButton:
            if self.editCenter.currMode == REF_MODE:
                self.editCenter.popTmpPoint()
                self.editCenter.drawTmpPoint(bDrawPoint=True, bDrawLine=False)
                self.mouseState = MOUSE_STATE_NONE
            elif self.editCenter.currMode == ROI_MODE:
                self.editCenter.popTmpPoint()
                self.editCenter.drawTmpPoint(bDrawPoint=True, bDrawLine=True)
            return



        pos = list(event.position().toPoint().toTuple())
        x, y = pos
        if x < 0 or x >= self.showWidth or y < 0 or y >= self.showHeight:
            return
        posImg = self.posToImg(pos)

        # Add double click event
        if event.type() == QEvent.MouseButtonDblClick and event.button() == Qt.LeftButton:
            if self.editCenter.currMode == ROI_MODE:
                self.editCenter.setTmpPoint(posImg)
                self.editCenter.setTmpPoint((-1, -1))
                self.editCenter.drawTmpPoint(bDrawPoint=True, bDrawLine=True)
                self.mouseState = MOUSE_STATE_NONE
                return

        if self.editCenter.currMode == REF_MODE:
            if self.mouseState == MOUSE_STATE_NONE:
                self.editCenter.setTmpPoint(posImg)
                self.editCenter.drawTmpPoint(bDrawPoint=True, bDrawLine=False)
                self.mouseState = MOUSE_STATE_DRAW_POINTS
            elif self.mouseState == MOUSE_STATE_DRAW_POINTS:
                self.editCenter.setTmpPoint(posImg)
                self.editCenter.drawTmpPoint(bDrawPoint=True, bDrawLine=True)
                self.mouseState = MOUSE_STATE_NONE
        elif self.editCenter.currMode == ROI_MODE:
            self.editCenter.setTmpPoint(posImg)
            self.editCenter.drawTmpPoint(bDrawPoint=True, bDrawLine=True)

    def onMouseMove(self, event):
        pos = list(event.position().toPoint().toTuple())
        if not self.editCenter.bImgExist:
            return
        x, y = pos
        if x < 0 or x >= self.showWidth or y < 0 or y >= self.showHeight:
            return
        posImg = self.posToImg(pos)
        if self.editCenter.currMode == REF_MODE:
            if self.mouseState == MOUSE_STATE_DRAW_POINTS:
                self.editCenter.setTmpPoint(posImg)
                self.editCenter.drawTmpPoint(bDrawPoint=False, bDrawLine=True)

    def doNotingEvent(self, event):
        pass

    @Slot()
    def changeView(self):
        if self.editCenter.currViewMode == VIEW_HISTOGRAM_MODE:
            self.stackedWidget.setCurrentIndex(1)
            self.updateHistogram()
        else:
            self.stackedWidget.setCurrentIndex(0)

    def updateHistogram(self):
        dfContoursValue = pd.read_csv('/Users/haoyulin/Desktop/new_qt/PyQT/contours_data.csv')
        minX = 300
        maxX = 1000

        self.cvHistogram.figure.clear()
        ax1 = self.cvHistogram.figure.add_subplot(111)
        df_sorted = dfContoursValue.sort_values(by='Index')
        df_visible = df_sorted[(df_sorted['Index'] >= minX) & (df_sorted['Index'] <= maxX)]
        df_visible['Cumulative Diameter'] = df_visible['Diameter'].cumsum()
        ax1.bar(df_visible['Index'], df_visible['Diameter'], color='lightblue', label='Diameter Distribution')
        ax2 = ax1.twinx()
        ax2.plot(df_visible['Index'], df_visible['Cumulative Diameter'], color='red', label='Cumulative Diameter', marker='o')
        ax1.set_xlim(minX, maxX)
        self.cvHistogram.draw()

