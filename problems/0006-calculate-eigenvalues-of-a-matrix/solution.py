import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	arr = np.array(matrix)
	return list(np.linalg.eig(arr)[0])
	