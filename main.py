import numpy as np
import matplotlib.pyplot as plt
from swalg import iswalg

def main():
    fin_curve, start_curve = iswalg()
    fig, wf = plt.subplots()

    wf.plot(fin_curve, label = 'fin_curve', linestyle = ':', linewidth = 2)
    wf.plot(start_curve, label = 'start_curve', linestyle = '--', linewidth = 4)

    fig.set_figwidth(6)
    fig.set_figheight(6)

    plt.show()

if __name__ == "__main__":
    main()