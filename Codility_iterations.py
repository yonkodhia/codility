def solution(N):
	"""A code that will calculate the Binary Gap of a number N"""
	result = 0
	counter = 0

	bin_number = "{0:b}".format(N)

	for num in bin_number:
		if num == "1":
			if counter > result:
				result = counter
			counter = 0
		else:
			counter += 1

	return result;

if __name__ == '__main__':
	solution(246)

