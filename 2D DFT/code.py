import numpy as np

f = np.array([
    [26, 20, 89, 123],
    [34, 23, 92, 128],
    [32, 19, 62, 121],
    [38, 19, 34, 25]
])

F = np.fft.fft2(f)

np.set_printoptions(precision=2, suppress=True)

print(F)
