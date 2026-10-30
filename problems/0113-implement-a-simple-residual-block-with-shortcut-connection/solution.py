import numpy as np

def residual_block(x: np.ndarray, w1: np.ndarray, w2: np.ndarray) -> np.ndarray:
	# Your code here
	l1 = w1 @ x
	l1[l1 < 0] = 0
	l2 = w2 @ l1
	o = l2 + x
	o[o < 0] = 0
	return o