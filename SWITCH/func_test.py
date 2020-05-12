import numpy as np
from cost import cost
from calcthd import calcthd
from correction import correction

# ! TESTS
def test_function():
    # * correction.py testing
    vec1 = np.array([1, 2, 1, 1, 3, 4, 5, 1, 1, 10])
    vec2 = np.array([1, 2, 3, 4, 6, 4, 8, 9, 12, 10])
    a = correction(vec1, vec2)
    print(a)

test_function()