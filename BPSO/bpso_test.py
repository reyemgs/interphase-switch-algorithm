import numpy as np
import matplotlib
import math
from tqdm import tqdm

def binary_particle_swarm_optimization(noP, Max_iteration, BPSO_num, CostFunction, noV):
    w = 2
    wMax = 0.9
    wMin = 0.4
    c1 = 2
    c2 = 2
    Vmax = 6

    Velocity = np.zeros((noP, noV))
    Position = np.zeros((noP, noV))

    pBestScore = np.zeros(noP)
    pBest = np.zeros((noP, noV))

    gBestScore = np.Inf
    gBest = np.zeros(noV)

    ConvergenceCurve = np.zeros(Max_iteration)

    for i in range(0, np.size(Position, 0)):
        for j in range(0, np.size(Position, 1)):
            if np.random.random_sample() <= 0.5:
                Position[i, j] = 0
            else:
                Position[i, j] = 1

    for i in range(0, noP):
        pBestScore[i] = np.Inf

    for l in tqdm(range(0, Max_iteration)):

        for i in range(0, np.size(Position, 0)):
            fitness = CostFunction(Position[i,:])

            if pBestScore[i] > fitness:
                pBestScore[i] = fitness
                pBest[i,:] = Position[i,:]

            if gBestScore > fitness:
                gBestScore = fitness
                gBest = Position[i,:]

        w = wMax - l * ((wMax - wMin) / Max_iteration)

        for i in range(0, np.size(Position, 0)):
            for j in range(0, np.size(Position, 1)):
                Velocity[i, j] = (w * Velocity[i, j] + c1 * np.random.random_sample()
                    * (pBest[i, j] - Position[i, j]) + c2 * np.random.random_sample()
                    * (gBest[j] - Position[i, j]))

                if Velocity[i, j] > Vmax:
                    Velocity[i, j] = Vmax

                if Velocity[i, j] < -Vmax:
                    Velocity[i, j] = -Vmax

                if BPSO_num == 1:
                    s = 1 / (1 + np.exp(-2 * Velocity[i,j]))

                if BPSO_num == 2:
                    s = 1 / (1 + np.exp(-Velocity[i,j]))

                if BPSO_num == 3:
                    s = 1 / (1 + np.exp(-Velocity[i,j] / 2))

                if BPSO_num == 4:
                    s = 1 / (1 + np.exp(-Velocity[i,j] / 3))

                if BPSO_num <= 4:
                    if np.random.random_sample() < s:
                        Position[i, j] = 1
                    else:
                        Position[i, j] = 0

                if BPSO_num == 5:
                    s = np.abs(math.erf(((math.sqrt(np.pi) / 2) * Velocity[i, j])))

                if BPSO_num == 6:
                    s = np.abs(np.tanh(Velocity[i, j]))

                if BPSO_num == 7:
                    s = np.abs(Velocity[i, j] / math.sqrt(1 + Velocity[i, j] ** 2))

                if BPSO_num == 8:
                    s = np.abs((2 / np.pi) * np.arctan((np.pi / 2) * Velocity[i, j]))

                if BPSO_num > 4 and BPSO_num <= 8:
                    if np.random.random_sample() < s:
                        Position[i, j] = not Position[i, j]

        ConvergenceCurve[l] = gBestScore
        #print("Value of BPSO", BPSO_num, ":", gBestScore)
    return gBest, gBestScore, ConvergenceCurve