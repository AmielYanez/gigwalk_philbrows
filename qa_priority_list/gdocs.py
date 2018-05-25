import os
import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials
CREDENTIALS = os.environ['CREDENTIALS']
SHARE_ACCOUNTS = os.environ['SHARE_ACCOUNTS']
# TODO: move this to a env var so we can update permisions without deployment
credentials_json = json.loads(CREDENTIALS)
scope = [
  'https://spreadsheets.google.com/feeds',
  'https://www.googleapis.com/auth/drive',
  'https://www.googleapis.com/auth/spreadsheets'
]

__all__ = ['GC']


credentials = ServiceAccountCredentials.from_json_keyfile_dict(credentials_json, scope)
gc = gspread.authorize(credentials)

def open_sh(file_key):
    return gc.open_by_key(file_key).sheet1

def generate_and_share_file(data, filename):
      sh = gc.create(filename)
      columns = [
          'Customer_Email',
          'Project_Title',
          'Project_Url',
          'QA_deadline_date',
          'Project_due_date',
          'Ticket_submitted_date',
          'Ticket_location',
          'Ticket_address',
          'Ticket_state',
          'TicketUrl',
          'Worker_id'
      ]
      sh.insert_row(columns)
      for row in data:
          sh.insert_row(row)

      share_file(sh)

def share_file(sh):
  emails = SHARE_ACCOUNTS.split(',')
  for email in emails:
      sh.share(email, perm_type='user', role='writer')
