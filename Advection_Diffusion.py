from Parameters import *
from make_movie import *
from Initial_condition import *
from scheme import *

def Advection_Diffusion():
    explicit_scheme = ['FTBS', 'explicit', 'explicit scheme']
    inplicit_scheme = ['CTCS', 'inplicit', 'inplicit scheme']
    if scheme.lower() in explicit_scheme:
        explicit(IC)
    if scheme.lower() in inplicit_scheme:
        inplicit(IC)    
        
    if save_fig:
        make_movie()