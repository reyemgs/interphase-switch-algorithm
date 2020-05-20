import matplotlib.pyplot as plt
import numpy as np
from bba_test import binary_bat_algorithm
from my_cost import my_cost
path = 'C:/interphase-switch-algorithm/SWITCH/samples/'
def main():

    Max_iteration = 30   # Maximum number of iterations
    noP = 25                  # Number of particles
    noV = 6
    A = .25                # Loudness  (constant or decreasing)
    r = .1                 # Pulse rate (constant or decreasing)
    kodV = np.loadtxt(path + 'kV.txt')
    #binary_bat_algorithm(noP, A, r, noV, Max_iteration, my_cost, kodV)
    C_Curve = binary_bat_algorithm(noP, A, r, noV, Max_iteration, my_cost, kodV)

    plt.plot(C_Curve)
    plt.show()

if __name__ == "__main__":
    main()