def emg_montage(syg):
    '''
    A function to montage emg signal (syg), respectivly to hand leads
    '''

    left_hand = syg[0, :] - syg[1, :]
    right_hand = syg[2, :] - syg[3, :]

    return left_hand, right_hand
