#level 4
#by zqzas

import re, urllib

pattern = "and the next nothing is ([0-9]+)"

index = '12345'

for i in xrange(400):
	print index
	html = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" % index).read()
	try:
		index = re.findall(pattern, html)[0]
	except:
		print html
		break



