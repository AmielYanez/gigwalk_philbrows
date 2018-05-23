## Motivations: 
1. The development cycle is taking too long to deliver functionalities-- it needs to be gone through BE API development, FE app development, QA, fixing bugs and then finally release.  
2. a lot of support requests may or may not be applicable to the later projects-- we want to build and support the CSMs and the support but we also want to build our applications with a more thoughtful approach and a better design if the feature is critical.
3. I also want to invest a little bit of time building these tools that Support/CSM could use those by themselves and hence saving engineering time because I am super lazy, so it's more of **"don't bug me, this is the tool for you, go figure!"** attitude here :)
4. But we need to find a **BALANCE to NOT randomly build** such tools vs building it within our product. Although these tools may or may not be suitable to merge into the core applications, this needs to be **as light as possible and they could be THROWN AWAY later**
5. It serves a framework for custom integration, e.g. partners who want to do integrations but may not have sufficient knowledge to build.  And a lot of custom logic could be left outside of the core applications.
 
## Main idea: 
Writing some microservice tools that could help CSM and support team to perform tasks, such that the tools could be deployed and used by end user quickly and could be thrown away with a little cost-- ideally 100~200 lines of code and 8-16 hours dev. time and those are not needed to be 100% robust.

### Example Use cases: 
1. Implemented: Gigwalkers lookup, given a Gigwalker email, it will look up Gigwalker's assigned certifications and his applied tickets.
2. Implemented: Getting mongo ES queue size and send out an alert to engineers.
3. Unblacklist Gigwalkers, if a Gigwalker is blacklisted, there's no way to unblock him (neither API/FE able to do so)-- the only way as of now is to stamped the application status on DB manually by BE engineers
4. As a marketing person, I should be able to send push notifications message M to a specific set of users (say users within X miles within zipcode Y)
5. and probably more...


## A little bit of overview of technical details
See more details under each folder's README.md
### Use case 1: Getting a Gigwalker Info:
I am describing how I implemented #1 use case here, and it needs not to be a slash command, it could be a curl, or a command line tool, as long as it's easily accessible to non-technical team members.  

But the main idea is to utilize serverless AWS lambda function to execute certain tasks.  And the AWS lambda function could be triggered by the different ways-- basically, a user sends a request through Slack, it posts an HTTP request to AWS API gateway, it then triggers AWS lambda function to query Postgres DB and getting all the information, and then populate the response back to Slack.  

### Use case 2: Getting mongo queue size and alert:
It's basically a scheduled lambda function that executes every 20 mins to get the size of a mongo collection size, once it's over a certain threshold, it sends an alert through AWS SNS service.