from __future__ import print_function

import os
import time
from datetime import datetime
import urllib
from urllib2 import urlopen
import psycopg2

SITE = os.environ['site']  # URL of the site to check, stored in the site environment variable, e.g. https://aws.amazon.com
EXPECTED = os.environ['expected']  # String expected to be on the page, stored in the expected environment variable, e.g. Amazon
DB_HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PWD = os.environ.get('DB_PWD')

def validate(token, team_domain):
    return EXPECTED ==token and team_domain == 'gigwalk'

def _get_certs(cur, email):
    certs = []
    sql_stmt = "select c.id, c.email, cs.id, cs.title from customers c left outer join customer_cert_associations ca on ca.customer_id = c.id join certifications cs on cs.id = ca.certification_id where lower(email)='{}' and c.organization_id = 5".format(email)
    cur.execute(sql_stmt)
    if cur.rowcount == 0:
        return []
    row = cur.fetchone()
    while row is not None:
        certs.append(row)
        row = cur.fetchone()
    return certs

def _get_tickets(cur, customer_id):
    tickets = []
    sql_stmt = "select os.title, t.id, t.status, case when t.assigned_customer_id={} then 'Yes' else 'No' end as ASSIGNED_TO_ME, t.approval_status, dm.status, os.organization_id from tickets t, organization_subscriptions os, doubleoptin_map dm where t.id = dm.ticket_id and os.id = t.organization_subscription_id and dm.customer_id = {}".format(customer_id, customer_id)
    cur.execute(sql_stmt)
    if cur.rowcount == 0:
        return []
    row = cur.fetchone()
    while row is not None:
        tickets.append(row)
        row = cur.fetchone()
    return tickets

def lambda_handler(event, context):
    try:
        if not validate(event.get('token'), event.get('team_domain')):
            raise Exception('Validation failed')

        email = urllib.unquote(event.get('text')).lower() if event.get('text') else None
        certs = []
        tickets = []
        customer_id = None
        if not email:
            return {"text": "hey I need the Gigwalker's email"}
        try:
            conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PWD)
            cur = conn.cursor()
            # get certifications
            certs = _get_certs(cur, email)
            if not certs:
                return {"text": "YO! who is this guy, I cannot recognize him"}
            customer_id = certs[0][0]
            tickets = _get_tickets(cur, customer_id)

            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            return {"text": error}
        finally:
            if conn is not None:
                conn.close()
        cert_json = {
          "fallback": "Required plain-text summary of the attachment.",
          "color": "#36a64f",
          "pretext": "Assigned certifications",
          "fields": [{"title": cert[3], "value": cert[2], "short":True} for cert in certs],
          "footer": "Certifications",
          "footer_icon": "https://platform.slack-edge.com/img/default_application_icon.png"
        }
        attachments = [cert_json]
        
        for ticket in tickets:
            attachments.append({
              "fallback": "Required plain-text summary of the attachment.",
              "color": "#3B5998",
              "pretext": ticket[0],
              "title": "https://next.gigwalk.com/tickets/{}/detail/{}".format(ticket[6], ticket[1]),
              "fields": [
                {
                  "title": "Ticket Status",
                  "value": ticket[2],
                  "short": True
                },
                {
                  "title": "ASSIGNED_TO_ME",
                  "value": ticket[3],
                  "short": True
                },
                {
                  "title": "Ticket Approval Status",
                  "value": ticket[4],
                  "short": True
                },
                {
                  "title": "My Application Status",
                  "value": ticket[5],
                  "short": True
                }
              ]
            })
        response = {
            "text": "ID: {}, Email:{}".format(customer_id, email),
            "attachments": attachments
        }
        return response
    except:
        return {"text": "Don't hack me, I am watching you!"}
    finally:
        print('Check complete at {}'.format(str(datetime.now())))
    