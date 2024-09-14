from PySide6.QtWidgets import QMainWindow
from UI.UI_MainWindow import Ui_MainWindow
from View.MenuBar import MenuBar
from View.Viewer import Viewer
from View.ContentBar import ContentBar
from View.StatisticsView import StatisticsView

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
        self.statisticsView = StatisticsView(self.StatisticsView)



    # def resizeEvent(self, event):
    #     super().resizeEvent(event)
    #     if self.viewer.qpImg:
    #         self.viewer.initImg()



