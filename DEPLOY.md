#DEPLOY

This file contains information about how to deploy the package
that you previously built in [PACKAGE](PACKAGE.md).

There are a few steps:
1. Gather information from SolarEdge Portal
1. Create an Alexa Skill that will use the Lambda function
1. Deploy the Lambda Function that we built in code
1. Connect the Skill and Function together
1. Test
1. Use every day

You will like want to have the [AWS CLI](https://aws.amazon.com/cli/)
installed. Also, take a few minutes and read:
* [Create a (Lambda) Function](https://docs.aws.amazon.com/lambda/latest/dg/getting-started-create-function.html)
* [Host a Custom Skill as an AWS Lambda Function](https://developer.amazon.com/docs/custom-skills/host-a-custom-skill-as-an-aws-lambda-function.html)


##SolarEdge Information

You will need an API key and your Site ID from the 
[SolarEdge Monitoring Portal](https://monitoring.solaredge.com/solaredge-web/p/login?locale=en_US).
This lets your deployed skill talk to your monitoring account.

Log into the monitoring portal using your credentials then:
1. Navigate to "Admin"
1. Go to the "Site Access" tab
1. Go to the "API Access" section
1. Read the SolarEdge API Terms and Conditions and check the box
1. Generate an API Key (using the "New key" button next to the field)
1. Copy the API Key and Site ID and store in the conf/site.py file
in the project


##Deploy to Lambda
It should be noted that the console experience changes frequently and these
instructions should be used as a guideline, not as a fact.

Sign up and log into the [Amazon Lambda](https://aws.amazon.com/lambda/) console.

Note that not all regions have the functionality we need, I've been using
us-west-1. The region you use has to support the Alexa Skills Kit trigger.

Follow the instructions to
[Create a Function](https://docs.aws.amazon.com/lambda/latest/dg/getting-started-create-function.html).

Another good article is:
[Host a Custom Skill as an AWS Lambda Function](https://developer.amazon.com/docs/custom-skills/host-a-custom-skill-as-an-aws-lambda-function.html)

When setting up the function:

1. From the Left Pane in the Designer, choose the "Alexa Skills Kit" as a
trigger. If the Alexa Skills Kit is not available as a trigger, find a region
that it is available in.

1. In the Function Code section
  * Choose the "Code Entry" to be "Upload a .zip file"
  * Choose the "Runtime" to be Python 3.x (whichever you used)
  * Choose the "Handler" to be solar_edge.handler (this corresponds to the handler
  defined in the solar_edge.py code)
  * Upload the .zip file created in the last step
  
1. You *must* add the following in the Environment Variables section
  * API_KEY <your SolarEdge API Key)
  * SIDE_ID <your SolarEdge Site ID)

Other items to be sure to follow in the instructions:
* Create a role from a template, once created, you can reuse it each
time you re-deploy the skill

You will want to enable Skill ID, you won't have a Skill ID until your
Amazon Skill is created, at least a shell of it. If it can't be saved,
hop down to the next section and get through the first steps of Create an
Alexa Skill to get a skill ID.

Once created, record the ARN at the top right of the page, it
looks something like this (where number is filled in):
`arn:aws:lambda:us-west-2:<number>:function:SolarEdge`.

##Create an Alexa Skill

It should be noted that the console experience changes frequently and these
instructions should be used as a guideline, not as a fact.

Sign up and log into the
[Alexa Skills Console](https://developer.amazon.com/alexa/console/ask?).

* Choose to "Create a Skill"
* In the skill model, choose "Custom"
* Press "Create Skill", and choose "Scratch"

In the "Endpoint" section:
* Note the Skill ID in the right pane, copy it and go back and finish
  the Lambda deployment, be sure to SAVE the Lambda. Copy the Lambda
  ARN.
* Paste the Lambda ARN into the "Default Region"
* Press "Save Endpoint"

Now move to the Intents and find the "JSON Editor". Review the file
`model/intents.json`, then copy/paste it into the JSON editor or 
drag and drop it onto the proper location at the top of the page.

Choose
* Save Model
* Build Model

Now go to the "Test" tab and try it out:
* Ask Solar Edge about this month
* Ask Solar Edge about today
* Ask Solar Edge about (date)

If you have your Alexa devices linked to your development account,
they should show up automatically! Start talking away!


