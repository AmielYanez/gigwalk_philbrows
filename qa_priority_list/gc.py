import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials
CREDENTIALS = os.environ['CREDENTIALS']
# TODO: move this to a env var so we can update permisions without deployment
credentials_json = json.loads(CREDENTIALS)

scope = [
  'https://spreadsheets.google.com/feeds',
  'https://www.googleapis.com/auth/drive',
  'https://www.googleapis.com/auth/spreadsheets'
]
credentials = ServiceAccountCredentials.from_json_keyfile_dict(credentials_json, scope)

gc = gspread.authorize(credentials)
