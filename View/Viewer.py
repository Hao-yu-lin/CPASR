from PySide6.QtCore import Qt, QEvent, QRect, QSize
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QWidget, QStackedWidget, QScrollArea
from PySide6.QtCore import Signal, Slot

from Controller.ImgEditCenter import imgEditCenter
from Model.PanZoom import PanZoom
from Model.StatisticsModel import StatisticsModel
from Model.AnalysisDataModel import analysisDataModel
from Controller.DataEditCenter import dataEditCenter
from UI.UI_Viewer import Ui_Viewer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import Model.MacroDefine as MacroDefine


# self.scrollAreaWidgetContents = QWidget()
# self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
# self.scrollAreaWidgetContents.setGeometry(QRect(-2, 0, 1036, 597))
# self.scrollAreaWidgetContents.setMinimumSize(QSize(1036, 597))
# self.scrollAreaWidgetContents.setAutoFillBackground(False)
# self.label_view = QLabel()
# self.scrollArea.setWidget(self.label_view)


class Viewer(QWidget, Ui_Viewer, PanZoom, StatisticsModel):
    I_EVT_CHANGE_BAR_VIEW = Signal(int)
    I_EVT_ENABLE_SAVE_HISTOGRAM = Signal(bool)

    def __init__(self, widget):
        QWidget.__init__(self, widget)
        Ui_Viewer.__init__(self)
        PanZoom.__init__(self)
        StatisticsModel.__init__(self)
        self.widget = widget
        self.setupUi(widget)
        self.initComplete(widget)
        self.imgEditCenter = imgEditCenter
        self.dataEditCenter = dataEditCenter
        self.analysisDataModel = analysisDataModel
        self.widthImg = -1
        self.heightImg = -1
        self.qpImg = None
        self.mouseState = MacroDefine.MOUSE_STATE_NONE
        self.bindEvent()


    def initComplete(self, widget):
        self.stackedWidget = QStackedWidget(widget)
        self.stackedWidget.setMinimumSize(QSize(1036, 597))
        # Matplotlib FigureCanvas for histogram or chart
        self.cvHistogram = FigureCanvas(Figure())
        self.cvHistogram.setGeometry(QRect(12, 12, 1036, 597))
        self.cvHistogram.setMinimumSize(QSize(1036, 597))

        # Create scroll area for cvHistogram
        self.scrollAreaHistogram = QScrollArea(widget)
        self.scrollAreaHistogram.setObjectName(u"scrollAreaHistogram")
        self.scrollAreaHistogram.setStyleSheet(u"background-color: rgb(190, 190, 190);")
        self.scrollAreaHistogram.setMinimumSize(QSize(1036, 597))
        self.scrollAreaHistogram.setWidgetResizable(False)

        self.scrollAreaHistogram.setWidget(self.cvHistogram)  # Set cvHistogram as the scroll area's widget
        self.scrollArea.setWidget(self.label_view)  # Initially set the image view

        # Add both widgets (image and chart) to the stacked widget
        self.stackedWidget.addWidget(self.scrollArea)  # Index 0
        self.stackedWidget.addWidget(self.scrollAreaHistogram)  # Index 1

        # Add both widgets to the layout but show one at a time

        self.verticalLayout_2.addWidget(self.stackedWidget)

    def bindEvent(self):
        self.imgEditCenter.I_EVT_UPDATE_IMG.connect(self.updateQImg)
        self.dataEditCenter.I_EVT_UPDATE_HISTOGRAM.connect(self.drawHistogram)

    def bindMouseEvent(self):
        self.label_view.mousePressEvent = self.onMouseDown
        self.label_view.mouseMoveEvent = self.onMouseMove

    def unbindMouseEvent(self):
        self.label_view.mousePressEvent = self.doNotingEvent
        self.label_view.mouseMoveEvent = self.doNotingEvent

    def initImg(self):
        self.widthImg, self.heightImg, bytesPerline = self.imgEditCenter.getImgShape()
        qImg = QImage(self.imgEditCenter.getImgData(), self.widthImg, self.heightImg, bytesPerline, QImage.Format_RGB888)
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
        self.widthImg, self.heightImg, bytesPerline = self.imgEditCenter.getImgShape()
        qImg = QImage(self.imgEditCenter.getImgData(), self.widthImg, self.heightImg, bytesPerline, QImage.Format_RGB888)
        self.qpImg = QPixmap.fromImage(qImg)
        self.drawImg()

    def getImgSize(self):
        return self.widthImg, self.heightImg

    def getViewSize(self):
        return self.label_view.width(), self.label_view.height()

    def onMouseDown(self, event):
        if not self.imgEditCenter.bImgExist:
            return

        if event.button() == Qt.RightButton:
            if self.imgEditCenter.currMode == MacroDefine.REF_MODE:
                self.imgEditCenter.popTmpPoint()
                self.imgEditCenter.drawTmpPoint(bDrawPoint=True, bDrawLine=False)
                self.mouseState = MacroDefine.MOUSE_STATE_NONE
            elif self.imgEditCenter.currMode == MacroDefine.ROI_MODE:
                self.imgEditCenter.popTmpPoint()
                self.imgEditCenter.drawTmpPoint(bDrawPoint=True, bDrawLine=True)
            return



        pos = list(event.position().toPoint().toTuple())
        x, y = pos
        if x < 0 or x >= self.showWidth or y < 0 or y >= self.showHeight:
            return
        posImg = self.posToImg(pos)

        # Add double click event
        if event.type() == QEvent.MouseButtonDblClick and event.button() == Qt.LeftButton:
            if self.imgEditCenter.currMode == MacroDefine.ROI_MODE:
                self.imgEditCenter.setTmpPoint(posImg)
                self.imgEditCenter.setTmpPoint((-1, -1))
                self.imgEditCenter.drawTmpPoint(bDrawPoint=True, bDrawLine=True)
                self.mouseState = MacroDefine.MOUSE_STATE_NONE
                return
            elif self.imgEditCenter.currMode == MacroDefine.DEL_MODE:
                self.analysisDataModel.delContoursPoint(posImg)
                self.imgEditCenter.drawImg()
                return

        if self.imgEditCenter.currMode == MacroDefine.REF_MODE:
            if self.mouseState == MacroDefine.MOUSE_STATE_NONE:
                self.imgEditCenter.setTmpPoint(posImg)
                self.imgEditCenter.drawTmpPoint(bDrawPoint=True, bDrawLine=False)
                self.mouseState = MacroDefine.MOUSE_STATE_DRAW_POINTS
            elif self.mouseState == MacroDefine.MOUSE_STATE_DRAW_POINTS:
                self.imgEditCenter.setTmpPoint(posImg)
                self.imgEditCenter.drawTmpPoint(bDrawPoint=True, bDrawLine=True)
                self.mouseState = MacroDefine.MOUSE_STATE_NONE
        elif self.imgEditCenter.currMode == MacroDefine.ROI_MODE:
            self.imgEditCenter.setTmpPoint(posImg)
            self.imgEditCenter.drawTmpPoint(bDrawPoint=True, bDrawLine=True)

    def onMouseMove(self, event):
        pos = list(event.position().toPoint().toTuple())
        if not self.imgEditCenter.bImgExist:
            return
        x, y = pos
        if x < 0 or x >= self.showWidth or y < 0 or y >= self.showHeight:
            return
        posImg = self.posToImg(pos)
        if self.imgEditCenter.currMode == MacroDefine.REF_MODE:
            if self.mouseState == MacroDefine.MOUSE_STATE_DRAW_POINTS:
                self.imgEditCenter.setTmpPoint(posImg)
                self.imgEditCenter.drawTmpPoint(bDrawPoint=False, bDrawLine=True)

    def doNotingEvent(self, event):
        pass

    @Slot()
    def changeView(self):
        if self.imgEditCenter.currViewMode == MacroDefine.VIEW_HISTOGRAM_MODE:
            self.stackedWidget.setCurrentIndex(1)
            self.I_EVT_CHANGE_BAR_VIEW.emit(MacroDefine.CNT_HIST_MODE)
        else:
            self.stackedWidget.setCurrentIndex(0)
            self.I_EVT_CHANGE_BAR_VIEW.emit(MacroDefine.CNT_BAR_MODE)

    @Slot()
    def drawHistogram(self):
        self.cvHistogram.figure.clear()

        # resize cvHistogram according to self.showWidth self.showHeight
        self.cvHistogram.resize(self.showHistogramWidth, self.showHistogramHeight)

        plot = self.cvHistogram.figure.add_subplot(111)
        showType = self.dataEditCenter.showType
        dataInfo = self.dataEditCenter.getHistogramInfo()
        if showType == MacroDefine.SHOW_HIST_TYPE_DATA1:
            self.plotSingleHistogram(dataInfo, plot)
        elif showType == MacroDefine.SHOW_HIST_TYPE_BOTH:
            self.plotMultiHistogram(dataInfo, plot)
        self.cvHistogram.figure.tight_layout()  # 明確地為 self.cvHistogram 進行布局調整
        self.cvHistogram.draw()
        self.I_EVT_ENABLE_SAVE_HISTOGRAM.emit(True)

    def saveHistogram(self, filePath):
        # Save the histogram as an image
        self.cvHistogram.figure.savefig(filePath)
