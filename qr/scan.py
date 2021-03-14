from vax_qr_reader import *
from user import *

reader = QRReader()
reader_data = reader.read_qr_camera()

user2 = User()
user2.user_from_qr(reader_data)
print(user2)
