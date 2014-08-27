#!/usr/bin/env python

import urllib2
import os.path
import time
import smtplib
from email.mime.text import MIMEText
import config

def check_config():
	ret = False
	missing = "Nothing"
	conf = dir(config)
	# This could be prettier
	if not 'sleep' in conf:
		missing = 'sleep'
	elif not 'url' in conf:
		missing = 'url'
	elif not 'timeout' in conf:
		missing = 'timeout'
	elif not 'msg' in conf:
		missing = 'msg'
	elif not 'subject' in conf:
		missing = 'subject'
	elif not 'msgto' in conf:
		missing = 'msgto'
	elif not 'msgfrom' in conf:
		missing = 'msgfrom'
	elif not 'smtp' in conf:
		missing = 'smtp'
	else:
		ret = True
	return ret, missing

def notify_user():
	msg = MIMEText(config.msg)
	msg['Subject'] = config.subject
	msg['From'] = config.msgfrom
	msg['To'] = config.msgto

	s = smtplib.SMTP(config.smtp)
	s.sendmail(config.msgfrom, [config.msgto], msg.as_string())
	s.quit()

def main():
	while(not os.path.isfile('./die')):
		print "still running..."
		response = urllib2.urlopen(config.url, None, config.timeout)
		#print dir(response)
		print response.code, response.info()
		if (not response.code == 200):
			notify_user()
		time.sleep(config.sleep)
		#

if __name__ == "__main__":
	(check, missing) = check_config()
	if check:
		main()
		os.remove('./die')
	else:
		print "Something was missing from your configuration!", missing