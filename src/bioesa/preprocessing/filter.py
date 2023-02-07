import numpy as np
from scipy.signal import butter, filtfilt, iirnotch


def bandpass_filter(F_samp, band=[1, 40]):
    '''
    Generating bandpass Butterworth filter parameters

    F_samp: sampling frequency of the signal
    band: lowcut and highcut values for the filter

    return: butterworth filter parameters

    '''

    [bB, aB] = butter(2, band, btype='bandpass', fs=F_samp)
    return aB, bB


def notch_filter(F_samp, notch=50):
    '''
    Generating notch filter parameters
    Input:
        F_samp: sampling frequency of the signal
        notch: frequency to cut off by notch filter

    return: notch filter parameters
    '''

    [bN, aN] = iirnotch(notch, 30, F_samp)
    return aN, bN


def filter_signal(syg, F_samp, butter_band=[1, 40], notch=50):

    '''
    filtering signal with Butterworth bandpass filter and notch filter

    Input:
        syg: loaded signal
        bandpass_freq: list [highcut value, lowcut value] in Hz
        notch_freq: frequency for notch filter

    Return:
        filtered_signal: signal with all the channels filtered
        with butterworth bandpass and notch filters

    '''

    bB, aB = bandpass_filter(F_samp, butter_band)
    bN, aN = notch_filter(F_samp, notch)

    filtered_signal = np.zeros(np.shape(syg))

    for ch_id in range(syg.shape[1]):
        filtered_signal[:, ch_id] = filtfilt(aB, bB, syg[:, ch_id])
        filtered_signal[:, ch_id] = filtfilt(aN, bN, filtered_signal[:, ch_id])

    return filtered_signal
