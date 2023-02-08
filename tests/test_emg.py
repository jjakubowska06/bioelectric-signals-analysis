from bioesa.emg_analysis import emg_montage
import pytest
import numpy as np


@pytest.mark.parametrize("V", [np.ones(120)])
def test_emg_montage(V):
    with pytest.raises(IndexError):
        emg = emg_montage(V)
