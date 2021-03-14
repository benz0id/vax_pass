from input import *
from vax_qr_generator import *
from user import *

"vax, first, last, birthday = user_input()"

user = User()
user.create_user()
print(user.get_user_string())

'''qr = QRGenerator()
qr.generate_simple_qr(vax, first, last, birthday, 0, os.path.join(
    "qr_images_output"))'''
#change

