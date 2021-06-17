from __future__ import print_function
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from typing import Dict

import numpy as np
import os.path
import pandas as pd


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = "1j46GF1TNc9nI6s7CPbWtO1JWsI6X0H-00EBN6N9tcDk"
RANGE_NAMES = [
    "Form Responses 1!A1:G1",
    "Form Responses 1!A2:G2",
    "Form Responses 1!A3:G3",
    "Form Responses 1!A4:G4",
    "Form Responses 1!A5:G5",
    "Form Responses 1!A6:G6"
]


def format_data(data: list[Dict]) -> pd.DataFrame:
    """
    Turn data collected from a spreadsheet into a pandas data frame.
    """
    # Getting the names of the columns from the first row of spreadsheet data.
    columns = data[0]['values'][0]

    rows = []
    for row in data[1:]:
        values = row['values'][0]
        rows.append(values)

    df = pd.DataFrame(np.array(rows), columns=columns)

    return df

if __name__ == "__main__":
    print("Beginning Authentication process...")

    # Make use of user's access token if it already exists.
    credentials = None
    if os.path.exists('token.json'):
        credentials = Credentials.from_authorized_user_file('token.json', SCOPES)
            
    # If credentials do not exist or not valid, we need user to authenticate first.
    if not credentials or not credentials.valid:
        # If the credentials exist, and they're expired, and there is a refresh token (not None).
        if credentials and credentials.expired and credentials.refresh_token:
            # Refresh the access token for these credentials.
            credentials.refresh(Request())
        else:
            # Creaates a flow variable based on our credentials.
            # Browser opens, requests a sign-in to google account
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            credentials = flow.run_local_server(port=0)
        # Save the credentials to the token file so they may be used again.
        with open('token.json', 'w') as token:
            token.write(credentials.to_json())

    print("Authentication Complete...")

    # Build the API service for google sheets.
    service = build('sheets', 'v4', credentials=credentials)
    spreadsheet = service.spreadsheets().values().batchGet(spreadsheetId=SPREADSHEET_ID, ranges=RANGE_NAMES).execute()
    range_data = spreadsheet.get('valueRanges', [])

    # Turn the data into a datframe so it is easier to manipulate.
    plasma_bank = format_data(range_data)
    plasma_bank.to_csv("donors.csv")
