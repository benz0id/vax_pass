import qrcode
from PIL import Image

class QR_Generator:
    """A class designed to encode QR codes that transmit and interpret vaccine
    verification info.
    """

    def __init__(self):
        pass

    def generate_simple_qr(self, name: str, userid: int):
        """Generates an unencrypted QR code containing the <name> and <userid>.
        """
