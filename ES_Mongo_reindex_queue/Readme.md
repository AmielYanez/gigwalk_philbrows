
##Usage: 
It's run every 20 mins to send SMS and Emails through AWS SNS

## Technical details

### AWS SNS
- [Dashboard](https://console.aws.amazon.com/sns/v2/home?region=us-east-1#/home)
- Create a topic, which gives you an `arn` resource URI
- Create subscriptions, like SMS, email address, and etc.

### AWS lambda function
Implement the logic in `lambda_handler.handler` here, Simply query the Mongo collection size and check if it's over the threshold, if so, sending out an alert through SNS
 - There are many packages are needed, so I zipped every package already within the zip file.  For deployment to AWS lambda, we just need to deploy this zip file.