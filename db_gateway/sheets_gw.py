import gspread
import os.path
from typing import List
from time import sleep

from oauth2client.service_account import ServiceAccountCredentials

JSON_PATH = os.path.join("db_gateway", "my_creds.json")
SPREADSHEET_NAME = 'Dummy Database'

SEMI = 's'
FULL = 'f'


class InvalidLoadParameter(Exception):
    """Raised when unknown parameters are passed to a database during its
    instantiation."""

class LoadDatabaseError(Exception):
    """Raised when a database cannot be loaded from remote. Caused by
    ConnectionError"""


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
    return client.open(sheet_name).Sheet1


class SheetsGateway:
    """A gateway class connecting to the google sheets API"""
    sheet: gspread.Worksheet
    _first_names: List[str]
    _last_names: List[str]
    _user_ids: List[int]
    _user_SINs: List[int]
    _birthdays: List[int]

    def __init__(self, mode: str) -> None:
        """Initialises the sheets gateway. Iff mode == SEMI, loads first names,
        last name, and user ids. Iff <mode> == FULL, loads the full suite of
        user data."""
        self.sheet = get_sheet(get_client(), SPREADSHEET_NAME).sheet1
        self._first_names = []
        self._last_names = []
        self._birthdays = []
        self._user_ids = []
        self._user_SINs = []

        success = False
        if mode == SEMI:
            success = self.load_semi()
        elif mode == FULL:
            success = self.load_full()
        else:
            raise InvalidLoadParameter("Unknown parameter: " + mode)

        if not success:
            raise LoadDatabaseError("Failed to connect to database. Check your"
                                    "internet connection")

    def load_full(self) -> bool:
        """Loads the full suite of user data. Returns true iff successful"""
        attempts = 0
        success = False
        while not success and attempts < 5:
            try:
                self._first_names = self.sheet.col_values(1)[1:]
                self._last_names = self.sheet.col_values(2)[1:]
                self._user_ids = self.sheet.col_values(3)[1:]
                self._birthdays = self.sheet.col_values(4)[1:]
                self._user_SINs = self.sheet.col_values(5)[1:]
                success = True
            except gspread.exceptions.APIError:
                attempts += 1
            except ConnectionError:
                attempts += 1
            if not success:
                sleep(0.2)
        return success

    def load_semi(self) -> bool:
        """Only loads first names, last name, and user ids. Returns true iff
        successful"""
        attempts = 0
        success = False
        while not success and attempts < 5:
            try:
                self._first_names = self.sheet.col_values(1)[1:]
                self._last_names = self.sheet.col_values(2)[1:]
                self._user_ids = self.sheet.col_values(3)[1:]
                success = True
            except gspread.exceptions.APIError:
                attempts += 1
            except ConnectionError:
                attempts += 1
            if not success:
                sleep(0.2)
        return success

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
