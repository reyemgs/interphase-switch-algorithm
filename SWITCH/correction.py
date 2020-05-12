def correction(
    inp_vector, 
    pbest_vector
):
    n = len(inp_vector)
    
    for i in range(0, n, 2):
        if inp_vector[i] == 1 and inp_vector[i+1] == 1:
            inp_vector[i] = pbest_vector[i]
            inp_vector[i+1] = pbest_vector[i+1]
    
    return inp_vector