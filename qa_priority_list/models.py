import os
import psycopg2

DB_HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PWD = os.environ.get('DB_PWD')

class Model:
    def __init__(self):
        self.conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PWD)

    def _execute_query(self, query):
        data = []
        cur = self.conn.cursor()
        cur.execute()
        if cur.rowcount == 0:
            return []
        row = cur.fetchone()
        while row is not None:
            data.append(row)
            row = cur.fetchone()
        return data


class Projects(Model):

    def get_projects_by_id_list(self, ids):
        query = "SELECT * FROM organization_subscriptions where id in ({})".format(",".join(ids))
        return self._execute_query(query)


class Tickets(Model):

    def get_tickets_by_project_id(self, project_id):
        query = "SELECT * FROM tickets where organization_subscription_id = {}".format(project_id)
        return self._execute_query(query)