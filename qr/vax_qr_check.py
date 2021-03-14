from db_gateway.sheets_gw import SheetsGateway
from qr.user import User
from vax_qr_reader import *
MAX_SCAN_TIME = 5

class QRCheck:
    """A class designed to inspect that validity of a user's QR code."""
    reader: QRReader
    gw: SheetsGateway

    def __init__(self):
        self.reader = QRReader()
        self.gw = SheetsGateway('s')

    def scan_and_validate(self) -> None:
        """Scans for a QR using the camera, validates user encoded by QR,
        and prints appropriate message according to user status."""
        user = self.scan()
        if user is None:
            print("Bad read or invalid QR.")
            return

        if self.validate(user):
            print(user.__str__() + " is vaccinated.\nConfirm indentity using "
                                   "photo ID if necessary.")
        else:
            print("User is not registered as being vaccinated.")

    def scan(self) -> User or None:
        """Scans using QR reader. Returns user iff successful,
        None otherwise. """
        data = self.reader.read_qr_camera(MAX_SCAN_TIME)
        if data:
            user = User()
            user.user_from_qr(data)
            return user
        else:
            return None

    def validate(self, user: User) -> bool:
        """Checks whether the given user is present in the database."""
        user_ids = self.gw.get_user_ids()
        first_names = self.gw.get_first_names()
        last_names = self.gw.get_last_names()
        first, last, uid = user.get_name_and_id()

        i = 0
        found = False
        while not found and i < len(user_ids):
            if uid == user_ids[i]:
                found = True

        if first == first_names[i] and last == last_names[i]:
            in_db = True
        else:
            in_db = False
        return in_db

    """
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

        while not found and index < len(user_ids):
            if data[4] == user_ids[index]:
                found = True

        if data[1] == first_names[index] and data[2] == last_names[index]:
            in_db = True

        return in_db"""




