import matplotlib.pyplot as plt
import numpy as np


def channels_definition(s):
    '''
    Function to give channels name accordingly to ECG montage systems
    Input:
        s: filtered signal
    Output:
        VLR, VPR, VLN: each channels named accordingly
                        to ECG montage system
    '''

    VLR = s[0, :]
    VPR = s[1, :]
    VLN = s[2, :]

    return VLR, VPR, VLN


def einthoven_montage(s):
    '''
    Einthoven montage system

    s: signal, should be filtered beforehand
    V1, V2, V3: arrays with voltage between respective leads
    '''

    VLR, VPR, VLN = channels_definition(s)

    V1 = VLR-VPR
    V2 = VLN-VPR
    V3 = VLN-VLR

    return V1, V2, V3


def goldberg_montage(s):
    '''
    Goldberg montage system

    s: signal, should be filtered beforehand
    aVl, aVr, aVn: arrays with voltage between respective leads
    '''

    VLR, VPR, VLN = channels_definition(s)

    aVl = VLR - (VPR + VLN)/2
    aVr = VPR - (VLR + VLN)/2
    aVn = VLN - (VLR + VPR)/2

    return aVl, aVr, aVn


def plot_montage(*channels):

    '''
    Function to plot all ECG channels after the montage
    '''

    for i in range(np.shape(channels)[0]):
        plt.subplot(3, 1, i+1)
        plt.plot(channels[i][0:600])
        plt.title('Lead nr {}'.format(i))
    plt.suptitle('Einthoven')
    plt.tight_layout()
    plt.show()
