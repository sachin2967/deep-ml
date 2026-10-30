import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	arr = np.array(matrix)
	if mode == 'column':
		return list(np.mean(arr, axis = 0))
	else:
		return list(np.mean(arr, axis = 1))