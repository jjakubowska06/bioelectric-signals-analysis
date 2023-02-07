import scipy
import numpy as np


def find_Rpeaks(V):
    '''
    A function to find signal indexes of peaks R occurences
    Input: V, filtered and montaged ECG signal channel
    '''
    return scipy.signal.find_peaks(V, height=400)[0]


def find_heart_rate(V, F_samp):

    '''
    A function to determine an average heart rate from signal V
    Input: V, filtered and montaged ECG signal channel

    '''

    # finding R peaks
    peaksR = find_Rpeaks(V)

    # mapping R peaks to time domain
    peak_occurence = np.zeros(len(V))
    peak_occurence[peaksR] = 1

    # we measure heart_rate in 60s periods
    T = 60
    n = int(T*F_samp)
    L = len(V)//n

    hr = np.zeros(L)
    for i in range(L):
        hr[i] += np.sum(peak_occurence[n*i:n*(1+i)])

    print('Mean heart rate value in the respective minutes: ', hr)
    print('Mean heart value: ', np.round(np.mean(hr), 2))

    return hr
