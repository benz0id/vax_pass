from input import *
from vax_qr_generator import *
from vax_qr_reader import *
from user import *


user = User()
user.create_user()
print(user)

qr = QRGenerator()
qr.generate_simple_qr(user, os.path.join("qr_images_output"))

reader = QRReader()
reader_data = reader.read_qr(os.path.join("qr_images_output", "qrcode.png"))

user2 = User()
user2.user_from_qr(reader_data)
print(user2)
#sheets2
