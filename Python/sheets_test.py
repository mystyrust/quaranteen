# python3.9 Python/sheets_test.py

import json
import os
import google.auth
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from fic_stats_helper_2 import ficStatsHelper, getSession

with open('./Python/config.json', 'r') as config_file:
    config = json.load(config_file)
    
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = './Python/sandbox-test-credential.json'
SPREADSHEET_ID = config['spreadsheet_id']
SHEET_NAME = config['sheet_name']
MONTH="November"
ROW=7

credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('sheets', 'v4', credentials=credentials)

# values = [
#    ['=HYPERLINK("https://www.example.com", "Example Link")', '', "johndoe@example.com", "Product Manager", "USA"]
#   , ['=HYPERLINK("https://archiveofourown.org/series/2438830", "Example Link")', '', "johndoe@example.com", "Product Manager", "USA"]
#   , ["=HYPERLINK('https://archiveofourown.org/series/2438830', 'BTHB Bingo)'", ""]
#   , ['=HYPERLINK("https://archiveofourown.org/series/2438830", "BTHB Bingo)"', ""]
# ]

ficLinks = [  
    "https://archiveofourown.org/works/17866526" #example
]

session = getSession()
values = ficStatsHelper(ficLinks, session, MONTH)

body = {
    'values': values
}

# Specify the range in A1 notation
range_to_insert = f'{SHEET_NAME}!A{ROW}'  # Adjust columns as per your sheet structure

result = service.spreadsheets().values().append(
    spreadsheetId=SPREADSHEET_ID,
    range=range_to_insert,
    valueInputOption="USER_ENTERED",  
    body=body
).execute()

print(f"{result.get('updates').get('updatedCells')} cells appended.")
