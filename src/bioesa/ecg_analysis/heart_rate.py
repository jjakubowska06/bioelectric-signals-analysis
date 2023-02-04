import scipy
import numpy as np

def find_Rpeaks(V):
    return scipy.signal.find_peaks(V, prominence=(max(V)-min(V))*0.7)[0]

def heart_rate(V, F_samp):
    
    '''
    '''

    peaksR = find_Rpeaks(V)

    # find R peaks (indexes in time)
    peak_occurence = np.zeros(len(V))
    peak_occurence[peaksR] = 1

    # we measure heart_rate in a 60s period
    T = 60 
    n = int(T*F_samp)

    L = len(V)//n
    hr = np.zeros(L)
    
    for i in range(L):
        hr[i] += np.sum(peak_occurence[n*i:n*(1+i)])

    print('Wartości tętna w kolejnych minutach:', hr)
    print('Srednie tetno: ', np.round(np.mean(hr), 2))
    
    return hr
