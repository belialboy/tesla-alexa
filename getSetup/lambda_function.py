
import boto3

def lambda_handler(event, context):
    html = "<html><head>Alexa for Tesla Activation and Signup</head><body><form action=\"POST\"><table><tr><td>Activation Code</td><td><input type=\"text\" name=\"activation\" /></td></tr><tr><td>Tesla username</td><td><input type=\"text\" name=\"email\" /></td></tr><tr><td>Tesla password</td><td><input type=\"password\" name=\"password\" /></td></tr><tr><td></td><td><input type=\"submit\" /></td></tr></table></form></body></html>"
    return {
        'statusCode': 200,
        'body': html
    }