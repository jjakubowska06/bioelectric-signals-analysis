import matplotlib.pyplot as plt

#plot montage ogolnie!

def channels_definition(s):
    
    VLR = s[:,0] 
    VPR = s[:,1]
    VLN = s[:,2]

    return VLR, VPR, VLN


def einthoven_montage(s):
    '''
    Odprowadzenie Einthovena

    s: signal, should be filtered beforehand
    '''

    VLR, VPR, VLN = channels_definition(s)

    V1 = VLR-VPR
    V2 = VLN-VPR
    V3= VLN-VLR

    return V1, V2, V3

def plot_einthoven(V1, V2, V3):

    channels = [V1, V2, V3]
    for i in range(3):
        plt.subplot(3, 1, i+1)
        plt.plot(channels[i])
        plt.title('odpr {i}')
    plt.suptitle('Einthoven')
    plt.show()

def goldberg_montage(s):

    VLR, VPR, VLN = channels_definition(s)

    aVl = VLR - (VPR + VLN)/2
    aVr = VPR - (VLR + VLN)/2
    aVn = VLN - (VLR + VPR)/2

    return aVl, aVr, aVn

def plot_goldberg(aVl, aVr, aVn):
    
    channels = [aVl, aVr, aVn]
    for i in range(3):  
        plt.subplot(3, 1, i+1)
        plt.plot(channels[i])
        plt.title('odpr {i}')
    
    plt.suptitle('Goldberg')
    plt.show()