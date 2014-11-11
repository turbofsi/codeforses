w = [None] * 5001
h = [None] * 5001
to = [None] * 5001
d = [None] * 5001
def dp(v):
	
	if d[v]:
		return d[v]
	else:
		d[v] = 1
		for i in xrange(n+1):
			if w[i] > w[v] and h[i] > h[v]:
				if dp(i) + 1 > d[v]:
					to[v] = i
					d[v] = d[i] + 1
		return d[v]

n, w[0], h[0] = map(int, raw_input().split())
to[0] = -1
for i in xrange(1, n + 1):
	to[i] = -1
	w[i], h[i] = map(int, raw_input().split())
dp(0)

print (d[0]-1)
i = to[0]
out = []
while i != -1:
	out.append(str(i))
	i = to[i]
print ' '.join(out)
	