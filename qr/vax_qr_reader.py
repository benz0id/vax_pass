import cv2 as cv
import os.path

class QRReader:
    """Pulls COVID data from a QR code"""
    detector: cv.QRCodeDetector

    def __init__(self):
        self.detector = cv.QRCodeDetector()

    def read_qr(self, qr_path: os.path) -> str or None:
        """Reads a string from a given image containing a QR code contained in
        <path>. Returns a string if data is readable, none otherwise."""

        img = cv.imread(qr_path)
        data, bbox, straight_qrcode = self.detector.detect(img)
        if bbox 




