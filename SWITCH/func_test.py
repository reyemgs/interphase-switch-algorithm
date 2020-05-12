import numpy as np
from calcthd import calcthd
from correction import correction
vec1 = np.array([1, 1, 1, 4, 5, 6, 7, 8, 1, 10])
vec2 = np.array([1, 2, 1, 4, 5, 1, 7, 1, 9, 1])
# thd_sum = np.zeros(11)
# a, b, c = calcthd(thd_sum)
# print(a, b, c)

a = correction(vec1, vec2)
print(a)
