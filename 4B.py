from heapq import *
d, s = map(int, raw_input().split())
mem = []
for i in xrange(d):
	temp = list(map(int, raw_input().split()))
	mem.append(temp)
sk = []
s1 = 0
s2 = 0
h = []
for i in xrange(len(mem)):
	s1 += mem[i][0]
	s2 += mem[i][1]
out = ''
if s >= s1 and s <= s2:
	print 'YES'
	for i, c in enumerate(mem):
		sk.append(c[0])
		s -= c[0]
		heappush(h, [c[1] - c[0], i])
	if s:
		while s:
			x, y = heappop(h)
			if x >= s:
				sk[y] += s
				s = 0
				break
			else :
				s -= x
				sk[y] += x
		for i in xrange(len(sk)):
			out += str(sk[i])
		print ' '.join(out)
					
	else :
		for i in xrange(len(sk)):
			out += str(sk[i])
		print ' '.join(out)
else :
	print 'NO'


