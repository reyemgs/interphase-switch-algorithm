import numpy as np
from cost import costfunction
from calcthd import calcthd
from correction import correction

# ! TESTS
def test_function():
    vec1 = np.array([1, 2, 1, 1, 3, 4, 5, 1, 1, 10, 11])
    #vec2 = np.array([1, 2, 3, 4, 6, 4, 8, 9, 12, 10])
    
    # * correction.py testing
    # a = correction(vec1, vec2)
    # print(a)
    
    # * calcthd.py testing
    cvof_elec, thd_percent, am = calcthd(vec1)
    print('cvof_elec:\n', cvof_elec, 
        '\nthd_percent:\n', thd_percent, 
        '\nam:\n', am)

test_function() 