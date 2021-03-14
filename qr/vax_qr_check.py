from vax_qr_reader import *
#from user import *

class QRCheck:
    
    def __init__(self):
        self.reader = QRReader()

    def check_db(self, folder, file):
        reader_data = self.reader.read_qr(os.path.join(folder, file))

        data = reader_data.split(":")

