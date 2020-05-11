import math
import numpy as np

            #Osc_sum
def calcthd(wf_sum):
    n = len(wf_sum) 
    wf = np.arange(1, n).reshape(n - 1, -1)

    
    cvof_elec = math.sqrt(sum((wf_sum**2) * 0.02 / (n - 1)) / 0.02)

    s = np.zeros((n, 11))
    c = np.zeros((n, 11))
    a = np.zeros(11)
    b = np.zeros(11)
    am = np.zeros(11)

    for i in range(0, n):
        for j in range(0, 11):
            s[i,j] = np.sin((2 * np.pi * i * k) / n)
            c[i,j] = np.cos((2 * np.pi * i * k) / n)
            j += 1

    for j in range(0, 11):
        a[j] = (2 / n) * sum(wf * s[:j])
        b[j] = (2 / n) * sum(wf * c[:j])
        am[j] = math.sqrt(a[j] ** 2 + b[j] ** 2) / math.sqrt(2)


    sq = math.sqrt(sum(am[1:] ** 2))
    thd_percent = 100 * sq / am[1]

    return cvof_elec, thd_percent, am