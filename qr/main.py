from input import *
from vax_qr_generator import *
from vax_qr_check import QRCheck
from user import *

"vax, first, last, birthday = user_input()"
generator = QRGenerator()
validator = QRCheck()

user = User()
user.user_signup()
while True:
    cmd = ''
    while cmd != 'Show QR' or cmd != 'Read QR':
        cmd = input("Enter 'Read Qr' to validate another user's QR. Enter "
                    "'Show QR' to show your QR code.")
        if cmd == 'ShowQR':
            generator.generate_simple_qr(user, os.path.join("qr_images_output"))
            image = Image.open(os.path.join("qr_images_output", "qrcode.png"))
        else:
            validator.scan_and_validate()


