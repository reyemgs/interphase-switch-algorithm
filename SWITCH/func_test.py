import numpy as np
from correction import correction
from calcthd import calcthd
from sumthd import sumthd
from cost import costfunction




# ! TESTS
def test_function():
    #wf_sum = np.array([1, 2, 1, 1, 3, 4, 5, 1, 1, 10, 11])
    # vec_x = np.array([0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0])
    v_struct = np.array([[0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                         [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                         [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0]])
    wf_vector = np.array([1, 2, 3, 4, 6, 4, 8, 9, 12, 10, 11])
    dec_vector = np.array([1, 2, 3, 4, 6, 4, 8, 9, 12, 10, 11])
    vec_x = np.linspace(0, 1, 312).reshape((3, 104))#np.zeros((3, 104))
    wf_sum = np.arange(312).reshape((3, 104))

    
    # * correction.py testing
    # a = correction(vec1, vec2)
    # print(a)
    
    # * calcthd.py testing
    # cvof_elec, thd_percent, am = calcthd(vec1)
    # print('cvof_elec:\n', cvof_elec,
    #     '\nthd_percent:\n', thd_percent,
    #     '\nam:\n', am)
    
    # * sumthd.py testing
    sumof_values, thd_percent, numof_switching, dec_vector, wf_sumout = sumthd( vec_x, 
                                                                                v_struct,
                                                                                30, 
                                                                                wf_vector,
                                                                                dec_vector, 
                                                                                wf_sum, calcthd)


test_function() 