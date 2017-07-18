# othermailer.py
othermailer.py is a simple script to send emails via TLS, optimized for providers that gives much importance in security, as Gmail.
As yo can also attach a text file, it fits perfect as a complement for scripting, when you need fast email reports without configuring Postfix or Sendmail.

### HowTo

Edit othermailer.py script for sender configuration:
```python
config = {
    'USER': "user@example.com",
    'PASS': "p@Ssws0Rd",
    'HOST': "smtp.example.com",
    'PORT': "587"
}
```
Run othermailer.py --help for usage hints:
```
usage: othermailer.py [-h] [-s SUBJECT] [-t TO] [-b BODY] [-a ATTACH]

optional arguments:
  -h, --help            show this help message and exit
  -s SUBJECT, --subject SUBJECT
                        Mail subject
  -t TO, --to TO        Destination emails, separated by comma
  -b BODY, --body BODY  Message body
  -a ATTACH, --attach ATTACH
                        Text file to attach
```
### Options
- *-s, --subject* : Subject of the email, a string in double quotes
- *-t, --to* : Recipients of the messages, separated by commas
- *-b, --body* : Body of message, also a string in double quotes
- *-a, --attach* : Full path to a plain text file to be attached. Only plain text supported

## Sample command
Installed in `/usr/local/bin`, a common ussage could be:
```bash
/usr/local/bin/othermailer-py -t systems@example.com,backend@example.com -s "CRITICAL - Service DOWN" -b "There is a critical down. See attached report for futher info" -a /tmp/service.log
```