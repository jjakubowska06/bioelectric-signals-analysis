from bioesa.preprocessing import load_signal, filter_signal
from bioesa.ecg_analysis import einthoven_montage, find_heart_rate, find_hrv, hrv_plot

import os


if __name__ == '__main__':

    data_path = '..\data\ecg_data'
    s, *params, = load_signal(os.path.join(data_path, 'ecg-rest.raw'),
                              F_samp=128, n_channel=3)

    F_samp = params[0]

    filt_syg = filter_signal(s, F_samp, butter_band=[1, 40])

    chans = einthoven_montage(filt_syg)

    HR = find_heart_rate(chans[2], F_samp)

    HRV, t = find_hrv(chans[2], F_samp)
    hrv_plot(HRV, t)
