from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import cv2
import time

class Thread(QThread):
    
    changePixmap = pyqtSignal(QImage, str, float, float, float) 
    cap = None
    def run(self):

        # cap = cv2.VideoCapture('SnapSave.io-Vision AI based Real-Time Vehicle Counting - Demo(720p).mp4')
        while True:
            ret, frame = self.cap.read()
            if ret:
                # https://stackoverflow.com/a/55468544/6622587
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                name = 'Car'
                height = 0.0
                width = 0.0
                length = 0.0
                self.changePixmap.emit(convertToQtFormat, name, height, width, length)
                time.sleep(0.03)

    def stop(self):
        self.terminate()