import numpy as np # Numpy is a library for working with Arrays
import matplotlib.pyplot as plt # Matplotlib is a plotting library
from PIL import Image # PIL is the Python Imaging Library

pic = Image.open('Numpy/00-puppy.jpg')

# print(type(pic))

# Image._show(pic)

# convert the image to a numpy array
pic_arr = np.asarray(pic)

# print(type(pic_arr))

# show the shape of the numpy array
# Create a figure with multiple subplots
fig, axs = plt.subplots(2, 2, figsize=(16, 8))

# Display each color channel separately
axs[0,0].imshow(pic_arr[:, :, 0], cmap='gray')
axs[0,0].set_title('Red Channel')

axs[0,1].imshow(pic_arr[:, :, 1], cmap='gray')
axs[0,1].set_title('Green Channel')

axs[1,0].imshow(pic_arr[:, :, 2], cmap='gray')
axs[1,0].set_title('Blue Channel')

pic_red = pic_arr.copy()

# Zero out the green and blue channels
pic_red[:, :, 1] = 0
pic_red[:, :, 2] = 0

axs[1,1].imshow(pic_red)
axs[1,1].set_title('Red Channel Only')

# Remove the axes for clarity
# for ax in axs:
#     ax.axis('off')

#remove the x and y ticks
for ax in axs.flat:
    ax.set(xticks=[], yticks=[])

# Display the figure
plt.show()






