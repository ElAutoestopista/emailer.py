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
from string import ascii_lowercase,digits

# Configure your sender settings
config = {
    'USER': "user@domain",
    'PASS': "password",
    'HOST': "mail.host.name",
    'PORT': "587"
}

# Parse arguments about receiver
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--subject", help="Mail subject", type=str)
parser.add_argument("-t", "--to", help="Destination email(s)", type=str)
parser.add_argument("-b", "--body", help="Message body", type=str)
args = parser.parse_args()

# Headers values. In most cases, default values are ok for text-only content
mime_ver = "1.0"
content_type = "text/plain"
charset = "UTF-8"
mailer_id = "Othermailer.py - https://github.com/ElAutoestopista/othermailer.py"
date_str = datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S %z")

# It's considered a good practice that MUA generates a message ID, so we are going to generate one randomly.
hostname = socket.getfqdn()
rand_str = ''.join(choice(ascii_lowercase + digits) for i in range(20))
message_id = "<"+rand_str+"@"+hostname+">"

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
Message-ID: %s
X-Mailer: %s
MIME-Version: %s
Content-Type: %s; charset="%s"
Date: %s

%s
""" % (config.get('USER'), to, subject, message_id, mailer_id, mime_ver, content_type, charset, date_str, msg)

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
