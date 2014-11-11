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

for i in range(n):
    if name[i] in dic:
        dic1[name[i]] += score[i]
    else:
        dic1[name[i]] = score[i]
    if dic1[name[i]] == smax:
        print (name[i])
