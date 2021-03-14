import gspread
import os.path
from typing import List

from oauth2client.service_account import ServiceAccountCredentials

JSON_PATH = os.path.join("db_gateway", "my_creds.json")
SPREADSHEET_NAME = 'Dummy Database'


def get_client() -> gspread.client:
    """Generates the client obj necessary to necessary to access the sheets API.
    """
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        JSON_PATH, scope)
    return gspread.authorize(creds)


def get_sheet(client: gspread.client,
              sheet_name: str) -> gspread.Spreadsheet:
    """Opens the spreadsheet with <sheet_name> using the given <client>.
    Raises: gspread.SpreadsheetNotFound if the spreadsheet is not found."""
    return client.open(sheet_name).sheet1


class SheetsGateway:
    """A gateway class connecting to the google sheets API"""
    sheet: gspread.Spreadsheet
    _first_names: List[str]
    _last_names: List[str]
    _user_ids: List[int]
    _user_SINs: List[int]
    _birthdays: List[int]

    def __init__(self):
        """Initialises the sheets gateway """
        self.sheet = get_sheet(get_client(), SPREADSHEET_NAME)

    def load_full(self) -> bool:
        """Loads the full suite of user data. Returns true iff successful"""

    def load_semi(self) -> bool:
        """Only loads first names, last name, and user ids. Returns true iff
        successful"""


    def get_first_names(self) -> List[str]:
        """Gets a list containing all user's first names"""
        return self._first_names

    def get_last_names(self) -> List[str]:
        """Gets a list containing all user's last names"""
        return self._last_names

    def get_user_ids(self) -> List[int]:
        """Gets a list of all user ids"""
        return self._user_ids

    def get_SINdex(self, sin: int) -> int:
        """If a user with <sin> exists, returns the index of that user.
        Otherwise, returns -1."""
        for i in range(0, len(self._user_SINs)):
            if self._user_SINs[i] == sin:
                return i
        return -1

    def get_birthdays(self) -> List[int]:
        """Gets a list of all user birthdays"""
        return self._user_SINs






