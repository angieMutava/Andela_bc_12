def prime_generator(number):
	result = []
	if number < 0:
		return "Negative numbers not allowed."

	for i in range(0, number):
		if i < 2:
			return result
		elif i == 2:
			return result.append(i)
		elif i > 2:
			if i % number == 0:
				return result
			return result.append(i)

print prime_generator(10)
