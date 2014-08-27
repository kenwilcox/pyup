import os

# Configuration
timeout = 30
url = "http://www.google.com"
sleep = 10

msg = "Site Down: " + url
subject = "Site Down"
msgto = os.environ.get('PYUP_TO')
msgfrom = os.environ.get('PYUP_FROM')
smtp = os.environ.get('PYUP_SMTP')