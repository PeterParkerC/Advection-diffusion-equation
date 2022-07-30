from Parameters import *

def BC(BC_method, u_next, u_now):
    if BC_method.lower() == 'fixed':          #fixed in time boundary condition
        u_next[0] = u_now[0]                  #BC@x=0
        u_next[-1] = u_now[-1]                #BC@x=L
        
    if BC_method.lower() == 'periodic':       #periodic boundary condition
        u_next[0,] = u_next[-2,]                #u_0=u_L-1
        u_next[-1,] = u_next[1]                #u_L=u_1
        u_next[:,0] = u_next[:,-2]                #u_0=u_L-1
        u_next[:,-1] = u_next[:,1]                #u_L=u_1

    if BC_method.lower() == 'absorbing':
        sigma = cx * dt / dx
        if sigma >= 0:
            u_next[0] = u_now[0]
            u_next[-1] = sigma*u_now[-2] + (1-sigma)*u_now[-1]
        
        else:
            u_next[0] = sigma*u_now[1] + (1+sigma)*u_now[0]
            u_next[-1] = u_next[-1]