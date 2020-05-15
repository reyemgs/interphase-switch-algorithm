import numpy as np
from calcthd import calcthd

# ! Calc_sum_thd.m
def sumthd(
        vec_x,        # * Vx
        v_struct,     # * V
        numof_value,  # * noV
        wf_vector,    # * Izm
        #dec_vector,   # * Rd
        #wf_sum,      # * Osc_sum
        calcthd       # ? calcthd.py
):
    #dec_vector = np.array([])
    dec_vector = = np.loadtxt('C:/interphase-switch-algorithm/SWITCH/samples/Rd.txt')
    sumof_values = [0, 0, 0]    #*S
    wf_sum = np.zeros((3,104))  #*Osc_sum
    numof_switching = 0         #*perecl
    g = 1                       #*G

    for i in range(1, numof_value, 2):
        a = i - 1
        if vec_x[a] == 1:
            if vec_x[i] == 0:
                dec_vector[g] = 3
                wf_sum[2,:] = wf_sum[2,:] + wf_vector[v_struct[1,g],:]

        else:
            if vec_x[i] == 1:
                dec_vector[g] = 2
                wf_sum[1,:] = wf_sum[1,:] + wf_vector[v_struct[1,g],:]

            else:
                dec_vector[g] = 1
                wf_sum[0,:] = wf_sum[0,:] + wf_vector[v_struct[1,g],:]

        if dec_vector[g] != v_struct[3,g]:
            numof_switching += 1

        g += 1
    thd_percent = [0, 0, 0]
    sumof_values[1], thd_percent[1] = calcthd(wf_sum[0,:]) # * Вызов calcthd

    return sumof_values, thd_percent, numof_switching, wf_sum