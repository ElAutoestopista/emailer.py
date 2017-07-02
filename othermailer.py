#!/usr/bin/env python3
# coding: UTF-8
'''
    othermailer.py - Just another simple script to send emails via TLS
    Sergio Fernandez <sergio@fenandezcordero.net>
    Usage: python3 othermailer.py --help
'''

import sys
import smtplib
import argparse
import socket
import datetime
from random import choice
from string import ascii_lowercase, digits

# Configure your sender settings
config = {
    'USER': "user@domain",
    'PASS': "password",
    'HOST': "mail.host.name",
    'PORT': "587"
}

# Parse arguments about receiver
PARSER = argparse.ArgumentParser()
PARSER.add_argument("-s", "--subject", help="Mail subject", type=str)
PARSER.add_argument("-t", "--to", help="Destination emails, separated by comma", type=str)
PARSER.add_argument("-b", "--body", help="Message body", type=str)
ARGS = PARSER.parse_args()

# Headers values. In most cases, default values are ok for text-only content
MIME_VER = "1.0"
CONTENT_TYPE = "text/plain"
CHARSET = "UTF-8"
MAILER_ID = "Othermailer.py - https://github.com/ElAutoestopista/othermailer.py"
DATE_STR = datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S %z")

# It's considered a good practice that MUA generates a message ID, so we are going to generate one randomly.
HOSTNAME = socket.getfqdn()
RAND_STR = ''.join(choice(ascii_lowercase + digits) for i in range(20))
Message_Id = "<"+RAND_STR+"@"+HOSTNAME+">"

# Check arguments
if ARGS.subject:
    Subject = ARGS.subject
else:
    print("No subject defined")
    sys.exit(1)
if ARGS.body:
    Msg = ARGS.body
else:
    print("No message defined")
    sys.exit(1)
if ARGS.to:
    To = [x.strip() for x in ARGS.to.split(',')]
else:
    print("No destination defined")
    sys.exit(1)

# Build message headers
Message = """\
From: %s
To: %s
Subject: %s
Message-ID: %s
X-Mailer: %s
MIME-Version: %s
Content-Type: %s; CHARSET="%s"
Date: %s

%s
""" % (config.get('USER'), ','.join(To), Subject, Message_Id, MAILER_ID, MIME_VER, CONTENT_TYPE, CHARSET, DATE_STR, Msg)

# Connect and try to send
try:
    Othermailer = smtplib.SMTP(config.get('HOST'), config.get('PORT'))
    Othermailer.ehlo()
    Othermailer.starttls()
    Othermailer.login(config.get('USER'), config.get('PASS'))
    Othermailer.sendmail(config.get('USER'), To, Message)
    print("Sent")
except smtplib.SMTPException as Error:
    print("ERROR: " + Error)
