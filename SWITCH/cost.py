import numpy as np
from sumthd import sumthd
from calcfitness import calcfitness

# ! My_Cost.m
def costfunction(
        vec_x,                 # * kodV
        pbest_vector,          # * PreviousV
        pbest_value,           # * PreviousBest
        numof_value,           # * noV
        #convergence_curve,    # * MyConvergenceCurve
        #all_costs,            # * AllCosts
        V,                     # ! sumthd
        Izm,                   # ! sumthd
        Rd                     # ! sumthd
):
    for i in range(0, numof_value, 2):
        if vec_x[i] == 1 and vec_x[i+1] == 1:
            vec_x[i] = pbest_vector[i]
            vec_x[i+1] = pbest_vector[i+1]

    sumof_values, thd_percent, numof_switching, dec_vector, wf_sum = sumthd(vec_x, V, 6, Izm, Rd)

    for j in range(0, len(thd_percent)):   # THD_sum_I(isnan(THD_sum_I))=[100];
        if np.isnan(thd_percent[j]):
            thd_percent[j] = 100

    f = [0, 0, 0]

    o, f[0], f[1] = calcfitness(sumof_values,        # * S
                                thd_percent,         # * THD_sum_I
                                numof_switching, 3)  # * KpOP

    f[2] = numof_switching

    #costs = np.array([all_costs, f])                # TODO Costs

    if np.isnan(pbest_value):
        pbest_vector = o
    if pbest_value > o:
        pbest_value = o
        pbest_vector = vec_x

    #np.append(convergence_curve, pbest_value)       # TODO MyConvergenceCurve

    return o








