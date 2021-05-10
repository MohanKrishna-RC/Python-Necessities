#import PIL and numpy
from PIL import Image
import numpy as np

#open images by providing path of images
img1 = Image.open("")
img2 = Imgae.open("")

#create arrays of above images
img1_array = np.array(img1)
img2_array = np.array(img2)

# collage of 2 images
#arrange arrays of two images in a single row
imgg = np.hstack([img1_array,img2_array])

#create image of imgg array
final_img = Image.fromarray(imgg)

#provide the path with name for finalizing where you want to save it
final_img.save("")
print("Image saved")