import numpy as np

def reshape_rows(values, width):
    if len(values)%width != 0:
        return []
    a = np.array(values)
    return a.reshape(-1, width).tolist()

def block(matrix, rows, columns):
    a = np.array(matrix)
    return a[np.ix_(rows, columns)].tolist()







# print(block([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [0, 2], [1, 2]))