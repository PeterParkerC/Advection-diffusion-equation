import os
import cv2
from Parameters import *

def make_movie():
    images = [img for img in sorted(os.listdir(fig_folder)) if img.endswith(".png")]
    frame = cv2.imread(os.path.join(fig_folder, images[0]))
    height, width, layers = frame.shape

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(movie_name, fourcc, 20, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(fig_folder, image)))

    cv2.destroyAllWindows()
    video.release()
