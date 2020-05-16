import numpy as np
from sumthd import sumthd
from calcthd import calcthd
from cost import costfunction
path = 'C:/interphase-switch-algorithm/SWITCH/samples/'
# ! TESTS
# ! Sumthd testing
def test_sumthd():
    # Данные
    V = np.loadtxt(path + 'V.txt')
    Izm = np.loadtxt(path + 'Izm.txt')
    kodV = np.loadtxt(path + 'kV.txt')
    Rd = np.loadtxt(path + 'Rd.txt')
    # Вызов
    sumof_values, thd_percent, numof_switching, wf_sumout = sumthd( kodV,
                                                                    V,
                                                                    6,
                                                                    Izm,
                                                                    Rd)
    # Вывод
    print('Start_sum:\n', sumof_values,
    '\nStart_THD:\n', thd_percent,
    '\nStartKPOP:\n', numof_switching,
    '\nStartSumOSC:\n', wf_sumout)

# ! Calcthd testing
def test_calcthd():
    # Данные
    Izm = np.loadtxt(path + 'Izm.txt')
    # Вызов
    cvof_elec, thd_percent, am = calcthd(Izm)
    # Вывод
    print(  'cvof_elec:\n', cvof_elec,
            '\nthd_percent:\n', thd_percent,
            '\nam:\n', am)

# ! Costfunction testing
def test_cost():
    


test_sumthd()
#test_calcthd()