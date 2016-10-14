import skimage.io as io
from skimage.color import rgb2gray

name = 'baboon.png'
img = io.imread(name)
img_grayscale = rgb2gray(img)
io.imsave('baboon_gs.png',img_grayscale)
show_grayscale = io.imshow(img_grayscale)
io.show()
