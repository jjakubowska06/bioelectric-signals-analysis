from .cut_tags import cut_tags_from_timestamp
import numpy as np


def evoked_potentials(syg, tags, F_samp):
    '''
    Function for calculating evoked potential for a specific tag
    '''
    tags_names, tags_from_signal = cut_tags_from_timestamp(syg, tags, F_samp)
    tags_values = list(tags_from_signal.values())

    ep = np.zeros((len(tags_names), len(tags_values[0][0])))

    for i, values in enumerate(tags_values):
        ep[i, :] = np.mean(values, axis=0)

    return ep
