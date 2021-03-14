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
    _user_SIs: List[int]

    def __init__(self):
        """Initialises the sheets gateway """
        self.sheet = get_sheet(get_client(), SPREADSHEET_NAME)

    def get_first_names(self):
        return self._first_names

    def get_last_names(self):
        return self._last_names

    def get_user_ids(self):
        return self._user_ids

    def get_SIs(self):
        return self._user_SIs




