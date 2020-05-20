import math
import numpy as np
np.seterr(divide='ignore', invalid='ignore')

# ! Calc_DznI_THD.m
def calcthd(wf_sum):
    n = len(wf_sum)                                  # * N
    wf = np.reshape(wf_sum, (np.size(wf_sum), 1))    # * Osc
    #wf = wf_sum.T

    cvof_elec = math.sqrt(sum((wf_sum**2) * 0.02 / (n - 1)) / 0.02) # * TrueRMSI

    # s = np.zeros((n, 11))
    # c = np.zeros((n, 11))
    a = np.zeros((11, 1))
    b = np.zeros((11, 1))
    am = np.zeros((11, 1))

    # for i in range(0, n):
    #     for k in range(0, 11):
    #         s[i,k] = np.sin((2 * np.pi * i * k) / n)
    #         c[i,k] = np.cos((2 * np.pi * i * k) / n)
    #         #j += 1
    s = np.loadtxt('C:/interphase-switch-algorithm/SWITCH/samples/S.txt')
    c = np.loadtxt('C:/interphase-switch-algorithm/SWITCH/samples/C.txt')
    for k in range(0, 11):
        a[k] = (2 / n) * sum(wf[:,0] * s[:,k])
        b[k] = (2 / n) * sum(wf[:,0] * c[:,k])
        am[k] = math.sqrt(a[k] ** 2 + b[k] ** 2) / math.sqrt(2)
        #k += 1

    sq = math.sqrt(sum(am[1:] ** 2))
    # print('sq: ', sq)
    #print('am[0]: ', am[0])
    thd_percent = 100 * sq / am[0]                   # * THD_sum_I

    return cvof_elec, thd_percent , am