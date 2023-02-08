import numpy as np


def a1a2mean_montage(syg, num_of_channels):

    '''
    Most standard montage; the mean of signals from A1 and A2
    electrode is substracted from signals from other electrodes
    Input:
        syg: eeg signal
    Output:
        syg_montaged: montaged eeg signal
    '''

    for n in range(num_of_channels):
        syg[n] -= (syg[20]+syg[19])/2
    return syg


def a1_montage(syg, num_of_channels):

    '''
    Montage: A1 channel substracted from the rest of signals
    electrode is substracted from signals from other electrodes
    Input:
        syg: eeg signal
    Output:
        syg_montaged: montaged eeg signal
    '''

    for n in range(num_of_channels):
        syg[n] -= syg[19]
    return syg


def a2_montage(syg, num_of_channels):

    '''
    Montage: A2 channel substracted from the rest of signals
    Input:
        syg: eeg signal
    Output:
        syg_montaged: montaged eeg signal
    '''

    for n in range(num_of_channels):
        syg[n] = syg[20]
    return syg


def eeg_montage(syg, type='a1a2mean'):

    '''
    Function to montage EEG signal
    Input:
        syg: eeg signal
    Output:
        syg_montaged: montaged eeg signal
    '''

    s = np.copy(syg)
    num_of_channels = np.shape(syg)[0]

    if type == 'a1a2mean':
        montaged_signal = a1a2mean_montage(s, num_of_channels)
    elif type == 'a1montage':
        montaged_signal = a1_montage(s, num_of_channels)
    elif type == 'a2montage':
        montaged_signal = a2_montage(s, num_of_channels)
    else:
        raise ValueError('Only three types of EEG montage are\
                         available: "a1a2mean", "a1" and "a2"S')
    return montaged_signal
