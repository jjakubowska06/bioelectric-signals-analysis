import numpy as np


# loading a signal

def load_raw(syg, type, F_samp=128.0):
    
    ds = np.DataSource(None)
    gfile = ds.open(syg, 'rb')
    syg = np.fromfile(gfile, dtype='<f')
        
    if (type=='ECG'):
        syg *= 0.0715
        syg = np.reshape(syg, (len(syg)//3, 3))

    # if type=='EEG':

    # if type=='EMG':

    T = syg.shape[0]/F_samp

    dt = 1/F_samp
    t = np.arange(0,T,dt)
    f = np.arange(0.01,F_samp/2,0.01) 
    
    return syg, F_samp, T, t, f
