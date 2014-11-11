n = int(input())
name = [None] * n
score = [None] * n

dic = {}
dic1 = {}

for i in range(n):
    name[i], sc = input().split()
    score[i] = float(sc)
    if name[i] in dic:
        dic[name[i]] += score[i]
    else:
        dic[name[i]] = score[i]

smax = max(dic.values())

for j in range(n):
    if name[j] in dic1:
        dic1[name[j]] += score[j]
    else:
        dic1[name[j]] = score[j]
    if dic1[name[j]] >= smax and dic[name[j]] == smax:
    	print (name[j])
    	break