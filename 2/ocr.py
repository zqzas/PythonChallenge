import string

f = open('chars.txt').read()
dic = {}
for x in f:
	dic[x] = 1
print dic

for x in f:
	if x in string.letters:
		print x
		
