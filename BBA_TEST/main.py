import matplotlib.pyplot as plt
from bba_test import binary_bat_algorithm
from my_cost import my_cost

def main():

    Max_iteration = 30   # Maximum number of iterations
    noP = 25                  # Number of particles
    noV = 100
    A = 0.25                # Loudness  (constant or decreasing)
    r = 0.1                 # Pulse rate (constant or decreasing)
    
    #binary_bat_algorithm(noP, A, r, noV, Max_iteration, my_cost)
    C_Curve = binary_bat_algorithm(noP, A, r, noV, Max_iteration, my_cost)
    
    plt.plot(C_Curve)
    plt.show()

if __name__ == "__main__":
    main()