import numpy as np
from correction import correction
from calcfitness import calcfitness
from sumthd import sumthd
from cost import costfunction
from binbatalg import bba
Rd = np.loadtxt('C:/interphase-switch-algorithm/SWITCH/samples/Rd.txt')
# ! MainOneBBA.m
def main(
        # numof_value,                      # * noV
        # wf_vector,                        # * Izm
        # costfunction,                     # ? MyCost.m
        # sumthd,                           # ? Calc_sum_thd.m
        # calcfitness,                      # ? Calc_Fitness.m
        # bba,                              # ? BBA.m
        # correction                        # ? Korrection.m
):
    # Данные
    total_spc = 3                           # * col_OP
    max_iteration = 30                      # * Max_iteration
    numof_agents = 25                       # * noP
    numof_value = total_spc * 2             # * noV
    count_wf = 56                           # * Count_Osc
    wf_vector = np.zeros((count_wf, 104))   # * Izm
    y = 0                                   # * Y
    s = np.loadtxt('C:/interphase-switch-algorithm/SWITCH/samples/Izm.txt')

    for i in range(0, 56):
        wf_vector[i,] = s[i,]

    # * SamplesV
    #v = np.loadtxt('C:/interphase-switch-algorithm/SWITCH/samples/V.txt')
    v2 = np.loadtxt('C:/interphase-switch-algorithm/SWITCH/samples/v2.txt')
    v3 = np.loadtxt('C:/interphase-switch-algorithm/SWITCH/samples/v3.txt')
    kv = np.loadtxt('C:/interphase-switch-algorithm/SWITCH/samples/kV.txt')

    start_sum = np.array([])                # * StartSum
    start_thd = np.array([])                # * StartTHD
    v_struct = np.array([[]])               # * V
    bin_vector = np.array([])               # * kodV
    best_f = np.array([])                   # * BestsF

    pbest_vector = bin_vector
    pbest_value = 0

    #Результаты
    y_n = 0                                 # * Y_N
    time = 0                                # * Time
    fbest = 0                               # * Fbest
    fsteps = 0                              # * Fsteps
    fin_vector = 0                          # * FinVect
    distr_spc = 0                           # * RasprOP
    numof_switch = 0                        # * KpOP
    fmean = 0                               # * Fmean
    fvar = 0                                # * Fvar
    yok = 0                                 # * YoK

    #Обработка примеров
    v_struct = np.array([[0, 0, 0], v2, v3])
    print(v_struct)
    bin_vector = kv


    # * Вызов sumthd
    (start_sum, start_thd,
    start_nswitch, dec_vector,
    start_wfsum) = sumthd(bin_vector, v_struct,                         # TODO Calcthd
                                        numof_value, wf_vector, Rd)

    # Корректируем THD
    for j in range(0, len(start_thd)):   # StartTHD(isnan(StartTHD))=[100];
        if np.isnan(start_thd[j]):
            start_thd[j] = 100

    # * Вызов costfunction
    start_score = costfunction(bin_vector, bin_vector, pbest_value,     # TODO Sumthd, Calcfitness
                                numof_value, v_struct, wf_vector, Rd)#,    # ? Caclthd
                                #start_sum, start_thd, start_nswitch)

    # * Вызов calcfitness
    O ,start_f1, start_f2 = calcfitness(start_sum, start_thd,              # TODO Ничего не вызывается
                                    start_nswitch, total_spc)

    pbest_vector = bin_vector
    pbest_value = start_score

    A = .25
    r = .1

    # * Вызов bba
    (g_best, g_bestscore,
    convergence_curve) = bba(numof_agents, A, r, numof_value,           # TODO Costfunction
                            max_iteration, bin_vector,                     # ? Sumthd, Calcfitness
                            pbest_vector, pbest_value,                     # * Calcthd
                            v_struct, wf_vector, Rd)

    # * Вызов correction
    g_best = correction(g_best, pbest_vector)
    print('\ngBest: ', g_best)
    convergence_curve /= start_score

    (fin_sum, fin_thd,
    switch, distr_spc, fin_wfsum) = sumthd(g_best, v_struct, numof_value,
                                            wf_vector, Rd)
    best_f = np.append(g_best, g_best/start_score)
    if best_f[0] <= 0.9:
        y_n = 1
        y += 1
    else:
        y_n = 0

    fbest = best_f[0]
    fsteps = convergence_curve
    fin_vector = g_best
    distr_spc = distr_spc
    fmean = np.mean(best_f)
    fvar = np.var(best_f)
    yok = y

if __name__ == "__main__":
    main()