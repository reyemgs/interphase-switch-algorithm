import numpy as np
import scipy.io as sio
from termcolor import colored
from correction import correction
from calcfitness import calcfitness
from sumthd import sumthd
from cost import costfunction
from binbatalg import bba
#Rd = np.loadtxt('C:/interphase-switch-algorithm/samples/Rd.txt')
#Rd = np.array([1, 2, 3])

# ! MainOneBBA.m
def iswalg():
    # Данные                                # TODO for сol_OP = 3:30
    total_spc = 30                          # * col_OP
    max_iteration = 30                      # * Max_iteration
    numof_agents = 25                       # * noP
    numof_value = total_spc * 2             # * noV
    count_wf = 56                           # * Count_Osc
    wf_vector = np.zeros((count_wf, 104))   # * Izm
    y = 0                                   # * Y
    s = np.loadtxt('C:/interphase-switch-algorithm/samples/Izm.txt')

    for i in range(0, 56):
        wf_vector[i,] = s[i,]

    # * SamplesV
    struct = sio.loadmat('C:/interphase-switch-algorithm/samples/V.mat')
    samples_v = struct['SamlesV']
    v2 = samples_v['V2']
    v3 = samples_v['V3']
    kv = samples_v['kV']
    v_struct = np.zeros((3, total_spc))     # * V

    Rd =np.zeros(total_spc)
    start_sum = np.array([])                # * StartSum
    start_thd = np.array([])                # * StartTHD
    bin_vector = np.array([])               # * kodV
    best_f = np.array([])                   # * BestsF

    pbest_value = np.nan
    pbest_vector = bin_vector

    print('\nCalculated for TSPC = ', total_spc)
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
    print('Processing the ', 1 ,'example')
    v_struct[1,] = v2[0, total_spc - 1][0,]
    v_struct[2,] = v3[0, total_spc - 1][0,]
    bin_vector = kv[0, total_spc - 1][0,]
    print(v_struct)
    # * Вызов sumthd
    (start_sum, start_thd,
    start_nswitch, dec_vector, start_wfsum) = sumthd(bin_vector, v_struct,
                                                    numof_value, wf_vector, Rd)
    # print(  'Start_sum:\n', start_sum,
    #     '\nStart_THD:\n', start_thd,
    #     '\nStartKPOP:\n', start_nswitch,
    #     '\nRd:\n', dec_vector,
    #     '\nStartSumOSC:\n', start_wfsum)
    print('\n\tsumthd: OK')

    # Корректируем THD
    for j in range(0, len(start_thd)):   # StartTHD(isnan(StartTHD))=[100];
        if np.isnan(start_thd[j]):
            start_thd[j] = 100

    # * Вызов costfunction
    start_score = costfunction(bin_vector, bin_vector, pbest_value,
                                numof_value, v_struct, wf_vector, Rd)
    print('\n\tcostfunction: OK')

    # * Вызов calcfitness
    O ,start_f1, start_f2 = calcfitness(start_sum, start_thd,
                                        start_nswitch, total_spc)
    print('\n\tcalcfitness: OK')

    pbest_vector = bin_vector
    pbest_value = start_score
    A = 0.25
    r = 0.1

    # * Вызов bba
    (g_best, g_bestscore,
    convergence_curve) = bba(numof_agents, A, r, numof_value, max_iteration, bin_vector,
                            pbest_vector, pbest_value, v_struct, wf_vector, Rd)
    print('\n\tbba: OK')

    # * Вызов correction
    g_best = correction(g_best, pbest_vector)
    convergence_curve /= start_score
    print('\n\tcorrection: OK')

    # *Вызов sumthd
    (fin_sum, fin_thd,
    switch, distr_spc, fin_wfsum) = sumthd(g_best, v_struct, numof_value,
                                            wf_vector, Rd)
    print('\n\tsumthd: OK\n')

    best_f = np.append(best_f, g_bestscore/start_score)
    print('BestsF: ', best_f)
    print('gBestScore: ', g_bestscore)
    print('StartScore: ', start_score)
    if best_f[0] <= 0.9:
        y_n = 1
        y += 1
    else:
        y_n = 0

    fbest = best_f[0]
    fsteps = convergence_curve
    fin_vector = g_best
    distr_spc = distr_spc
    numof_switch = switch
    fmean = np.mean(best_f)
    fvar = np.var(best_f)
    yok = y
    print(
        'FinSum:', fin_sum,
        '\nFinTHD:', fin_thd,
        '\nFbest:', fbest,
        '\nFsteps:', fsteps,
        '\nFinVector:', fin_vector,
        '\nSwitch:', switch,
        '\nKpOP:', numof_switch,
        '\nRaspr_OP:', distr_spc,
        '\nFinSumOsc:', fin_wfsum,
        '\nFmean:', fmean,
        '\nFvar:', fvar,
        '\nYoK:', yok)

    return start_wfsum[0,], fin_wfsum[0,], start_wfsum[1,], fin_wfsum[1,], start_wfsum[2,], fin_wfsum[2,]