import numpy as np
from Initial_condition import *
from Parameters import *
from Plotting_tools import *
from Boundary_condition import *

def explicit(IC):                     #explicit scheme / FTBS
    data = np.zeros((n_total, nx, ny))
    u_past = np.zeros((nx, ny))
    u_now = np.zeros((nx, ny))
    u_next = np.zeros((nx, ny))
    sigma_x = cx * dt / dx              #Courant number
    sigma_y = cy * dt / dy
    rho = D * dt / (dx ** 2)          #Fourier number
    print(rho, sigma_x, sigma_y)
    if sigma_x >= 0 :
        for n in range(n_total):
            if n == 0:
                u_next = np.copy(IC())

            else:
                u_next[1:nx-1, 1:ny-1] = u_now[1:nx-1, 1:ny-1] + rho*(u_now[2:nx, 1:ny-1]+u_now[0:nx-2, 1:ny-1]-2*u_now[1:nx-1, 1:ny-1]) - sigma_x*(u_now[1:nx-1, 1:ny-1]-u_now[0:nx-2, 1:ny-1]) - sigma_y*(u_now[1:nx-1, 1:ny-1]-u_now[1:nx-1, 0:ny-2])         #FTBS
                BC(BC_method, u_next, u_now)

            u_past = np.copy(u_now)
            u_now = np.copy(u_next)
            data[n] = np.copy(u_now)  
            plot_n_save(n, data)
    else:
        for n in range(n_total):
            if n == 0:
                u_next = np.copy(IC())

            else:
                u_next[1:nx-1] = u_now[1:nx-1] + rho*(u_now[2:nx]+u_now[0:nx-2]-2*u_now[1:nx-1]) - sigma*(u_now[2:nx]-u_now[1:nx-1])         #FTBS
                BC(BC_method, u_next, u_now)

            u_past = np.copy(u_now)
            u_now = np.copy(u_next)
            data[n] = np.copy(u_now)  
            plot_n_save(n, data)
    # np.savetxt('result.txt', data, fmt = '%.9g')
    
# def explicit(IC):                     #explicit scheme / FTBS
#     data = np.zeros((n_total, nx))
#     u_past = np.zeros(nx)
#     u_now = np.zeros(nx)
#     u_next = np.zeros(nx)
#     sigma = cx * dt / dx              #Courant number
#     rho = D * dt / (dx ** 2)          #Fourier number
#     print(rho, sigma)
#     if sigma >= 0 :
#         for n in range(n_total):
#             if n == 0:
#                 u_next = np.copy(IC())

#             else:
#                 u_next[1:nx-1] = u_now[1:nx-1] + rho*(u_now[2:nx]+u_now[0:nx-2]-2*u_now[1:nx-1]) - sigma*(u_now[1:nx-1]-u_now[0:nx-2])         #FTBS
#                 BC(BC_method, u_next, u_now)

#             u_past = np.copy(u_now)
#             u_now = np.copy(u_next)
#             data[n] = np.copy(u_now)  
#             plot_n_save(n, data)
#     else:
#         for n in range(n_total):
#             if n == 0:
#                 u_next = np.copy(IC())

#             else:
#                 u_next[1:nx-1] = u_now[1:nx-1] + rho*(u_now[2:nx]+u_now[0:nx-2]-2*u_now[1:nx-1]) - sigma*(u_now[2:nx]-u_now[1:nx-1])         #FTBS
#                 BC(BC_method, u_next, u_now)

#             u_past = np.copy(u_now)
#             u_now = np.copy(u_next)
#             data[n] = np.copy(u_now)  
#             plot_n_save(n, data)
#     np.savetxt('result.txt', data, fmt = '%.9g')
        
def inplicit(IC): #under development
    data = np.zeros((n_total, nx))
    u_past = np.zeros(nx)
    u_now = np.zeros(nx)
    u_next = np.zeros(nx)
    sigma = cx * dt / dx               #Courant number
    rho = D * dt / (dx ** 2)           #Fourier number
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