import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    A = np.asarray(A)
    out = np.empty((A.shape[1], A.shape[0]), dtype=A.dtype)
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            out[j,i] = A[i,j]
    return out