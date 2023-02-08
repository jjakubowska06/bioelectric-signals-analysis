from bioesa.preprocessing import load_signal, filter_signal, find_spectrum, plot_spectrum
from bioesa.eeg_analysis import eeg_montage, evoked_potentials

import matplotlib.pyplot as plt
import os


if __name__ == '__main__':

    path = '..\data\eeg_data'
    s, *params = load_signal(os.path.join(path, 'eeg_evoked.raw'),
                             os.path.join(path, 'eeg_evoked.xml'),
                             os.path.join(path, 'eeg_evoked.tag'))

    F_samp = params[0]
    channel_names = params[1]
    tags = params[2]

    syg_mont = eeg_montage(s)
    filt_syg = filter_signal(syg_mont, F_samp, butter_band=[1, 40])

    eps = evoked_potentials(filt_syg[17], tags, F_samp)
    plot_spectrum(*find_spectrum(eps[0], F_samp), [1, 40])
    plot_spectrum(*find_spectrum(eps[1], F_samp), [1, 40])
    plt.show()
