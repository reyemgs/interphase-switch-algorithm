import numpy as np
import math
import matplotlib

def binary_bat_algorithm(n, A, r, d, Max_iter, CostFunction):
    #Frequency range
    Q_min = 0
    Q_max = 2
    #Iteration
    N_iter = 0
    #Arrays
    Q = np.zeros((1, n))                    #Frequency
    V = np.zeros((n, d))                    #Velocities
    Sol = np.zeros((n, d))
    Fitness = np.zeros(n)
    cg_curve = np.zeros((1, Max_iter))
    #Population/Solutions
    for i in range(1, n + 1):
        for j in range(1, d + 1):               #For demension
            if np.random.random_sample() <= 0.5:
                Sol[i, j] = 0
            else:
                Sol[i, j] = 1
    
    for i in range(1, n + 1):
       Fitness[i] = CostFunction(Sol[i,:])
    
    fmin, I = Fitness.min(1), Fitness.argmin(1)
    best = Sol[I,:]

    while N_iter < Max_iter:
        N_iter += 1
        cg_curve[N_iter] = fmin
        for i in range(1, n):
            for i in range(1, d):
                Q[i] = Q_min + (Q_min + Q_max) * np.random.random_sample()
                V[i, j] = V[i, j] + (Sol[i, j] - best[j]) * Q[i]
                V_shaped_transfer_function = math.fabs((2 / math.pi) * math.atan((math.pi / 2) * V[i,j]))
                
                if np.random.random_sample() < V_shaped_transfer_function:
                    Sol[i, j] = not Sol[i, j]
                else:
                    Sol[i, j] = Sol[i, j]
                
                if np.random.random_sample() < r:
                    Sol[i, j] = best[j]
        Fnew = CostFunction(Sol[i,:])

        if Fnew <= Fitness[i] and np.random.random_sample() < A:
            Sol[i,:] = Sol[i,:]
            Fitness[i] = Fnew
        
        if Fnew <= fmin:
            best = Sol[i,:]
            fmin = Fnew
    
    print('Number of evaluations: ',N_iter)
    print('fmin = ', fmin)
    




