alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
value = {}
for i in range(0,len(alpha)):
	value[alpha[i]] = i + 1
for i in range(raw_input()):
	text = input()
	if text[1].isdigit() and 'R' in text and 'C' in text:
		index = text.index('C')
		x, c = '', int(text[index + 1:])
		while c != 0:
			c -= 1
			x = alpha[c % 26] + x
			c = c // 26
		print(x + text[1:index])
	else :
		i, c = 0, 0
		while text[i].isalpha():
			c = c * 26 + value[text[i]]
			i += 1
		print('R' + text[i:] + 'C' + str(c))