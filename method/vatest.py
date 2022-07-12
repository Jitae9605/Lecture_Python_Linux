a = 1
def vartest(a):
	a = a + 1
	return a
	
# 전역변수임을 기억 
vartest(a)
print(a)

a = vartest(a)
print(a)
