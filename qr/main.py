from input import *
from vax_qr_generator import *

vax, first, last, birthday = user_input()
qr = QRGenerator()
qr.generate_simple_qr(vax, first, last, birthday, 0, os.path.join(
    "qr_images_output"))
#change

