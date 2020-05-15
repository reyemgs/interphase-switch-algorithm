import numpy as np
from sumthd import sumthd
from calcthd import calcthd

# ! TESTS

# ! Sumthd testing
def test_sumthd():
    V = np.loadtxt('C:/interphase-switch-algorithm/SWITCH/samples/v_struct.txt')
    Izm = np.loadtxt('C:/interphase-switch-algorithm/SWITCH/samples/wf_best.txt')
    kodV = np.loadtxt('C:/interphase-switch-algorithm/SWITCH/samples/kV.txt')
    Rd = np.loadtxt('C:/interphase-switch-algorithm/SWITCH/samples/Rd.txt')

    sumof_values, thd_percent, numof_switching, wf_sumout = sumthd( kodV,
                                                                    V,
                                                                    6,
                                                                    Izm,
                                                                    Rd,
                                                                    calcthd)
    print('Start_sum:\n', sumof_values,
    '\nStart_THD:\n', thd_percent,
    '\nStartKPOP:\n', numof_switching,
    '\nStartSumOSC:\n', wf_sumout)

# ! Calcthd testing
def test_calcthd():
    Izm = np.loadtxt('C:/interphase-switch-algorithm/SWITCH/samples/wf_best.txt')
    cvof_elec, thd_percent, am = calcthd(Izm)
    print(  'cvof_elec:\n', cvof_elec,
            '\nthd_percent:\n', thd_percent,
            '\nam:\n', am)

#test_sumthd()
test_calcthd()













    # wf_sum = np.array([1, 2, 1, 1, 3, 4, 5, 1, 1, 10, 11])
    # wf_sum = np.arange(312).reshape((3, 104))
    # vec_x = np.linspace(0, 1, 312).reshape((3, 104))#np.zeros((3, 104))
    # vec_x = np.array([0, 0, 0, 1, 1, 0])
    # v_struct = np.zeros((3,104))
    # v_struct = np.array([[0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    #                     [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    #                     [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0]])
    #wf_vector = np.array([1, 2, 3, 4, 6, 4, 8, 9, 12, 10, 11])
    # dec_vector = np.array([1, 2, 3, 4, 6, 4, 8, 9, 12, 10, 11])