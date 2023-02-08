from bioesa.preprocessing import load_signal, filter_signal, find_spectrum, plot_spectrum
from bioesa.emg_analysis import emg_montage

import os


if __name__ == '__main__':

    path = '..\data\emg_data'
    s, *params = load_signal(os.path.join(path, 'emg.raw'), 
                             os.path.join(path, 'emg.xml'),
                             os.path.join(path, 'emg.tag'))

    F_samp = params[0]
    channel_names = params[1]
    tags = params[2]

    filt_syg = filter_signal(s, F_samp, butter_band=[25, 400])
    chans = emg_montage(filt_syg)

    f, P = find_spectrum(chans[0], F_samp)
    plot_spectrum(f, P, [20, 400])
