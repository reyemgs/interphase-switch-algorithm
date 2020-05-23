import numpy as np
# ! Korrection.m
def correction(
        inp_vector,   # * g_best
        pbest_vector  # * pbest_vector
):
    n = len(inp_vector)
    for i in range(0, n, 2):
        if inp_vector[i] == 1 and inp_vector[i+1] == 1:
            inp_vector[i] = pbest_vector[i]
            inp_vector[i+1] = pbest_vector[i+1]
    output_vector = inp_vector
    return output_vector