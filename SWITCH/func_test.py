import numpy as np
from cost import costfunction
from calcthd import calcthd
from correction import correction

# ! TESTS
def test_function():
    vec1 = np.array([1, 2, 1, 1, 3, 4, 5, 1, 1, 10])
    #vec1 = np.array([[1, 2, 1, 1, 3, 4, 5, 1, 1, 10],
                     #[1, 2, 1, 1, 3, 4, 5, 1, 1, 10]])
    #vec2 = np.array([1, 2, 3, 4, 6, 4, 8, 9, 12, 10])
    
    # * correction.py testing
    # a = correction(vec1, vec2)
    # print(a)
    
    # * calcthd.py testing
    # print(np.reshape(vec2[0:], (10, 1)))
    # print(vec2[3])
    a, b, c = calcthd(vec1)
    print(a, b, c)


test_function() 