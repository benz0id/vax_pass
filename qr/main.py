from input import *
from vax_qr_generator import *
from user import *

"vax, first, last, birthday = user_input()"

user = User()
user.create_user()
print(user)

qr = QRGenerator()
qr.generate_simple_qr(user, os.path.join("qr_images_output"))
#change

