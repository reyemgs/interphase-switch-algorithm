import numpy as np
import matplotlib.pyplot as plt
from bpso_test import binary_particle_swarm_optimization
from my_cost import my_cost

def main():

    Max_iteration = 30   # Maximum number of iterations
    noP = 25              # Number of particles
    noV = 100
    ConvergenceCurves = np.zeros((8, Max_iteration))

    print("BPSO1 PROGRESS:")
    gBest1, gBestScore1, ConvergenceCurves[0,:] = binary_particle_swarm_optimization(noP, Max_iteration, 1, my_cost, noV)
    print("BPSO2 PROGRESS:")
    gBest2, gBestScore2, ConvergenceCurves[1,:] = binary_particle_swarm_optimization(noP, Max_iteration, 2, my_cost, noV)
    print("BPSO3 PROGRESS:")
    gBest3, gBestScore3, ConvergenceCurves[2,:] = binary_particle_swarm_optimization(noP, Max_iteration, 3, my_cost, noV)
    print("BPSO4 PROGRESS:")
    gBest4, gBestScore4, ConvergenceCurves[3,:] = binary_particle_swarm_optimization(noP, Max_iteration, 4, my_cost, noV)
    print("BPSO5 PROGRESS:")
    gBest5, gBestScore5, ConvergenceCurves[4,:] = binary_particle_swarm_optimization(noP, Max_iteration, 5, my_cost, noV)
    print("BPSO6 PROGRESS:")
    gBest6, gBestScore6, ConvergenceCurves[5,:] = binary_particle_swarm_optimization(noP, Max_iteration, 6, my_cost, noV)
    print("BPSO7 PROGRESS:")
    gBest7, gBestScore7, ConvergenceCurves[6,:] = binary_particle_swarm_optimization(noP, Max_iteration, 7, my_cost, noV)
    print("BPSO8 PROGRESS:")
    gBest8, gBestScore8, ConvergenceCurves[7,:] = binary_particle_swarm_optimization(noP, Max_iteration, 8, my_cost, noV)
    
    print("\ngBest1:\n", gBest1)
    print("gBest2:\n", gBest2)
    print("gBest3:\n", gBest3)
    print("gBest4:\n", gBest4)
    print("gBest5:\n", gBest5)
    print("gBest6:\n", gBest6)
    print("gBest7:\n", gBest7)
    print("gBest8:\n", gBest8)

    print("\ngBestScore1:", gBestScore1)
    print("gBestScore2:", gBestScore2)
    print("gBestScore3:", gBestScore3)
    print("gBestScore4:", gBestScore4)
    print("gBestScore5:", gBestScore5)
    print("gBestScore6:", gBestScore6)
    print("gBestScore7:", gBestScore7)
    print("gBestScore8:", gBestScore8)

    print("\nConvergence Curves:\n", ConvergenceCurves)

    plt.semilogy(ConvergenceCurves)
    plt.show()

if __name__ == "__main__":
    main()