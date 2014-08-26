#!/usr/bin/env python

import urllib2
import os.path
import time
import config

def check_config():
	ret = True
	missing = "Nothing"
	conf = dir(config)
	if not 'sleep' in conf:
		ret = False
		missing = 'sleep'
	if not 'url' in conf:
		ret = False
		missing = 'url'
	if not 'timeout' in conf:
		ret = False
		missing = 'timeout'
	return ret, missing

def main():
	while(not os.path.isfile('./die')):
		print "still running..."
		response = urllib2.urlopen(config.url, None, config.timeout)
		#print dir(response)
		print response.code, response.info()
		time.sleep(config.sleep)
		#

if __name__ == "__main__":
	(check, missing) = check_config()
	if check:
		main()
		os.remove('./die')
	else:
		print "Something was missing from your configuration!", missing