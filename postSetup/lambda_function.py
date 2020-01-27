import json
import boto3
import requests
import os

def lambda_handler(event, context):
    # This function gets called when an activation is being requested
    ddb=boto3.resource('dynamodb')
    usersTable=ddb.Table(os.environ['usersTable'])

    # Look up the activation code to ensure it's valid
    user=usersTable.get_item(
        Key={
        'activationCode': json.loads(event["body"])['activationCode']
        })
    # Use the un/pw provided to create an accessToken
    token=requests.post(url="https://owner-api.teslamotors.com/oauth/token?grant_type=password",
        json= json.dumps({
            "grant_type": "password",
            "client_id": os.environ['teslaAPIClientId'],
            "client_secret": os.environ['teslaAPIClientSecret'],
            "email": json.loads(event["body"])['email'],
            "password": json.loads(event["body"])['password']
        }))

    # Store the accessToken and refreshToken(?) in DDB
    usersTable.update_item(
        Key={
            'activationCode': json.loads(event["body"])['activationCode'],
            'userId': user.userId
            },
        UpdateExpression="set accessToken = :t, refreshToken=:r, status=:s, expires=:e",
        ExpressionAttributeValues={
            ':t': json.loads(token.text)['access_token'],
            ':r': json.loads(token.text)['refresh_token'],
            ':s': "ready",
            ':e': json.loads(token.text)['created_at'] + json.loads(token.text)['expires_in']
        },
        ReturnValues="UPDATED_NEW"
        )
    # Profit!
    return {
        'statusCode': 200,
        'body': "<html><body>Activated</body></html>"
    }