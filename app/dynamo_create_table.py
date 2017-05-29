from __future__ import print_function # Python 2/3 compatibility
import boto3
import os


dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="http://localhost:8000", aws_access_key_id='AKIAIYZX72H3BF2KL2WQ',
                          aws_secret_access_key='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')


table = dynamodb.create_table(
    TableName='Testing',
    KeySchema=[
        {
            'AttributeName': 'year',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'title',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'year',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'title',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)