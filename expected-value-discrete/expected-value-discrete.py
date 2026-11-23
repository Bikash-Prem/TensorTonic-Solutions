import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    # Write code here
    x = np.asarray(x)
    p = np.asarray(p)
    ex = 0.0
    for i in range(len(x)):
        ex += x[i] * p[i]
    return ex