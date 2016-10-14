from skimage import data,io,filter

# Sobel does not work with 3D image. So we had to take the 2D version of
# baboon image.

name = 'baboon_gs.png'

img = io.imread(name)

# applying filter
edge = filter.sobel(img)

# Saving the image
io.imsave("baboon_sobel.png",edge)

# Showing the image
io.imshow(edge)
io.show()
