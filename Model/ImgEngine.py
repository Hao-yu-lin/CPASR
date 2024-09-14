import cv2

class ImgEngine:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def decodeImg(self, path):
        if path == '':
            return None
        imgBGR = cv2.imread(path)
        imgRGB = self.imgBGR2RGB(imgBGR)
        return imgRGB

    def imgBGR2RGB(self, img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    def imgRGB2BGR(self, img):
        return cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    def drawPoints(self, img, point, color=(0, 255, 0)):
        if img is None or point is None:
            return img
        pointSZ = 10
        thickness = 4
        intPoint = (int(point[0]), int(point[1]))
        return cv2.circle(img, intPoint, pointSZ, color, thickness)

    def drawLine(self, img, startPts, endPts, color=(0, 255, 0)):
        if img is None or startPts is None or endPts is None:
            return img
        thickness = 2
        intStartPts = (int(startPts[0]), int(startPts[1]))
        intEndPts = (int(endPts[0]), int(endPts[1]))
        return cv2.line(img, intStartPts, intEndPts, color, thickness)

    def updatePtsOnView(self, img, lstPts, bDrawPoint=True, bDrawLine=True, color=(0, 255, 0)):
        if img is None or not lstPts:
            return img
        img = self.drawPoints(img, lstPts[0], color)
        for i in range(1, len(lstPts)):
            if bDrawPoint:
                img = self.drawPoints(img, lstPts[i], color)
            if bDrawLine:
                img = self.drawLine(img, lstPts[i - 1], lstPts[i], color)

        return img
