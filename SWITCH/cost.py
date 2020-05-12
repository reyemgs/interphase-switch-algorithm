import numpy as np
# ! My_Cost.m
def costfunction(
    vec_x,                 # * Vx (not sure)
    pbest_vector,          # * PreviousV
    pbest_value,           # * PreviousBest
    numof_value,           # * noV
    convergence_curve,     # * MyConvergenceCurve
    all_costs,             # * AllCosts
    sumthd,                # * calc_sum_thd.m
    calculationfitness     # * calc_fitness.m
):
    for i in range(0, numof_value, 2):
        if vec_x[i] == 1 and vec_x[i+1] == 1:
            vec_x[i] = pbest_vector[i]
            vec_x[i+1] = pbest_vector[i+1]
    #1)S          2)THD_sum_I  3)KPOP            4)Sum_THD(x)
    sumof_values, thd_percent, numof_switching = sumthd(vec_x)    # ? Вызов Calc_Sum_THD

    thd_percent = np.isnan(thd_percent) # ! Неверно
    #f(1,1), f(1,2)
    o, f1, f2 = calculationfitness(                               # ? Вызов Calc_Fitness
                                    sumof_values,     # * S              
                                    thd_percent,      # * THD_sum_I
                                    numof_switching)  # * KpOP
    f3 = numof_switching
    #costs = [all_costs; f3]
    if pbest_value > o:
        pbest_value = o
        pbest_vector = vec_x

    convergence_curve = [convergence_curve, pbest_value]

    return o








