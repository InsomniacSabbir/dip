import skimage.io as io
from skimage.color import rgb2gray 
img = io.imread('baboon.png')
print img.shape
