import matplotlib.pyplot as plt
import numpy as np
import scipy

from .heart_rate import find_Rpeaks


def hrv(V, F_samp):
   
    '''
    '''

    peaks = find_Rpeaks(V)    
    HRV = np.diff(peaks)/F_samp

    t = np.arange(0,len(V)/F_samp, 1/F_samp)
    time = [t[peaks[i]] for i in range(len(peaks)-1)]

    return HRV, time
    

def hrv_plot(HRV, t):
    '''
    '''
    
    fig=plt.figure(figsize=(12,10), dpi= 100)
    plt.plot(t, HRV)
    plt.title('HRV')
    plt.xlabel('Time [s]')
    plt.show()

