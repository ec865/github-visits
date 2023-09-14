import json
import logging
import boto3
from datetime import datetime


logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Get the service resource.
client = boto3.resource('dynamodb')
table_name = 'visits'
table = client.Table(table_name)
    
def add_visit(data):
    try:
        table.put_item(Item=datetime.now())
        return {
        'statusCode': 200,
        'body': json.dumps('New visit has been added!')
        }

    except:
        return {
        'statusCode': 400,
        'body': json.dumps('Error adding the visit!')
        }
        
def get_visits():
    try:
        print('aaaaaaaaaa')
        response = table.scan()['Items']
        print('bbbbbbbbbb')
        print(response)
        return {
        'statusCode': 200,
        'body': json.dumps(response)
        }

    except:
        return {
        'statusCode': 400,
        'body': json.dumps('Error getting the visits!')
        }
    
        
def lambda_handler(event, context):
    
    
    
    http_method = event['httpMethod']
    
    if (http_method == 'GET'):
        return get_visits()
    elif (http_method == 'POST'):
        return add_visit()
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('Error!')
        }
