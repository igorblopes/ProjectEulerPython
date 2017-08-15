def isPrime(number):
	stats = True
	if number % 2 == 0 and number > 2:
		stats = False
	else:
		for i in range(3, number):
			if number % i == 0:
				stats = False
	return stats

def calcLargestPrimeFactor(number):
	largest = 0
	for i in range(2, number):
		if number == i or number == 1:
			break
		while number % i == 0:
			number //= i
			largest = number
			
	print(largest)

calcLargestPrimeFactor(600851475143)


