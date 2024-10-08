.PHONY: ui

ui:
	pyside6-uic UI/UI_MainWindow.ui -o UI/UI_MainWindow.py
	pyside6-uic UI/UI_MenuBar.ui -o UI/UI_MenuBar.py
	pyside6-uic UI/UI_ContentBar.ui -o UI/UI_ContentBar.py
	pyside6-uic UI/UI_StatisticsView.ui -o UI/UI_StatisticsView.py
	pyside6-uic UI/UI_Viewer.ui -o UI/UI_Viewer.py
	pyside6-uic UI/UI_HistogramBar.ui -o UI/UI_HistogramBar.py



    # 	for viewer behavior
	sed -i '' '40,44d' UI/UI_Viewer.py
	sed -i '' 's/self.label_view = QLabel(self.scrollAreaWidgetContents)/self.label_view = QLabel()/' UI/UI_Viewer.py
	sed -i '' '47,49d' UI/UI_Viewer.py
