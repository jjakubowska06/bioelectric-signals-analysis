from bioesa.ecg_analysis import find_hrv, find_heart_rate
import pytest
import numpy as np


@pytest.mark.parametrize("V, fs", [(np.ones(120), 2)])
def test_heart_rate(V, fs):
    hr = find_heart_rate(V, fs)
    assert np.mean(hr) == 0


@pytest.mark.parametrize("V, F_samp", [('V', 128.)])
def test_find_hrv(V, F_samp):
    with pytest.raises(ValueError):
        *hrv, = find_hrv(V, F_samp)
