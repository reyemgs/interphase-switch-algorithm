import math
import numpy as np
# ! Calc_DznI_THD.m

def calcthd(wf_sum): # * OscS  
    n = len(wf_sum)  # * N
    wf = np.reshape(wf_sum[0:], (n, 1))  # * Osc
    
    cvof_elec = math.sqrt(sum((wf_sum**2) * 0.02 / (n - 1)) / 0.02) # * TrueRMSI
    
    s = np.zeros((n, 11))
    c = np.zeros((n, 11))
    a = np.zeros(11)
    b = np.zeros(11)
    am = np.zeros(11)

    for i in range(0, n):
        for j in range(0, 11):
            s[i,j] = np.sin((2 * np.pi * i * j) / n)
            c[i,j] = np.cos((2 * np.pi * i * j) / n)
            j += 1

    for k in range(0, 11):
        a[k] = (2 / n) * sum(wf[:,0] * s[:,k])
        b[k] = (2 / n) * sum(wf[:,0] * c[:,k])
        #a[k] = (2 / n) * sum(np.dot(wf[:,0], s[:,k]))
        #b[k] = (2 / n) * sum(np.dot(wf[:,0], c[:,k]))
        am[k] = math.sqrt(a[k] ** 2 + b[k] ** 2) / math.sqrt(2)
        k += 1

    sq = math.sqrt(sum(am[1:] ** 2))
    thd_percent = 100 * sq / am[1]

    # TODO TESTING
    # print('WF_NOT_TRANSPOSE: ',wf_sum)
    #print('WF_TRANSPOSE:\n ',wf)
    #('Cvoc_elec: ', cvof_elec)
    # print('\nWF: ',np.size(wf))
    # print('\nS: ', np.size(s)) 
    # print('\nC: ', np.size(c)) 

    return cvof_elec, thd_percent, am