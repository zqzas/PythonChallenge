#one liner ^_^
#by zqzas

import urllib, re

print re.findall('(?<![A-Z])[A-Z]{3}([a-z])[A-Z]{3}(?![A-Z])', urllib.urlopen('http://www.pythonchallenge.com/pc/def/equality.html').read())

