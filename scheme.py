import numpy as np
from Initial_condition import *
from Parameters import *
from Plotting_tools import *
from Boundary_condition import *

def FTBS(IC):
    data = np.zeros((n_total, nx))
    u_past = np.zeros(nx)
    u_now = np.zeros(nx)
    u_next = np.zeros(nx)
    sigma = cx * dt / dx
    rho = D * dt / (dx ** 2)
    print(rho, sigma)
    for n in range(n_total):
        if n == 0:
            u_next = np.copy(IC())
            
        else:
            u_next[1:nx-1] = u_now[1:nx-1] + rho*(u_now[2:nx]+u_now[0:nx-2]-2*u_now[1:nx-1]) - sigma*(u_now[1:nx-1]-u_now[0:nx-2])         #FTBS
            BC(BC_method, u_next, u_now)
            
        u_past = np.copy(u_now)
        u_now = np.copy(u_next)
        data[n] = np.copy(u_now)  
        plot_n_save(n, data)
        
def CTCS(IC):
    data = np.zeros((n_total, nx))
    u_past = np.zeros(nx)
    u_now = np.zeros(nx)
    u_next = np.zeros(nx)
    sigma = cx * dt / dx
    rho = D * dt / (dx ** 2)
    print(rho, sigma)
    for n in range(n_total):
        if n == 0:
            u_next = np.copy(IC())

        elif n == 1:
        #1st step
            u_next[1:nx-1] = u_now[1:nx-1] + rho*(u_now[2:nx]+u_now[0:nx-2]-2*u_now[1:nx-1]) - sigma*(u_now[1:nx-1]-u_now[0:nx-2])         #FTBS
            BC(BC_method, u_next, u_now) 

        else:
            u_next[1:nx-1] = u_past[1:nx-1] + 2.*rho*(u_now[2:nx]-2*u_now[1:nx-1]+u_now[0:nx-2]) - sigma*(u_now[2:nx]-u_now[0:nx-2])       #CTCS
            BC(BC_method, u_next, u_now)

        u_past = np.copy(u_now)
        u_now = np.copy(u_next)
        data[n] = np.copy(u_now)  
        plot_n_save(n, data)
        np.savetxt('result.txt', data, fmt = '%.9g')