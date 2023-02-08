import scipy
import matplotlib.pyplot as plt
import numpy as np


def find_spectrum(syg, F_samp):

    '''
    Calculate spectrum in frequency domain using Welch's method
    Input:
      syg: signal from one channel
      F_samp: sampling frequencies
    Output:
      f: array of frequencies
      P: power values for freqs in array f
    '''
    win = np.hamming(len(syg))
    win /= np.linalg.norm(win)

    f, P = scipy.signal.welch(syg, fs=F_samp, window=win, nperseg=len(syg),
                              noverlap=int(0.75*len(syg)), nfft=len(syg),
                              detrend='constant', return_onesided=True,
                              scaling='density', axis=-1, average='mean')
    return f, np.abs(P)


def plot_spectrum(f, P, xlim=[1, 40]):

    '''
    Plot spectrum in frequencies domain
    Input:
      f: array of frequencies
      P: power values for freqs in array f
    '''

    P = P*1e-3

    plt.plot(f, P)
    plt.xlim(xlim)
    plt.ylim(bottom=0)
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Power [MW]')
    plt.title('Power spectrum diagram')
    plt.show()
