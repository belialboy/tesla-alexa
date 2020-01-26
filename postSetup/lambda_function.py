import json

def lambda_handler(event, context):
    # This function gets called when an activation is being requested
    # Look up the activation code to ensure it's valid
    # Use the un/pw provided to create an accessToken
    # Store the accessToken and refreshToken(?) in DDB
    # Profit!
    return {
        'statusCode': 200,
        'body': "<html><body>Activated</body></html>"
    }