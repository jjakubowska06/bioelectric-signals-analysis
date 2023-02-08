from bioesa.preprocessing import load_signal, filter_signal
import pytest


@pytest.mark.parametrize("syg, info", [('../data/eeg_data/eeg_alfa.raw', 
                        '../data/eeg_data/eeg_alfa.xml')])
def test_load_signal(syg, info):
    with pytest.raises(Exception):
        s, *params = load_signal(syg, info)


@pytest.mark.parametrize("s, fs, n", [('../data/emg_data/emg.raw', 200, 5.5)])
def test_load_raw(s, fs, n):
    with pytest.raises(Exception):
        s, *params = load_signal(s, fs, n)


@pytest.mark.parametrize("syg, F_samp", [('signal', 128.)])
def test_filter_signal(syg, F_samp):
    with pytest.raises(IndexError):
        filter_signal(syg, F_samp)
