import qrcode
from PIL import Image
import os.path

class QRGenerator:
    """A class designed to encode QR codes that transmit and interpret vaccine
    verification info.
    ---Attributes---

    """
    qr: qrcode.QRCode

    def __init__(self):
        self.qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )

    def generate_simple_qr(self, is_vax: bool, name: str, userid: int,
                           dest: os.path):
        """Generates an unencrypted QR code containing the <name> and <userid>.
        Stores the QR code as a png in <dest>.
        """
        if is_vax:
            v_stat = "vax"
        else:
            v_stat = "novax"

        dest_path = os.path.join(dest, "qrcode.png")
        self.qr.add_data(''.join([v_stat, ':', name, ':', str(userid)]))
        self.qr.make(fit=True)
        img = self.qr.make_image(fill_color="black", back_color="white")
        self.qr.clear()
        img.save(dest_path)
        # TODO handle image deletion






