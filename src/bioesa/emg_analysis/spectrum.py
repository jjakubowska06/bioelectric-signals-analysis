import scipy
import matplotlib.pyplot as plt


def spectrum(syg, F_samp): 
  f, P = scipy.signal.welch(syg, fs=F_samp, window ='hann', nperseg=len(syg), noverlap=int(0.75*len(syg)), nfft=len(syg), scaling='density', axis=- 1, average='mean') 

  return f, P

def plot_spectrum(syg, F_samp):
    
    f, P = spectrum(syg, F_samp)
    # fig = plt.figure(figsize = (20,20), dpi = 100)
   
    # for i, signal in enumerate(load):
    #     f, P = widmo(signal, F_samp)
    #     P = P*1e-3

    plt.plot(f, P)
    # plt.xlim(10, 200)
    # plt.ylim(bottom = 0)
    plt.xlabel('częstotliwość [Hz]')
    plt.ylabel('Moc [W]')
    # plt.title('Widmo dla obciążenia: ' + str(x[i]))

    # fig.subplots_adjust(hspace=.5)
    plt.show()

