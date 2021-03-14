from qr_io_exceptions import QRReadError
from typing import Tuple
#from db_gateway.sheets_gw import LoadDatabaseError, SheetsGateway

class User:
    """A class to store a user's data.

    ---Attributes---
    vax - has the user been vaccinated? (Boolean)
    first_name - user's first name (String)
    last_name - user's last name (String)
    birthday - user's date of birth (int: YYYYMMDD)

    # TODO
    add self._idnum
    change all functions to reflect this change
    """
    _vax: bool
    _first_name: str
    _last_name: str
    _birthday: int

    #Initializes User class
    def __init__(self):
        self._vax = True
        self._first_name = ""
        self._last_name = ""
        self._birthday = 0

    def __str__(self):

        birthday_string = str(self._birthday)
        birthday_string = birthday_string[0:4] + "/" + birthday_string[4:6] + \
                          "/" + birthday_string[6:8]

        vax_string = "Not Vaccinated"
        if self._vax is True:
            vax_string = "Vaccinated"

        user_string = ""
        user_string = ("""Name: {} {}
Date of Birth: {}
Vaccination Status: {}""".format(self._first_name, self._last_name, birthday_string, vax_string))

        return user_string #TODO

    def get_name_and_id(self) -> Tuple[str, str, int]:
        """Returns the user's firstname, lastname, user id"""

    def get_qr_data(self):
        """Returns users attributes in a readable format for the qr generator.

        Format is: vax:first_name:last_name:birthday"""

        qr_string = "{}:{}:{}:{}".format(self._vax, self._first_name, self._last_name, self._birthday)

        return qr_string

    def create_user(self):
        # asks vaccination status (must be 'Yes' or 'No')
        vax_input = ""
        while vax_input not in ['Yes', 'yes', 'No', 'no']:
            vax_input = input("Have you been vaccinated? (Yes or No): ")

        # converts to Boolean
        if vax_input == "Yes":
            self._vax = True
        else:
            self._vax = False

        # gets name
        self._first_name = input("What is your first name?: ")
        self._last_name = input("What is your last name?: ")

        # gets birthday (must be 8 digits)
        while self._birthday < 10000000 or self._birthday > 99999999:
            self._birthday = int(
                input("What is your date of birth? (YYYYMMDD): "))

        '''if vax == True:
            print("{} {} has been vaccinated.".format(first_name, last_name))
        else:
            print("{} {} has not been vaccinated.".format(first_name, last_name))'''

        return

    def user_signup(self) -> bool:
        """Like create_user, but validates with social security number."""
        self.create_user()
        sin = 0
        while sin < 100000000 or sin > 999999999:
            sin = input("What is your SIN")

        print("Validating...")
        try:
            db = SheetsGateway('f')
        except LoadDatabaseError:
            print("Failed to reach host. Check your internet connection.")
            return False

        sin_ind = db.get_SINdex(sin)
        if sin_ind == -1:
            print("Your SIN is not valid")
        elif db.get_first_names()[sin_ind] != self._first_name:
            print("Name does not match entry in our database.")
        elif db.get_last_names()[sin_ind] != self._last_name:
            print("Name does not match entry in our database.")
        elif db.get_birthdays()[sin_ind] != self._birthday:
            print("Birthday does not match entry in our database.")
        else:
            print("You have successfully registered. Welcome, " +
                  self._first_name)
            return True
        return False

    def user_from_qr(self, user_str: str):
        """Extracts a user from a <user_str> of format:
        vax:first_name:last_name:birthday"""
        num_attr = 4
        try:
            attribs = user_str.split(':')
            if num_attr != len(attribs):
                raise QRReadError("Too many attributes read, assuming corrupted"
                                  " read")

            # Format is: vax:first_name:last_name:birthday

            if attribs[0] == 'True':
                self._vax = True
            else:
                self._vax = False

            self._first_name = attribs[1]
            self._last_name = attribs[2]
            self._birthday = int(attribs[3])
        except ValueError:
            raise QRReadError("Failed to convert string to int, "
                              "assuming bad QR read")









