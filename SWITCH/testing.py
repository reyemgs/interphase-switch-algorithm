import numpy as np
import matplotlib.pyplot as plt
from calcfitness import calcfitness
from sumthd import sumthd
from calcthd import calcthd
from cost import costfunction
from binbatalg import bba
from my_cost import my_cost

# * Данные
path = 'C:/interphase-switch-algorithm/SWITCH/samples/'
kodV = np.loadtxt(path + 'kV.txt')
V = np.loadtxt(path + 'V.txt')
Izm = np.loadtxt(path + 'Izm.txt')
Rd = np.loadtxt(path + 'Rd.txt')
StartSum = np.loadtxt(path + 'StartSum.txt')
StartTHD = np.loadtxt(path + 'StartTHD.txt')
Max_iteration = 30
noP = 25
noV = 6
A = .25
r = .1


# ! Sumthd testing
def test_sumthd():
    #Вызов
    (sumof_values, thd_percent,
    numof_switching, dec_vector, wf_sumout) = sumthd(kodV, V, 6, Izm,Rd)
    # Вывод
    print(  'Start_sum:\n', sumof_values,
            '\nStart_THD:\n', thd_percent,
            '\nStartKPOP:\n', numof_switching,
            '\nRd:\n', dec_vector,
            '\nStartSumOSC:\n', wf_sumout)


# ! Calcthd testing
def test_calcthd():
    # Вызов
    cvof_elec, thd_percent, am = calcthd(Izm)
    # Вывод
    print(  'cvof_elec:\n', cvof_elec,
            '\nthd_percent:\n', thd_percent,
            '\nam:\n', am)


# ! Calcfitness testing
def test_calcfitness():
    # Вызов
    o, f1, f2 = calcfitness(StartSum, StartTHD, 0, 3)
    # Вывод
    print(  'F1: ', f1,
            '\nF2: ', f2,
            #'\nF3: ', f3,
            '\no: ', o)


# ! Costfunction testing
def test_costfunction():
    # Вызов
    o = costfunction(kodV, kodV, 55, 6, V, Izm, Rd)#, StartSum, StartTHD, 0)
    # Вывод
    print(o)


# ! Binbatalg testing
def test_bba():
    # Вызов
    fmin, best, cg_curve = bba(noP, A, r, noV, Max_iteration, kodV,
                                kodV, 6, V, Izm, Rd)
    # Вывод
    print(fmin, best)
    plt.plot(cg_curve)
    plt.show()

test_sumthd()
# test_calcthd()
#test_calcfitness()
#test_costfunction()
#test_bba()