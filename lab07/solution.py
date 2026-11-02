import numpy as np

def reshape_rows(values, width):
    if len(values)%width != 0:
        return []
    a = np.array(values, dtype=float)
    return a.reshape(-1, width).tolist()

def block(matrix, rows, columns):
    if len(matrix) == 0:
        return []
    a = np.array(matrix, dtype=float)
    return a[np.ix_(rows, columns)].tolist()


def column_means(matrix):
    if len(matrix) == 0:
        return []
    a = np.array(matrix, dtype=float)
    return np.round(a.mean(axis=0), 6).tolist()

def column_range(matrix, column):
    if len(matrix) == 0:
        return 0.0
    a = np.array(matrix, dtype=float)
    b= a[:, column]
    return float(np.round((b.max() - b.min()), 6))


