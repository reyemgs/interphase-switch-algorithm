import numpy as np
from cost import costfunction

# ! MainOneBBA.m
def main(
    numof_value,                               # * noV
    #wf_vector                                 # * Izm
    costfunction,                               # ? MyCost.m
    sumthd,                                    # ? Calc_sum_thd.m
    bba                                        # ? BBA.m
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

    v_struct = []       # * V
    bin_vector = []     # * kodV
    y = 0


if __name__ == "__main__":
    main()