from math import pi,sin,acos
xe1, ye1 = input().split()
xe2, ye2 = input().split()
xe3, ye3 = input().split()

x1, y1 = float(xe1), float(ye1)
x2, y2 = float(xe2), float(ye2)
x3, y3 = float(xe3), float(ye3)

mod = []
for i in range(3, 101):
    mod.append(2 * pi / i)	

def vecdis(x):
    return (x[0]**2 + x[1]**2)**0.5
    
def vecangle(x,y,z):
	alpha = acos(abs((x[0]**2 + x[1]**2 + y[0]**2 + y[1]**2 - (z[0]**2 + z[1]**2)) / (2 * (x[0]**2 + x[1]**2)**0.5 * (y[0]**2 + y[1]**2)**0.5)))
	return alpha

def f(x, y):
	for i in range(len(mod)):
		a1 = x / mod[i]
		a2 = y / mod[i]
		if abs(round(a1) - a1) < 0.01 or abs(round(a2) - a2) < 0.01:
			i += 3
			return i
			break
		else:
			continue
	

ca = [x1 - x3, y1 - y3]
cb = [x2 - x3, y2 - y3]
ab = [x2 - x1, y2 - y1]




alpha1 = 2 * vecangle(ca, cb, ab)
alpha2 = 2 * vecangle(ca, ab, cb)

N = f(alpha1, alpha2)
dis = vecdis(ab)
r = dis / (2 * sin(alpha1 / 2))
s = N * (0.5 * r**2 * sin(2*pi / N))

print (s)
