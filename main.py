import numpy as np
import matplotlib.pyplot as plt
from swalg import iswalg

def main():
    fin_wfsum, start_wfsum = iswalg()
    fig, wf = plt.subplots()
    wf.plot(fin_wfsum,             # * FinSumOsc
            marker = 'o',
            markersize = '3',
            label = 'fin_curve',
            linestyle = '-',
            linewidth = 1,
            color = 'seagreen')
    wf.plot(start_wfsum,           # * StartSumOsc
            label = 'start_curve',
            linestyle = '--',
            linewidth = 1,
            color = 'crimson')
    fig.set_figwidth(6)
    fig.set_figheight(6)
    plt.show()

if __name__ == "__main__":
    main()