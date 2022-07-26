import numpy as np
from Parameters import *

def IC():
    IC = np.zeros(nx)                 #IC initialize
    
    # 1. A box-shaped packet located at the center
    IC[nx//2-10:nx//2+10] = 1.        #IC
    
    # 2. A bell-shaped packet located at the center
    # x = np.linspace(0, nx, num = int(nx))
    # IC = np.exp(-8e-4*(x-nx/2)**2)
    
    # 3. A sinusodal shape packet
    # IC[nx//2-10:nx//2+10] = np.cos(np.linspace(-1., 1., 20))   
    return IC