import numpy as np
from matplotlib import image
import matplotlib.cm as color_map
import matplotlib
import gc


def image_to_mat(image_file, gray_scale=False):
    """
    image_file: str
    gray_scale: Boolean
    returns:
    img: numpy array  
    """
    img = image.imread(image_file)
    # in case of transparency values
    dim = len(img.shape)
    if dim == 3 and img.shape[2] > 3:
        height, width, ch = img.shape
        new_img = np.zeros([height, width, 3])
        for r in range(height):
            for c in range(width):
                new_img[r, c, :] = img[r, c, 0:3]
        img = np.copy(new_img)
    if gray_scale and len(img.shape) == 3:
        height, width = img.shape[0:2]
        new_img = np.zeros([height, width])
        for r in range(height):
            for c in range(width):
                new_img[r, c] = img[r, c, 0]
        img = new_img
    return img


def mat_to_image(image_mat, image_file):
    """
    Convert mat of color/gray_scalecale values to png file.
    image_mat = (color) or (gray-scale) numpy array
    image_file = str
    """
    c_map = None
    if len(image_mat.shape) < 3:
        c_map = color_map.Greys_r
    image.imsave(image_file, image_mat, cmap=c_map)
    del(image_mat)
    gc.collect()


def flatten_input(image_mat):
    """
    Flatten image mat from
    h x w x ch to (h*w) x ch 
    image_mat: multi-dim numpy array of size h x w x ch

    returns: flattened_values 
    image_mat: mult-dim numpy array of size (h*w) x ch 
    """
    if(len(image_mat.shape) == 3):
        height, width, ch = image_mat.shape
    else:
        height, width = image_mat.shape
        ch = 1
    flattened_values = np.zeros([height*width, ch])
    for h, r in enumerate(image_mat):
        for idx, c in enumerate(r):
            flattened_values[h*width + idx, :] = c
    return flattened_values


def unflatten_input(image_mat, width):
    """
    image_mat = (color) or (gray-scale) numpy array (height* width) x ch
    width = int

    returns:
    unflattened_values = (color) or (gray-scale) numpy array of height x width x ch
    """
    height_width = image_mat.shape[0]
    height = int(height_width/width)
    dim = len(image_mat.shape)
    if dim > 1:
        ch = image_mat.shape[-1]
        unflattened_values = np.zeros([height, width, ch])
        for i in range(height):
            for j in range(width):
                unflattened_values[i, j,:] = image_mat[i*width + j,:]
    else:
        ch = 1
        unflattened_values = np.zeros([height, width])
        for i in range(height):
            for j in range(width):
                unflattened_values[i, j] = image_mat[i*width + j]
    return unflattened_values



