def solution(A = list, K = int):
	"""A code that will rotate an array K times"""
	N = len(A)
	if N == 0:
		return A
	result = [0] * N
	reminder = K % N

	if K == N:
		result = A
		return result
	if K == 0:
		result = A
		return result

	for i in range (N):
		result[i] = A[i-reminder]
	print(result)
	return result;

if __name__ == '__main__':
	print(solution([-1, -10 , 10 ,2 ], 3))

