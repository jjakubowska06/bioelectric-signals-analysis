from preprocessing.filter import *
from preprocessing.load import *
from ecg_analysis.montage import * 
from ecg_analysis.heart_rate import *

import matplotlib.pyplot as plt

if __name__=='__main__':
    
    s, F_samp, T, t, f = load_raw('D:/projekty-zaliczeniowe/bioelectric-signals-analysis/data/ekg.raw', 'ECG')
    filt_syg = filter_signal(s, F_samp)

    # plt.plot(t, s[:,1])
    plt.plot(t[200:400], filt_syg[:,1][200:400])
    plt.show()

    #einthoven(filt_syg)
    chans = einthoven(filt_syg)
    # plot_einthoven(*chans)
    HR = heart_rate(chans[2], F_samp)
    
    #plot_goldberg(*goldberg(filt_syg))

