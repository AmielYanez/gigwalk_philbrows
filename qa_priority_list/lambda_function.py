import os
import gdocs
from models import Projects, Tickets
FILE_KEY = os.environ['FILE_KEY']


def priority_list_by_project(project):

    tickets = Tickets().get_tickets_by_project_id(project[0])
    gdocs.generate_and_share_file(tickets, 'QA_PRIORITY_LIST_{}'.format(project[0]))


def lambda_handler(event, context):

    wks = gdocs.open_sh(FILE_KEY)
    project_ids = wks.col_values(1)
    if not project_ids:
        return "No projects found"
    projects = Projects().get_projects_by_id_list(project_ids)
    for project in projects:
        priority_list_by_project(project)
    return 'Done'