import os
global nx, ny, dx, dy, dt, n_total, out_step, D, cx, cy, path, save_fig, scheme, BC_method, movie_name, fig_folder
nx = 601                # number of grid points
ny = 601                # number of grid points
dx = 1000.0             # grid spacing = 1km
dy = 1000.0             # grid spacing = 1km
dt = 30.0               # time interval = 30 second
n_total = 3000          # final time step
out_step = 30           # number of time steps between output
                        # output is written every 30s x 50 = 25 mins
D = 1000.               # diffustion constant
cx = 15.                # propagation speed > 0 (upwind) 
cy = 15.
path = 'figs'
BC_method = 'periodic'
scheme = 'FTBS'
save_fig = True
movie_name = 'movie_3d.mp4v'
fig_folder = 'figs'