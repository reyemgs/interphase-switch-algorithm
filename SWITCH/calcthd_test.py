import numpy as np
from calcthd import calcthd

thd_sum = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
a, b, c = calcthd(thd_sum)

print(a, b, c)