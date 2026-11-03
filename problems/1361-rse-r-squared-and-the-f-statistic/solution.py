import numpy as np
import math


def model_fit_stats(X: np.ndarray, y: np.ndarray) -> tuple:
    """Residual standard error, R-squared and the overall F-statistic.

    Args:
        X (np.ndarray): (n, p) design matrix without an intercept column.
        y (np.ndarray): (n,) target.

    Returns:
        tuple: (rse, r2, f_stat) as floats. RSS == 0 gives (0.0, 1.0, inf).
    """
    p = X.shape[1]
    n = X.shape[0]
    I = np.ones((n, 1)) 
    D = np.hstack([I, X])
    # print(D)
    w = np.linalg.inv((D.T @ D)) @ (D.T @ y)
    # print(w)
    y_pred = D @ w 
    # print(y_pred)
    TSS = np.sum((y - np.mean(y))**2)
    RSS = np.sum((y_pred - y)**2)


    RSE = math.sqrt(RSS / ( n - p - 1))
    R_2 = 1 - (RSS/TSS)
    if RSS == 0:
        return (0.0,1.0,float('inf'))
    else:
        F_stat = ((TSS - RSS)/p) / (RSS / (n - p - 1))
        return (RSE, R_2, F_stat)
    # print(w)
    # return w
    
