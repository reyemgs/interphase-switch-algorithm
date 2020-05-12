import numpy as np
from calcthd import calcthd

#thd_sum = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
thd_sum = np.zeros(11)
a, b, c = calcthd(thd_sum)

print(a, b, c)

s = [ [1]
      [2]   
      [3] ]