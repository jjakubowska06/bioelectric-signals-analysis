import numpy as np


def extract_tags_timestamps(tags, F_samp):

    '''
    Tags timestamp extraction
    '''

    tags_names = np.unique([d['name'] for d in tags])

    tags_timestamp = dict()

    for name in tags_names:
        tags_timestamp[name] = []

    for i, tag in enumerate(tags):
        if i == len(tags) - 1:
            break
        tmp = tag['start_timestamp']
        start = int((tmp - 4.0)*F_samp)
        stop = int((tmp + 6.0)*F_samp)

        tags_timestamp[tag['name']].append([start, stop])

    return tags_timestamp


def cut_tags_from_timestamp(syg, tags, F_samp):
    '''
    Function to cut fragments form signal indicated
    by tags collected during procedure
    '''
    tags_timestamp = extract_tags_timestamps(tags, F_samp)
    tags_names = list(tags_timestamp.keys())

    tags_signal = {}

    for id in range(len(tags_names)):
        tags_signal[tags_names[id]] = []

        for ts in tags_timestamp[tags_names[id]]:
            tags_signal[tags_names[id]].append(syg[ts[0]:ts[1]])

    return tags_names, tags_signal
