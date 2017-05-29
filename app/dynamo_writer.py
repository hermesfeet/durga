import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('jules_memory')

table.put_item(
   Item={
        'user_id': 'ruan_3111',
        'Name': 'ruan',
        'Age': 30
    }
)



response = table.get_item(
   Key={
        'user_id': 'ruan_3111'
    }
)

item = response['Item']

print(item)
print("Hello, {}" .format(item))