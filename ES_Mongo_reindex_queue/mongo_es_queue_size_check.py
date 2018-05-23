from __future__ import print_function

import os
from datetime import datetime
import pymongo
from pymongo import MongoClient
import json
import boto3


client = boto3.client('sns')
RSJP_MONGODB_URI = os.environ['RSJP_MONGODB_URI']
CSMK_MONGODB_URI = os.environ['CSMK_MONGODB_URI']
mongoDBClient = pymongo.MongoClient(RSJP_MONGODB_URI)
RSJP_mongoDB = mongoDBClient.get_default_database()
mongoDBClient2 = pymongo.MongoClient(CSMK_MONGODB_URI)
CSMK_mongoDB = mongoDBClient2.get_default_database()
ALERT_THRESHOLD_COUNT = int(os.environ['ALERT_THRESHOLD_COUNT'])
SNS_ARN = os.environ['SNS_ARN']


def lambda_handler(event, context):
    print('Checking {} at {}...'.format('Mongo queue size for RSJP and CSMK production', event['time']))
    try:
        # counting for RSJP
        check_queue_size_publish_sns('RS_JP', RSJP_mongoDB)
        check_queue_size_publish_sns('CSMK', CSMK_mongoDB)
    except:
        print('Check failed!')
        raise
    else:
        print('Check passed!')
        return event['time']
    finally:
        print('Check complete at {}'.format(str(datetime.now())))


def check_queue_size_publish_sns(site, mongoDB):
    counts = mongoDB.es_reindex_queue.count()
    print(site, counts)
    if counts >= ALERT_THRESHOLD_COUNT:
        print('sending alerts')
        message = {"SITE": site, "ES_MONGO_QUEUE_SIZE": counts, "_timestamp": datetime.utcnow().isoformat()}
        response = client.publish(
            TargetArn=SNS_ARN,
            Message=json.dumps(message)
            )
    else:
        print('life goes well')
