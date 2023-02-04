import numpy as np
from scipy.signal import butter
from scipy.signal import filtfilt
from scipy.signal import iirnotch


def bandpass_filter(F_samp, band=[1, 40]):
    
    ''' 
    Generating bandpass Butterworth filter parameters 

    F_samp: sampling frequency of the signal
    band: lowcut and highcut values for the filter
    '''

    [bB,aB]=butter(2, band, btype = 'bandpass',fs = F_samp)

    return aB, bB

    
def notch_filter(F_samp, notch=50):
    
    '''
    generating notch filter parameters 

    F_samp: sampling frequency of the signal
    notch: frequency to cut off by notch filter

    return: 
    '''
 
    bN,aN = iirnotch(notch, 30, F_samp)
    
    return aN, bN


def filter_signal(syg, F_samp, butter_band=[1, 40], notch=50):

    '''
    filtering signal with Butterworth bandpass filter and notch filter

    Input:
    syg: 
    bandpass_freq:
    notch_freq:

    Return:
    filtered_signal - 

    '''

    bB, aB = bandpass_filter(F_samp, butter_band)
    bN, aN = notch_filter(F_samp, notch)

    filtered_signal = np.zeros(np.shape(syg))

    for channel_id in range(syg.shape[1]):
        filtered_signal[:,channel_id] = filtfilt(aB, bB, syg[:,channel_id])
        filtered_signal[:,channel_id] = filtfilt(aN, bN, filtered_signal[:,channel_id])
    
    return filtered_signal

