from vax_qr_reader import *
from sheets_gw import *
#from user import *

class QRCheck:
    reader: QRReader
    gw: SheetsGateway
    
    def __init__(self):
        self.reader = QRReader()
        self.gw = SheetsGateway()

    def check_db(self, folder, file):
        in_db = False
        
        reader_data = self.reader.read_qr(os.path.join(folder, file))

        data = reader_data.split(":")
        
        user_ids = self.gw.get_user_ids()
        first_names = self.gw.get_first_names()
        last_names = self.gw.get_last_names()
        
        index = 0
        found = False
        
        # update reader with idnum
        
        while found == False and index < len(user_ids):
            if data[4] == user_ids[index]:
                found = True
                
        if data[1] == first_names[index] and data[2] == last_names[index]:
            in_db = True
        
        return in_db
            
        
        

