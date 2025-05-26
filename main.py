import os
import numpy as np
from PIL import Image
from random import choice
import matplotlib.pyplot as plt 


def get_pixel(img):
    img.show()  # show the image
    return np.asarray(image)  # return image as pixel array


def global_centering(pixel):
    mean = pixel.mean()
    print('Before Global Centering')
    print('\tMean = %.3f' % mean)
    print('\tMin = %.3f\n\tMax = %.3f' % (pixel.min(), pixel.max()))
    pixel = pixel - mean  # global centering of pixels
    # confirm it had the desired effect
    mean = pixel.mean()
    print('\nAfter Global Centering')
    print('\tMean = %.3f' % mean)
    print('\tMin = %.3f\n\tMax = %.3f' % (pixel.min(), pixel.max()))
    return pixel


def pixel_normalize(pixel):
    # confirm pixel range is 0-255
    print('----------------------------\nBefore Normalization')
    print('\tMean = ', round(pixel.mean(), 3))
    print('\tMin = %.3f\n\tMax = %.3f' % (pixel.min(), pixel.max()))
    pixel = pixel.astype('float32')  # convert from integers to floats
    pixel /= 255.0  # normalize to the range 0-1
    print('\nAfter Normalization')
    print('\tMean = ', round(pixel.mean(), 3))
    # confirm the normalization
    print('\tMin = %.3f\n\tMax = %.3f' % (pixel.min(), pixel.max()))
    return pixel


def visualize(pixel):
    fig, (ax0, ax1) = plt.subplots(1, 2)
    ax0.imshow(image)
    ax0.axis('off')
    ax0.set_title('Original Image')
    ax1.imshow(pixel)
    ax1.axis('off')
    ax1.set_title('Processed Image')
    plt.show()


path = r'C:\Users\Dell\OneDrive\Desktop\Glaucoma\Glaucoma-detection-main\data\Fundus_Train_Val_Data\Fundus_Scanes_Sorted\Train\Glaucoma_Positive\\'
image = Image.open(f'{path}{choice(os.listdir(path))}')
image_pixel = get_pixel(image)
image_pixel = global_centering(image_pixel)
image_pixel = pixel_normalize(image_pixel)
visualize(image_pixel)
