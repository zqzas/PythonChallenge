#brute force:
#by zqzas
import string

t = open('equality.txt', 'r').read().strip().split('\n')

def inboard(pos, lmt):
	if pos >= 0 and pos < lmt:
		return True
	return False
	
ans = []
print len(t)
for i in xrange(len(t)):
	for j in xrange(len(t[i])):
		x = t[i][j]
		if x in string.uppercase:
			continue
		cnt = [0,0,0]
		for dy in xrange(-3, 0):
				for st in [1, -1]:
					if inboard(j + dy * st, len(t[i])):
						if t[i][j + dy * st] in string.uppercase:
							cnt[st + 1] += 1
		flag = 0
		for st in [1, -1]:
			if inboard(j + 4 *st, len(t[i])) and t[i][j + 4 * st] in string.uppercase:
				flag = 1
		if (not flag) and cnt[0] == 3 and cnt[2] == 3:
			print t[i][j-3:j+4]
			ans.append(t[i][j])
			
print ''.join(ans)
