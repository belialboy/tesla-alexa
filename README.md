# tesla-alexa
This is a python Alexa project that extends the work done at https://tesla-api.timdorr.com/ and allows you to monitor and control various functions of your car though voice commands.

## Pre-requisites
These are the things you'll need to install and prepare before you attempt to install this skill
* AWS Developer account
* AWS Console account
* AWS-CLI installed `pip install aws-cli`
* AWS credentials available for your terminal session
* Have python3.7 installed (Or be using a virtualenv that uses python3.7)
* AWS-SAM installed `pip install ask-sdk`
* You may want to check that the Client ID and Secret are correct and current: [https://pastebin.com/pS7Z6yyP], and update the `parameters.ini` file appropriately.
* A Tesla account with email and password
* At least one Tesla vehicle

## Skill Installation

* Update `parameters.ini` file with the Skill ID

## Backend Installation

Run the following commands:

`sam build`
`sam package --s3-bucket <bucket-name> --output-template-file ./out-template.yml`
`aws cloudformation deploy --template-file out-template.yml --stack-name <StackName> --capabilities CAPABILITY_NAMED_IAM --parameter-overrides $(cat parameters.ini`

## Setup

1. Open the skill using the Alexa invocation "Alexa open Tesla"
2. Alexa will respond with an activation code.
3. Open a browser to the URL provided followinf the cloudformation deployment command (you can find this by running the following command: `aws cloudformation describe-stacks --stack-name <StackName> --query 'Outputs[*]'`)
4. Enter the activation code along with your Tesla Account credentials (The system does not record or store these)
5. Return to your Alexa, and open the skill again with "Alexa open Tesla"
6. Ask it to honk "Honk"
7. Listen for your car to honk twice.

## Assumptions

* You only have one Tesla vehicle
* You trust all those who have access to your Alexa devices!