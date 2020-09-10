################################################################
##################### email details ############################
################################################################

import argparse
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



parser = argparse.ArgumentParser()
parser.add_argument('--fromid', help="from-emailid", type= str)
parser.add_argument('--toid', help="to-emailid, use coma to delimit multile email id", type= str)
parser.add_argument('--ccid', help="email id in cc, use coma to delimit email id", type=str, default=" ")
parser.add_argument('--subject', help="subject of email", type=str, default="subject missing")
parser.add_argument('--body', help="body of email", type=str, default="email body missing")
parser.add_argument('--attachment', help="attachment in email", type=str, default="")

args = parser.parse_args()

#if "/" in args.body:
# email_body = open(args.body,"r")
#else:
# email_body = args.body

#try:
# email_body = open(args.body,"r")
#except IOError:
# print("file not found: %s" % args.body)


'''
below function is for sending email alert, to add new ids in alert use comma to seperate ids
'''

def add_attachment(attachments=""):
     attach_file_name = os.path.basename(attachments)
     attach_file = open(attachments, 'rb') # Open the file as binary mode
     payload = MIMEBase('application', 'zip')
     payload.set_payload(attach_file.read())
     attach_file.close()
     encoders.encode_base64(payload) #encode the attachment
     payload.add_header('Content-Decomposition', 'attachment', filename = (attach_file_name ))
     return payload

def sendEmail( fromId, toId, ccId, subject,email_body,attachment="" ):
     msg = MIMEMultipart()
     msg["Subject"] = subject
     msg["From"] = fromId
     msg["To"] = toId
     msg["Cc"] = ccId
     msg.attach(MIMEText(email_body,'html'))
     #### attachment block ####
     if attachment:
       msg.attach(add_attachment(attachment))
     ##########################
     s = smtplib.SMTP("<SMTP_IP>", <SMTP_PORT>)
     s.sendmail(msg["From"], msg["To"].split(",") + msg["Cc"].split(","), msg.as_string())



sendEmail(args.fromid,args.toid,args.ccid,args.subject,args.body,args.attachment)
