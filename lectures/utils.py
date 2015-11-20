print('lecture7')

def prime(n):
	if n == 1:
		return False
	for i in range(2, n):
		if n % i == 0:
			return False
	return True

print(__name__)

if __name__ == "__main__":
	def euclid(a,b):
		if b == 0:
			return a
		return euclid(b, a % b)

#print('Some text')
