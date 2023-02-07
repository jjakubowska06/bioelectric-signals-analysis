import matplotlib.pyplot as plt
import numpy as np

from .heart_rate import find_Rpeaks


def find_hrv(V, F_samp):

    '''
    Function to calculate HRV signal
    Input:
        V: signal from one channel
        F_samp: sampling frequency
    Output:
        HRV: an array with hrv values between each R peak
        time: an array of time corresponding to HRV array
    '''

    peaks = find_Rpeaks(V)
    HRV = np.diff(peaks)/F_samp

    t = np.arange(0, len(V)/F_samp, 1/F_samp)
    time = [t[peaks[i]] for i in range(len(peaks)-1)]

    return HRV, time


def hrv_plot(HRV, t):
    '''
    Function to plot HRV
    '''

    plt.plot(t, HRV)
    plt.title('HRV')
    plt.xlabel('Time [s]')
    plt.ylabel('HRV [s]')
    plt.show()
