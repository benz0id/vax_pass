import qrcode
from PIL import Image
import os.path
from user import User

class QRGenerator:
    """A class designed to encode QR codes that transmit and interpret vaccine
    verification info.
    ---Attributes---

    """
    _qr: qrcode.QRCode
    
    #Initializes QRGenerator class
    def __init__(self):
        self._qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )

    def generate_simple_qr(self, user: User, dest: os.path):
        """Generates an unencrypted QR code containing the <name> and <userid>.
        Stores the QR code as a png in <dest>.
        """

        dest_path = os.path.join(dest, "qrcode.png")
        self._qr.add_data(user.get_user_string())
        self._qr.make(fit=True)
        img = self._qr.make_image(fill_color="black", back_color="white")
        self._qr.clear()
        img.save(dest_path)
        # TODO handle image deletion






