from obci_readmanager.signal_processing.read_manager import ReadManager

def emg_montage(syg):
    left_hand = (syg[:, 0] - syg[:, 1])
    right_hand = syg[:, 2] - syg[:, 3]
    
    return left_hand, right_hand
