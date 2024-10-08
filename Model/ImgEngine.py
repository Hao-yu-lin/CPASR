import cv2
import numpy as np

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

    def produceMaskImg(self, width, height, lstPts=None, color=(255, 255, 255), bReverse=False):
        if width < 0 or height < 0:
            return None

        if lstPts:
            mask = np.zeros((height, width), np.int32)
            npLstPts = np.array([lstPts], np.int32)
            npLstPts = npLstPts.reshape((-1, 1, 2))

            mask = cv2.polylines(mask, [npLstPts], True, color)
            mask = cv2.fillPoly(mask, [npLstPts], color)
        else:
            mask = np.ones((height, width), np.int32) * 255

        mask = np.uint8(mask)
        if bReverse:
            mask = cv2.bitwise_not(mask)
        return mask

    def blendImg(self, srcImg, srcWeight, maskImg, maskWeight, color=(255, 255, 255)):

        if srcImg is None or maskImg is None:
            return srcImg

        maskImg = cv2.cvtColor(maskImg, cv2.COLOR_GRAY2BGR)

        maskImg[np.where((maskImg == [255, 255, 255]).all(axis=2))] = list(color)

        maskImg = cv2.addWeighted(srcImg, srcWeight, maskImg, maskWeight, 0)
        return maskImg

    def contourDetect(self, roiImg, threshold = -1):
        print('[ImgEngine][contourDetect] contourDetect start')
        blueChannel = cv2.split(roiImg)[2]
        if threshold == -1:
            threshold = int(np.median(blueChannel) * 0.44)
        threshold = int(threshold)
        print('[ImgEngine][contourDetect] threshold:', threshold)
        _, mask = cv2.threshold(blueChannel, int(threshold), 255, cv2.THRESH_BINARY_INV)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        res = [contour for contour in contours if contour.size > 6]
        return res, threshold

    def updateContoursOnView(self, img, contours):
        if img is None or not contours:
            return img
        img = cv2.drawContours(img, contours, -1, (255, 0, 0), 2, lineType=cv2.LINE_AA)
        return img

    def calContorusArea(self, contour, scale):
        scaleSquare = scale * scale
        areaPixel = cv2.contourArea(contour)

        if len(contour) > 5:
            # cal minAreaRect
            _, rectSize, _ = cv2.minAreaRect(contour)
            areaRect = float(rectSize[0] * rectSize[1])

            # cal fitEllipse
            ellipse = cv2.fitEllipse(contour)
            areaEllipse = np.pi * ellipse[1][0] * ellipse[1][1]

            # areaOutLine choose that the closet value to areaRect
            areaOutLine = areaRect if abs(areaRect - areaEllipse) > abs(areaRect - areaEllipse) else areaEllipse


            # finalarea is the geometric mean of areaOutline and areaPixel
            finalArea = np.sqrt(areaOutLine * areaPixel)
        else:
            finalArea = areaPixel
        # translate mm to microns
        finalDiameter = np.sqrt(finalArea / np.pi) * 2 * 1000 * scale
        finalDiameter = self.diamterFix(scale, finalDiameter)
        finalArea = finalArea * scaleSquare
        return finalArea, finalDiameter

    def diamterFix(self, scale, diamter):
        # double diameterfix(const double & pixel_scal, const double & diameter)
        # {
        #     double a = 1.0 / (pixel_scal + 0.25);
        #     double t = std::pow(2.88, a);
        #     double f = -0.375 * (1.0 / t) + 0.0075;
        #
        #     doubl p = 2.453 * pixel_scal + 0.92;
        #     double diameter2 = diameter / 100.0;
        #     double new_sacle = f * diameter2 + p;
        #
        #     return diameter * new_sacle;
        # }
        a = 1.0 / (scale + 0.25)
        t = pow(2.88, a)
        f = -0.375 * (1.0 / t) + 0.0075
        p = 2.453 * scale + 0.92
        diameter2 = diamter / 100.0
        newScale = f * diameter2 + p
        return diamter * newScale

    def deleteCountour(self, lstContours, pos):
        # void DataBase::del_detect_vector(cv::Point2ipos)
        # {
        #     double pos_value;
        #     for (auto it = detect_contours.begin(); it != detect_contours.end();)
        #     {
        #         // 0 onside 1 inside -1 outside
        #         pos_value = cv::pointPolygonTest(*it, pos, false);
        #         if (pos_value == 1 | | pos_value == 0)
        #         {
        #                it = detect_contours.erase(it);
        #                 if (detect_contours.empty()){
        #                 set_flag->flag_contours = false;
        #                 }
        #                 return;
        #         } else {
        #             ++it;
        #
        #         }
        #     }
        # }
        posValue = -1
        tmpContours = lstContours.copy()
        for idx, contour in enumerate(lstContours):
            posValue = cv2.pointPolygonTest(contour, pos, False)
            if posValue == 1 or posValue == 0:
                tmpContours.pop(idx)
                return tmpContours
        print('[ImgEngine][deleteCountour] No contour deleted')
        return tmpContours


