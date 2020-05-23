import numpy as np
import matplotlib.pyplot as plt
from swalg import iswalg

def main():
    (start_wfsum1, fin_wfsum1,
    start_wfsum2, fin_wfsum2,
    start_wfsum3, fin_wfsum3) = iswalg()

    fig, wf = plt.subplots(1, 3, figsize = (15, 4))

    wf[0].plot(start_wfsum1,
            label = 'start_wfsum1',
            linestyle = '--',
            linewidth = 1,
            color = 'crimson')
    wf[0].plot(fin_wfsum1,
            label = 'fin_wfsum1',
            linestyle = '-',
            linewidth = 1,
            color = 'seagreen')

    wf[1].plot(start_wfsum2,
            label = 'start_wfsum2',
            linestyle = '--',
            linewidth = 1,
            color = 'crimson')
    wf[1].plot(fin_wfsum2,
            label = 'fin_wfsum2',
            linestyle = '-',
            linewidth = 1,
            color = 'seagreen')

    wf[2].plot(start_wfsum3,
            label = 'start_wfsum3',
            linestyle = '--',
            linewidth = 1,
            color = 'crimson')
    wf[2].plot(fin_wfsum3,
            label = 'fin_wfsum3',
            linestyle = '-',
            linewidth = 1,
            color = 'seagreen')

    wf[0].set_xlim(0, 104)
    wf[0].set_ylim(65000, -65000)
    wf[1].set_xlim(0, 104)
    wf[1].set_ylim(65000, -65000)
    wf[2].set_xlim(0, 104)
    wf[2].set_ylim(65000, -65000)
    wf[0].grid(True)
    wf[1].grid(True)
    wf[2].grid(True)
    wf[0].legend()
    wf[1].legend()
    wf[2].legend()

    plt.show()

if __name__ == "__main__":
    main()