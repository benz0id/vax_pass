from vax_qr_generator import *
from vax_qr_reader import *
from user import *

"vax, first, last, birthday = user_input()"
reader = QRReader()

user = User()
user.user_signup()

qr = QRGenerator()
qr.generate_simple_qr(user, os.path.join("qr_images_output"))

reader_data = reader.read_qr(os.path.join("qr_images_output", "qrcode.png"))

user2 = User()
user2.user_from_qr(reader_data)
print(user2)

