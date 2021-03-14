import cv2 as cv
import os.path
from qr_io_exceptions import QRReadError
from time import sleep


class QRReader:
    """Pulls COVID data from a QR code"""
    _detector: cv.QRCodeDetector

    #Initializes QRReader class
    def __init__(self):
        self._detector = cv.QRCodeDetector()

    def read_qr(self, qr_path: os.path) -> str:
        """Reads a string from a given image containing a QR code contained in
        <path>. Returns a string if data is readable, none otherwise."""

        img = cv.imread(qr_path)
        data, pts, straight_qrcode = self._detector.detectAndDecode(img)
        if pts is not None:
            return data
        else:
            raise QRReadError("Failed to fetch data from image")

    def read_qr_camera(self, runtime: int) -> str:
        """Reads qr code from camera. Tries for <runtime> seconds."""

        cap = cv.VideoCapture(0)

        data = ''
        crude_run_time = 0
        while len(data.split(":")) != 4 & crude_run_time < runtime * 2:

            _, frame = cap.read()

            data, pts, straight_qrcode = self._detector.detectAndDecode(frame)

            if len(data.split(":")) == 4:
                return data


            cv.imshow("Frame", frame)

            key = cv.waitKey(1)

            if key == 27:
                break
            sleep(0.5)
            crude_run_time += 1
        return ''

