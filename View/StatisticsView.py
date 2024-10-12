from UI.UI_StatisticsView import Ui_StatisticsView
from PySide6.QtWidgets import QWidget



class StatisticsView(QWidget, Ui_StatisticsView):

    def __init__(self, widget):
        super().__init__()
        self.setupUi(widget)
