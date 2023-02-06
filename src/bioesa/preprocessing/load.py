import numpy as np
from obci_readmanager.signal_processing.read_manager import ReadManager

# loading a signal
def load_raw(syg, type, F_samp=128.0):
    '''
    '''
    
    ds = np.DataSource(None)
    gfile = ds.open(syg, 'rb')
    syg = np.fromfile(gfile, dtype='<f')
    syg *= 0.0715

    if type.upper()=='ECG':
        n_channels = 3
    # elif type.upper()=='EEG':
        # n_channels = 
    elif type.upper()=='EMG':
        n_channels = 5
    else:
        raise Exception('This package was made for EEG, EMG and ECG signal analysis only')

    syg = np.reshape(syg, (len(syg)//n_channels, n_channels))
    return syg, F_samp


def load_Readmenager(info, signal, tags):
    '''
    '''
    
    mgr = ReadManager(info, signal, tags)

    F_samp = float(mgr.get_param("sampling_frequency"))
    #num_of_channels = int(mgr.get_param("number_of_channels"))
    channels_names = mgr.get_param("channels_names")

    syg = mgr.get_samples() * 0.0715

    tags = mgr.get_tags()

    return syg, F_samp, channels_names
