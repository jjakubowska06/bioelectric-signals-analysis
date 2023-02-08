import numpy as np
from obci_readmanager.signal_processing.read_manager import ReadManager


def load_raw(syg, F_samp=128., n_channels=3):
    '''
    A function to load raw signal WITHOUT tags and metadata
    Input:
        signal: .raw bioelectric signal
        type: type of signal ('eeg', 'ecg' or 'emg')
        F_samp: sampling frequency

        n_channels: number of channels in EMG signal
    Output:
        syg: loaded syg, an array where each row is a separate channel
        F_samp: signal frequency
    '''
    ds = np.DataSource(None)
    gfile = ds.open(syg, 'rb')
    syg = np.fromfile(gfile, dtype='<f')
    syg = np.reshape(syg, (len(syg)//n_channels, n_channels)) * 0.0715

    return syg.transpose(), F_samp


def load_signal(signal, info=None, tags=None, F_samp=None, n_channel=None):
    '''
    A function to load signal, with/without tags and metadata
    Input:
        signal: .raw bioelectric signal
        For signals with metadata:
            info: metadata in .xml format
            tags: .tag file with signal tags
        For raw signals without metadata:
            n_channel: number of channels
            F_samp: sampling frequency
    Output:
        syg: loaded syg, an array where each row is a separate channel
        F_samp: signal frequency
        *channels_names: names of channels
    '''
    if not signal.split('.')[-1] == 'raw':
        raise TypeError('Signal should be in a .raw format')

    # load raw signal without tags and metadata
    if (not info and not tags) and (F_samp and n_channel):
        if not (isinstance(F_samp, float) or isinstance(n_channel, int)):
            raise TypeError('F_samp: float, n_channel: int')
        else:
            return load_raw(signal, F_samp=F_samp, n_channels=n_channel)

    # load signal with tags and metadata
    elif info and tags:
        if not (info.split('.')[-1] == 'xml' and tags.split('.')[-1] == 'tag'):
            raise TypeError('metadata should be a .xml file, and tags a \
                            .tag file')

        mgr = ReadManager(info, signal, tags)

        F_samp = float(mgr.get_param("sampling_frequency"))
        channels_names = mgr.get_param("channels_names")
        syg = mgr.get_samples() * 0.0715
        tags = mgr.get_tags()

        return syg, F_samp, channels_names, tags
    else:
        raise Exception('To load a signal, tags with metadata OR signal \
                        type with F_samp are required')
