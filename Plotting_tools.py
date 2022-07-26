import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from mpl_toolkits.mplot3d import axes3d
from Parameters import *

def plot_n_save(n, data):
    if n%out_step == 0:
        title = str(n).zfill(5)
        filename = os.getcwd() + '\\' + path + '\\' + title + f'.png'
        fig = plt.figure(figsize = (12, 8), dpi = 80)
        
        # Plot a 3D surface
        x = np.arange(0, nx, 1)
        y = np.arange(0, ny, 1)
        X,Y = np.meshgrid(x,y)
        matrix=np.array([data[n] for i in range(601)])
        ax = fig.add_subplot(111, projection='3d')
        ax.set_xlim(0,nx)
        ax.set_ylim(0,ny)
        ax.set_zlim(-0.5,1.5)
        ax.set_xlabel('x (km)', fontsize = 15)
        ax.set_ylabel('y (km)', fontsize = 15)
        ax.set_zlabel('u (mag)', fontsize = 15)
        ax.set_title(title, fontsize = 15)
        ax.plot_surface(X, Y, matrix, cmap='viridis', edgecolor='none')
        # ax = fig.add_subplot()
        # ax.set_xlim(0,600)
        # ax.set_ylim(-0.5,1.5)
        # ax.set_ylabel('u (mag)', fontsize = 15)
        # ax.set_xlabel('x (km)', fontsize = 15)
        # ax.set_title(title, fontsize = 15)
        # ax.set_facecolor('#E6E6E6')        
        # matrix=[data[n] for i in range(50)]
        # ax=sns.heatmap(data=matrix, vmin=0, vmax=1)        
        # sns.lineplot(data = data[n])
        # sns.lineplot(data = data[0])
        if save_fig:
            plt.savefig(filename, dpi = 300)
        else:
            plt.show()
        plt.close()