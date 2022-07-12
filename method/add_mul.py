def add_mul(choice, *args):
	if choice == "add":
		result = 0
		for i in args:
			result += i
	elif choice == "mul":
		result = 1
		for i in args:
			result *= i
	return result
	
a = 10
b = 20
print(add_mul('add', a, b, 50))
print(add_mul('mul', a, b, 50))

