n = int(input())
M = [[0 for col in range(n)] for row in range(n)]
for i in range(n):
	M[i] = input().split()

for i in range(n):
	for j in range(n):
		print (M[i][j])

rou = 0
lvd = 1
lvr = 1
lv = int(M[0][0])
i = 0
j = 0

while (i == 0 and j == 0):
	rou = 10**rou 
	d = int(M[i+1][j])
	r = int(M[i][j+1])
	lvd = lv * d
	lvr = lv * r
	print (rou)

	if (lvr/rou) % 10 == 0 and (lvd/rou) % 10 != 0:
		i += 1
		lv = lvd
	elif (lvd/rou) % 10 == 0 and (lvr/rou) % 10 != 0:
		j += 1
		lv = lvr
	else:
		print ('in the else loop %d' % i)
		rou += 1
	if i == n-1 and j == n-1:
		print ('break')
		break

print (rou)
