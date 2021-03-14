import gspread
import os.path
from oauth2client.service_account import ServiceAccountCredentials

JSON_PATH = os.path.join("my_creds.json")


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
    """A gateway class connecting to the


