n = int(raw_input())
dic = {}
out = []
for i in xrange(n):
	temp = raw_input()
	if temp not in dic:
		dic[temp] = 0
		out.append('OK')
	else :
		dic[temp] += 1
		o = temp + str(dic[temp])
		out.append(o)
for i in xrange(len(out)):
	print out[i]