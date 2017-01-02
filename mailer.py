#coding: UTF-8
'''
    mailer.py - Simple script to send emails via TLS
    Sergio Fernandez <sergio@fenandezcordero.net>
    Usage: python3 mailer.py --help
'''

import sys
import smtplib
import argparse

# Configure your sender settings
config = {
    'USER' : "user@domain",
    'PASS' : "password",
    'HOST' : "mail.host.name",
    'PORT' : "587"
}

# Parse arguments about receiver
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--subject", help="Mail subject", type=str)
parser.add_argument("-t", "--to", help="Destination email(s)", type=str)
parser.add_argument("-b", "--body", help="Message body", type=str)
args = parser.parse_args()

# Check arguments
if args.subject:
    subject = args.subject
else:
    print("No subject defined")
    sys.exit(1)
if args.body:
    msg = args.body
else:
    print("No message defined")
    sys.exit(1)
if args.to:
    to = args.to
else:
    print("No destination defined")
    sys.exit(1)

# Build message headers
message = """\
From: %s
To: %s
Subject: %s

%s
""" % (config.get('USER'), to, subject, msg)

# Connect and try to send
try:
    server = smtplib.SMTP(config.get('HOST'), config.get('PORT'))
    server.ehlo()
    server.starttls()
    server.login(config.get('USER'), config.get('PASS'))
    server.sendmail(config.get('USER'), to, message)
    print("Sent")
except smtplib.SMTPException as e:
    print("ERROR: " + e)
