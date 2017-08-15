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


