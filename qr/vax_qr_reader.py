import cv2 as cv
import os.path
import pyzbar.pyzbar as pyzbar
from qr_io_exceptions import QRReadError


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

    def read_qr_camera(self) -> str:
        """Reads qr code from camera"""

        cap = cv.VideoCapture(0)

        while True:

            _, frame = cap.read()

            decodedObjects = pyzbar.detectAndDecode(frame)

            for obj in decodedObjects:
                return obj.data

            cv.imshow("Frame", frame)

            key = cv.waitKey(1)

            if key == 27:
                break
