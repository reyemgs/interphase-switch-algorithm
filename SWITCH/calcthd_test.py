import numpy as np
from calcthd import calcthd

thd_sum = np.zeros((2,3))
a, b, c = calcthd(thd_sum)

print(a, b, c)