from bioesa.eeg_analysis import eeg_montage, evoked_potentials
import pytest
import numpy as np


@pytest.mark.parametrize("syg, type", [(np.ones((5, 20)), 'o2')])
def test_eeg_montage(syg, type):
    with pytest.raises(ValueError):
        eeg = eeg_montage(syg, type)

@pytest.mark.parametrize("V, tags, F_samp", [(np.ones((1, 20)), ['lewa', 'prawa'], 128.)])
def test_evoked_potentials(V, tags, F_samp):
    with pytest.raises(TypeError):
        eps = evoked_potentials(V, tags, F_samp)
