import scipy
import matplotlib.pyplot as plt


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

    f, P = scipy.signal.welch(syg, fs=F_samp, window='hann', nperseg=len(syg),
                              noverlap=int(0.75*len(syg)), nfft=len(syg),
                              scaling='density', axis=-1, average='mean')
    return f, P


def plot_spectrum(f, P):

    '''
    Plot spectrum in frequencies domain
    Input:
      f: array of frequencies
      P: power values for freqs in array f
    '''

    P = P*1e-3

    plt.plot(f, P)
    plt.xlim(10, 400)
    plt.ylim(bottom=0)
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Power [MW]')
    plt.title('Power spectrum diagram')
    plt.show()
