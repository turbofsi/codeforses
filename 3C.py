rx = []
cx = []
r0 = []
c0 = []

def detect(m):
	x=0
	y=0
	z=0
	for i in xrange(len(m)):
		if m[i] == 0 :
			x += 1
		if m[i] == 1 :
			y += 1
		if m[i] == 2:
			z += 1
	if x == 3 or y == 3 or z == 3:
		return True
	else:
		return False

def dig(m):
	if [0, 0] in m and [1, 1] in m and [2, 2] in m :
		return True
	elif [0, 2] in m and [1, 1] in m and [2, 0] in m :
		return True
	else:
		return False

for i in xrange(3):
	st = raw_input()
	for j in xrange(3):
		temp = st[j]
		if temp == 'X':
			rx.append(i)
			cx.append(j)
		elif temp == '0':
			r0.append(i)
			c0.append(j)
		else:
			pass
mx = []
m0 = []
for i in xrange(len(rx)):
	mx.append([rx[i], cx[i]])
for i in xrange(len(r0)):
	m0.append([r0[i], c0[i]])

countx = len(rx)
count0 = len(r0)
countd = 9 - (count0 + countx)
if countx - count0 == 0 or countx - count0 == 1:
	if (detect(rx) or detect(cx)) and (detect(r0) or detect(c0)):
		print "illegal"
	elif countx - count0 == 1 and (detect(r0) or detect(c0)):
		print "illegal"
	elif countx - count0 == 0 and (detect(rx) or detect(cx)):
		print "illegal"
	elif countx - count0 == 1 and dig(m0):
		print "illegal"
	elif countx - count0 == 0 and dig(mx):
		print "illegal"
	elif dig(mx):
		print "the first player won"
	elif dig(m0):
		print "the second player won"
	elif detect(rx) or detect(cx):
		print "the first player won"
	elif detect(r0) or detect(c0):
		print "the second player won"
	elif countd != 0 and countx - count0 == 1:
		print "second"
	elif countd != 0 and countx - count0 == 0:
		print "first"
	elif countd == 0:
		print "draw"
	else:
		print "illegal"

else:
	print "illegal"


