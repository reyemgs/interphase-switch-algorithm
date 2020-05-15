import numpy as np
from sumthd import sumthd
from calcthd import calcthd

# ! TESTS
# ! Sumthd testing
def test_sumthd():
    path = 'C:/interphase-switch-algorithm/SWITCH/samples/'
    V = np.loadtxt(path + 'v_struct.txt')
    Izm = np.loadtxt(path + 'wf_best.txt')
    kodV = np.loadtxt(path + 'kV.txt')
    Rd = np.loadtxt(path + 'Rd.txt')
    sumof_values, thd_percent, numof_switching, wf_sumout = sumthd( kodV, V, 6, Izm, Rd, calcthd)
    print('Start_sum:\n', sumof_values,
    '\nStart_THD:\n', thd_percent,
    '\nStartKPOP:\n', numof_switching,
    '\nStartSumOSC:\n', wf_sumout)

# ! Calcthd testing
def test_calcthd():
    path = 'C:/interphase-switch-algorithm/SWITCH/samples/'
    Izm = np.loadtxt(path + 'wf_best.txt')
    cvof_elec, thd_percent, am = calcthd(Izm)
    print(  'cvof_elec:\n', cvof_elec,
            '\nthd_percent:\n', thd_percent,
            '\nam:\n', am)

test_sumthd()
#test_calcthd()