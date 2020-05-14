import numpy as np
from cost import costfunction

# ! MainOneBBA.m
def main(
    numof_value,                               # * noV
    #wf_vector                                 # * Izm
    costfunction,                              # ? MyCost.m
    sumthd,                                    # ? Calc_sum_thd.m
    calcfitness,                               # ? Calc_Fitness.m
    bba,                                       # ? BBA.m
    correction                                 # ? Korrection.m
):
    max_iteration = 30                         # * Max_iteration
    numof_agents = 25                          # * noP
    count_wf = 56                              # * Count_Osc
    global start_sum, start_thd # ! Проверить
    wf_vector = np.zeros((count_wf, 104))      # * Izm

    for i in range(0, 56):
        s = np.loadtxt('samples/wf_best')
        wf_vector[i, :] = s
        s = []

    # * SamplesV
    v2 = np.loadtxt('samples/v2.txt')
    v3 = np.loadtxt('samples/v3.txt')
    kv = np.loadtxt('samples/kV.txt')

    v_struct = np.array([])       # * V
    bin_vector = np.array([])     # * kodV
    y = 0

    results = { 'y_n': 0,
                'time': 0,
                'fbest': 0,
                'fsteps': 0,
                'fin_vector': 0,
                'distr_spc': 0,
                'numof_switch': 0,
                'fmean': 0,
                'fvar': 0,
                'yok': 0
    }

    v_struct[0,:] = v2[0,:]
    v_struct[1,:] = v3[0,:]
    bin_vector = kv[0,:]

    start_sum, start_thd, start_nswitch, start_wfsum = sumthd(bin) # TODO Прописать через модуль
    start_thd = np.isnan(start_thd) # ! Неверно
    start_score = costfunction(bin_vector) # TODO Дописать параметры
    f1, f2 = calcfitness(start_sum, start_thd, start_nswitch)

    pbest_vector = bin_vector
    pbest_value = start_score

    A = .25
    r = .1

    g_best, g_bestscore, convergence_curve = bba(numof_agents, # ? Вызов BBA
                                                A, r, numof_agents,
                                                max_iteration,
                                                costfunction,
                                                bin_vector)
    g_best = correction(g_best, pbest_vector)

    convergence_curve /= start_score

    fin_sum, fin_thd, switch, distr_spc, fin_wfsum = sumthd(g_best)


















# if __name__ == "__main__":
#     main()