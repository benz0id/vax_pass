import cv2 as cv
import os.path

class QRReader:
    """Pulls COVID data from a QR code"""
    _detector: cv.QRCodeDetector

    def __init__(self):
        self._detector = cv.QRCodeDetector()

    def read_qr(self, qr_path: os.path) -> str or None:
        """Reads a string from a given image containing a QR code contained in
        <path>. Returns a string if data is readable, none otherwise."""

        img = cv.imread(qr_path)
        data, pts, straight_qrcode = self._detector.detectAndDecode(img)
        if pts is not None:
            return data
        else:
            return None

    """TODO:
    -write make_user which can convert a qr code to a user
    -if possible, make it two-way compatible; have it in both this and user.py
    """






