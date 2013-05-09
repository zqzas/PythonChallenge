#Python Challenge Prob 1
#Sulution by zqzas
#5.9.2013

import string

s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"

url = 'ocr'

trans = string.maketrans(string.lowercase, string.lowercase[2:] + 'ab')

print string.translate(s, trans)
print string.translate(url, trans)


