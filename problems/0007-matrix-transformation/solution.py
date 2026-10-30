import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	A = np.array(A); T = np.array(T); S = np.array(S)
	#first i have to check if matrix are square or not
	if A.shape[0] == A.shape[1] == T.shape[0] == T.shape[1] == S.shape[0] == S.shape[1] and np.linalg.det(T) != 0 and np.linalg.det(S) != 0:
		ans = np.linalg.inv(T) @ A @ S
		return list(ans)
	else:
		return -1