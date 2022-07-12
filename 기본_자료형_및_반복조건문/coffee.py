coffee = 10
while True:
	money = int(input("Coin Insert: "))
	if money == 300:
		print("Coffee")
		coffee -= 1
	elif money > 300:
		print("Coffee And Return Change %d Won" %(money - 300))
		coffee -= 1
	else:
		print("Giveme more money. Take back")
		print("Coffee Stock : %d" % coffee)
	if coffee == 0:
		print("Out of Coffee. Close Store")
		break 
