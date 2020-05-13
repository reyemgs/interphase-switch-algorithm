import numpy as np
import matplotlib
from tqdm import tqdm

def binary_bat_algorithm(n, A, r, d, Max_iter, CostFunction):
    #Frequency range
    Q_min = 0
    Q_max = 2
    #Iteration
    N_iter = 0
    #Arrays 

    Q = np.zeros(n)                               #Frequency
    #Q = Q[:, np.newaxis]                          #ROTATE
    V = np.zeros((n, d))                          #Velocities
    Sol = np.zeros((n, d))
    Fitness = np.zeros(n)
    cg_curve = np.zeros(Max_iter)
    #Population/Solutions
    for i in range(0, n):
        for j in range(0, d):                     #For demension
            if np.random.random_sample() <= 0.5:
                Sol[i, j] = 0
            else:
                Sol[i, j] = 1

    for i in range(0, n):
        Fitness[i] = CostFunction(Sol[i,:])

    fmin, I = Fitness.min(0), Fitness.argmin(0)
    best = Sol[I,:]

    
    with tqdm(total = Max_iter) as bar:
        while N_iter < Max_iter - 1:    
            N_iter += 1
            cg_curve[N_iter] = fmin
            for i in range(0, n):
                for j in range(0, d):
                    Q[i] = Q_min + (Q_min - Q_max) * np.random.random_sample()
                    V[i, j] = V[i, j] + (Sol[i, j] - best[j]) * Q[i]
                    V_shaped_transfer_function = np.abs((2 / np.pi) * np.arctan2((np.pi / 2) * V[i,j], 0))
                
                    if np.random.random_sample() < V_shaped_transfer_function:
                        Sol[i, j] = not Sol[i, j]
                    else:
                        Sol[i, j] = Sol[i, j]
                
                    if np.random.random_sample() > r:
                        Sol[i, j] = best[j]
            
                Fnew = CostFunction(Sol[i,:])

                if (Fnew <= Fitness[i]) and (np.random.random_sample() < A):
                    Sol[i,:] = Sol[i,:]
                    Fitness[i] = Fnew
        
                if Fnew <= fmin:
                    best = Sol[i,:]
                    fmin = Fnew
            bar.update(1)
        #print('Number of evaluations: ', N_iter)
        #print('fmin = ', fmin)
    print("\nMatrix f_min:\n", cg_curve)
    print("\nBest values:\n", best)
    print("\nLen of array:\n", len(cg_curve))
    return cg_curve