import numpy as np
import matplotlib.pyplot as plt
from calcfitness import calcfitness
from sumthd import sumthd
from calcthd import calcthd
from cost import costfunction
from binbatalg import bba
from swalg import iswalg

# * Данные
path = 'C:/interphase-switch-algorithm/SWITCH/samples/'
kodV = np.loadtxt(path + 'kV.txt')
V = np.loadtxt(path + 'V.txt')
Rd = np.loadtxt(path + 'Rd.txt')
StartSum = np.loadtxt(path + 'StartSum.txt')
StartTHD = np.loadtxt(path + 'StartTHD.txt')

Izm = np.zeros((56, 104))
s = np.loadtxt(path + 'Izm.txt')
for i in range(0, 56):
        Izm[i,] = s[i,]

Max_iteration = 30
noP = 25
noV = 6
A = .25
r = .1


# ! Sumthd testing
def test_sumthd():
    #Вызов
    (sumof_values, thd_percent,
    numof_switching, dec_vector, wf_sumout) = sumthd(kodV, V, 6, Izm, Rd)
    # Вывод
    print(  'Start_sum:\n', sumof_values,
            '\nStart_THD:\n', thd_percent,
            '\nStartKPOP:\n', numof_switching,
            '\nRd:\n', dec_vector,
            '\nStartSumOSC:\n', wf_sumout)


# ! Calcthd testing
def test_calcthd():
    # Вызов
    cvof_elec, thd_percent, am = calcthd(Izm[0,])
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
    o , pb= costfunction(kodV, kodV, 0.6, 6, V, Izm, Rd)#, StartSum, StartTHD, 0)
    # Вывод
    print(o, pb)


# ! Binbatalg testing
def test_bba():
    # Вызов
    fmin, best, cg_curve = bba(noP, A, r, noV, Max_iteration, kodV,
                                kodV, 6, V, Izm, Rd)
    # Вывод
    print(fmin, best)
    plt.plot(cg_curve)
    plt.show()

def test_iswalg():
    iswalg()


#test_sumthd()
#test_calcthd()
#test_calcfitness()
#test_costfunction()
#test_bba()
test_iswalg()