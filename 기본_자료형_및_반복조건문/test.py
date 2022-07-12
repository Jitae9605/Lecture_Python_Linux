a = "Life is too short"
c = 0
while a.find('o') != -1:
	b = a.find('o')
	a = a[a.find('o')-1:]
	c += b
	print(c)

