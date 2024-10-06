from PySide6.QtWidgets import QMainWindow, QWidget, QStackedWidget
from PySide6.QtCore import QSize
from UI.UI_MainWindow import Ui_MainWindow
from View.MenuBar import MenuBar
from View.Viewer import Viewer
from View.ContentBar import ContentBar
from View.StatisticsView import StatisticsView
from View.HistogramBar import HistogramBar
import Model.MacroDefine as MacroDefine

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.loadComplete()
        self.qpImg = None

    def loadComplete(self):
        self.menuBar = MenuBar(self.MenuBar)
        self.viewer = Viewer(self.Viewer)
        self.contentBar = ContentBar(self.ContentBar)
        self.histogramBar = HistogramBar(self.HistogramBar)
        self.bindEvent()

    def bindEvent(self):
        self.viewer.I_EVT_CHANGE_BAR_VIEW.connect(self.changeCntStackWidget)

    def changeCntStackWidget(self, mode):
        self.CntStackWidget.setCurrentIndex(mode)
        if mode == MacroDefine.CNT_HIST_MODE:
            self.histogramBar.updateHistogram()


