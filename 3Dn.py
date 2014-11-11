from heapq import *
a, h = 0, []
t, s = 0, []
for i, item in enumerate(raw_input()):
	if item == '?':
		item = ')'
		x, y = map(int, raw_input().split())
		heappush(h, [x-y, i])
		a += y
	s.append(item)
	if item == '(':
		t += 1

	else:
		if t == 0:
			if not h:
				t = -1
				break
			t = 1
			x, y = heappop(h)
			a += x
			s[y] = '('
		else: t -= 1


if t:
	print -1
else :
	print a
	print ''.join(s)



		