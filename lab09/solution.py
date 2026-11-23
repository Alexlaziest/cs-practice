import numpy as np

def make_hours():
    return np.arange(0,22,3).tolist()


def vector_report(values):
    ar=np.asarray(values)
    return {
    "third": ar[2],
    "last": ar[-1],
    "middle": ar[2:6].tolist(),
    "every_second": ar[::2].tolist(),
    "reversed": ar[::-1].tolist()}

def change_vector(values):
    ar=np.asarray(values).copy()
    ar[2:5]=99
    ar[::2]=-1
    return ar.tolist