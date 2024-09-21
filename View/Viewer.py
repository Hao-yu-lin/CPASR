from PySide6.QtCore import Qt, Slot, QEvent
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QWidget

from Controller.ImgEditCenter import imgEditCenter
from Model.PanZoom import PanZoom
from UI.UI_Viewer import Ui_Viewer
from Model.MacroDefine import REF_MODE, ROI_MODE, MOUSE_STATE_NONE, MOUSE_STATE_DRAW_POINTS

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
        self.editCenter = imgEditCenter
        self.widthImg = -1
        self.heightImg = -1
        self.qpImg = None
        self.mouseState = MOUSE_STATE_NONE
        self.bindEvent()

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

