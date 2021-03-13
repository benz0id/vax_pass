import qrcode
from PIL import Image
from qrcode.image.pure import PymagingImage
import os.path

class QR_Generator:
    """A class designed to encode QR codes that transmit and interpret vaccine
    verification info.
    """
    qr: qrcode.QRCode

    def __init__(self):
        self.qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )

    def generate_simple_qr(self, name: str, userid: int, dest: str):
        """Generates an unencrypted QR code containing the <name> and <userid>.
        Stores the QR code as a png in <dest>.
        """
        dest_path = os.path.join(dest, "qrcode.png")
        self.qr.add_data(''.join([name, ':', str(userid)]))
        self.qr.make(fit=True)
        img = self.qr.make_image(fill_color="black", back_color="white")
        self.qr.clear()
        img.save(dest_path)





