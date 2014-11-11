a = list(raw_input())
b = filter(lambda x: x != '?', a)
nq = len(a) - len(b)
mem = []
for i in xrange(nq):
	temp = list(map(int, raw_input().split()))
	mem.append(temp)

def detect(m):
	c = 0
	for i in xrange(len(m)):
		if m[i] == '(':
			c += 1
		elif c == 0 :
			return False
		else :
			c -= 1
	if c == 0:
		return True
	else :
		return False

def measure(m):
	c = 0
	for i in xrange(len(m)):
		if m[i] == '(':
			c += 1
		elif m[i] == ')' :
			c -= 1
		else:
			pass
	return c

v = len(a) - len(b)
vx = -measure(a)

nn = (v - vx) / 2
np = (v + vx) / 2

print mem


