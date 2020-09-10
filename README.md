# python-email-script-for-Azure-Devops
This is script can be used for sending email from Azure DevOps task. It can also send attachment.

# command to run script:

python send_email.py --fromid="<from_id>" --toid="<to_id>" --subject="<email subject>" --attachment="<attachment_file>" --body="<email_body>"



## Help:

fromid*: email id from the email should be sent.

toid*: email ids of the recepient, multiple email id should be coma seperated. ex: "test@gmail.com,test2@gmail.com,test3@gmail.com".

subject*: subject of the email.

attachment: attachment file name to be sent in email (optional).


## How to integrate with Azure DevOps:
![image](https://user-images.githubusercontent.com/20087806/92676189-b1849700-f33e-11ea-9ce6-2fdb6ce0a80c.png)
