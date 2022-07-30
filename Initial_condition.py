import numpy as np
from Parameters import *

def IC():   
    # 1. Box-shaped packet 
    # IC = np.zeros(nx)
    # IC[nx//2-10:nx//2+10] = 1.        #IC
    
    # 2. Gaussian
    if dim.lower() == '2d':
        array = np.linspace(0, nx, num = int(nx))
        x = np.copy(array)
        y = np.copy(array)
        X, Y = np.meshgrid(x, y)
        IC = np.exp(-8e-4*(X-nx/2)**2-8e-4*(Y-ny/2)**2)
    
    if dim.lower() == '1d':
        x = np.linspace(0, nx, num = int(nx))
        IC = np.exp(-8e-4*(x-nx/2)**2)
    
    # 3. Sinusodal shape packet
    # IC = np.zeros(nx)
    # IC[nx//2-10:nx//2+10] = np.cos(np.linspace(-1., 1., 20))   
    return IC