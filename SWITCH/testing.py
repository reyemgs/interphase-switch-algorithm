import numpy as np
from calcfitness import calcfitness
from sumthd import sumthd
from calcthd import calcthd
from cost import costfunction
path = 'C:/interphase-switch-algorithm/SWITCH/samples/'

kodV = np.loadtxt(path + 'kV.txt')
V = np.loadtxt(path + 'V.txt')
Izm = np.loadtxt(path + 'Izm.txt')
Rd = np.loadtxt(path + 'Rd.txt')
StartSum = np.loadtxt(path + 'StartSum.txt')
StartTHD = np.loadtxt(path + 'StartTHD.txt')

# ! Sumthd testing
def test_sumthd():
    #Вызов
    (sumof_values, thd_percent,
    numof_switching, wf_sumout) = sumthd(kodV, V, 6, Izm,Rd)
    # Вывод
    print(  'Start_sum:\n', sumof_values,
            '\nStart_THD:\n', thd_percent,
            '\nStartKPOP:\n', numof_switching,
            '\nStartSumOSC:\n', wf_sumout)


# ! Calcthd testing
def test_calcthd():
    # Вызов
    cvof_elec, thd_percent, am = calcthd(Izm)
    # Вывод
    print(  'cvof_elec:\n', cvof_elec,
            '\nthd_percent:\n', thd_percent,
            '\nam:\n', am)


# ! Costfunction testing
def test_calcfitness():
    # Вызов
    f1, f2, f3, o = calcfitness(StartSum, StartTHD, 0, 3)
    # Вывод
    print(  'F1: ', f1,
            '\nF2: ', f2,
            '\nF3: ', f3,
            '\no: ', o)



test_sumthd()
#test_calcthd()
#test_calcfitness()