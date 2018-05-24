import os
from gc import gc
from models import Projects, Tickets
FILE_KEY = os.environ['FILE_KEY']

def generate_file(data, filename):
    sh = gc.create(filename)
    columns = ['ticket_id', 'link']
    sh.insert_row(columns)
    for row in data:
        sh.insert_row(row)

def priority_list_by_project(project):

    tickets = Tickets().get_tickets_by_project_id(project[0])

    #############
    #### TODO: implement logic to create prority list
    #############

    # generate_file(data, 'QA_PRIORITY_LIST')


def lambda_handler(event, context):

    wks = gc.open_by_key(FILE_KEY).sheet1
    project_ids = wks.col_values(1)
    if not project_ids:
        return "No projects found"
    projects = Projects().get_projects_by_id_list(project_ids)
    for project in projects:
        priority_list_by_project(project)
    return 'Done'