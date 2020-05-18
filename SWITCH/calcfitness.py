import math
import numpy as np

# ! Calc_Fitness.m
def calcfitness(
        sumof_values,    # * S
        thd_sum,         # * T
        numof_switching, # * KpOP
        #start_thd,       # * StartTHD
        total_spc        # * Col_OP
):
    total_spc = 3
    f1 = ((sumof_values[0]**2 + sumof_values[1]**2 + sumof_values[2]**2) /
            ((sumof_values[0] + sumof_values[1] + sumof_values[2])**2))

    f2 = math.sqrt((thd_sum[0] + thd_sum[1] + thd_sum[2]) / 900)

    f3 = numof_switching / total_spc

    f1 *= 0.7
    f2 *= 0.2
    f3 *= 0.1

    o = f1 + f2 + f3

    #return o, f1, f2, f3
    return o, f1, f2




