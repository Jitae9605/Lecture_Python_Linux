a = [1,2,3,4]

#  리스트내포
result = []
for num in  a:
	result.append(num * 3)
print(result)

# 리스트내포 2
result = []
result = [num * 3 for num in a]
print(result)

# 리스트내포 3
result = []
result = [num * 3 for num in a if num % 2 == 0]
print(result)
