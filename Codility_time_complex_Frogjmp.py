import math
def solution (X = int, Y = int, D = int):
	""""A program that calculates the minimal number of jumps a frog takes to
	reach from point X to Y if he jumps a fixed distance D"""
	#specifications:
	#X, Y and D are integers within the range [1..1,000,000,000]; X ≤ Y.
	#algoritm:
	#restar Y de X para calcular la distancia total
	#dividir resultado / D y redondear para obtener la distancia en
	#caso límite, si X y Y son iguales, regresar 0
	#si la distancia * el número de saltos + distancia inicial < Y: sumar 1 a
	# distancia
	#return result
	if Y == X:
		return 0
	jumps = math.floor((Y-X) / D)
	if jumps * D + X < Y:
		jumps += 1
	return jumps

if __name__ == '__main__':
	print(solution (1,5,2))

#Analysis
#Detected time complexity: O(1)