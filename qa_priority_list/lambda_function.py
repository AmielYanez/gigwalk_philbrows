import os
from gc import gc
from models import Projects, Tickets
FILE_KEY = os.environ['FILE_KEY']
SHARE_ACCOUNTS = os.environ['SHARE_ACCOUNTS']


def generate_and_share_file(data, filename):
    sh = gc.create(filename)
    columns = [
        'Customer_email',
        'Campain',
        'ProjectUrl',
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


def priority_list_by_project(project):

    tickets = Tickets().get_tickets_by_project_id(project[0])
    generate_and_share_file(tickets, 'QA_PRIORITY_LIST_{}'.format(project[0]))


def lambda_handler(event, context):

    wks = gc.open_by_key(FILE_KEY).sheet1
    project_ids = wks.col_values(1)
    if not project_ids:
        return "No projects found"
    projects = Projects().get_projects_by_id_list(project_ids)
    for project in projects:
        priority_list_by_project(project)
    return 'Done'