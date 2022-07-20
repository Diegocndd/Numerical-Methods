# Algoritmo 2

from itertools import product

from PIL import Image
from cv2 import COLOR_BGR2GRAY, cvtColor, imread, imshow, waitKey
from numpy import dot, exp, mgrid, pi, ravel, square, uint8, zeros
import math
import cv2
import numpy as np
import numpy

def gen_gaussian_kernel(k_size, sigma):
    center = k_size // 2
    x, y = mgrid[0 - center : k_size - center, 0 - center : k_size - center]
    g = 1 / (2 * pi * sigma) * exp(-(square(x) + square(y)) / (2 * square(sigma)))
    return g

def laplace(gray_img, sigma=1., kappa=0.75, pad=False):
    assert len(gray_img.shape) == 2
    img = cv2.GaussianBlur(gray_img, (0, 0), sigma) if 0. < sigma else gray_img
    img = cv2.Laplacian(img, cv2.CV_64F)
    rows, cols = img.shape[:2]
    min_map = np.minimum.reduce(list(img[r:rows-2+r, c:cols-2+c]
                                     for r in range(3) for c in range(3)))
    max_map = np.maximum.reduce(list(img[r:rows-2+r, c:cols-2+c]
                                     for r in range(3) for c in range(3)))

    pos_img = 0 < img[1:rows-1, 1:cols-1]

    neg_min = min_map < 0
    neg_min[1 - pos_img] = 0

    pos_max = 0 < max_map
    pos_max[pos_img] = 0

    zero_cross = neg_min + pos_max

    value_scale = 255. / max(1., img.max() - img.min())
    values = value_scale * (max_map - min_map)
    values[1 - zero_cross] = 0.

    if 0. <= kappa:
        thresh = float(np.absolute(img).mean()) * kappa
        values[values < thresh] = 0.
    log_img = values.astype(np.uint8)
    if pad:
        log_img = np.pad(log_img, pad_width=1, mode='constant', constant_values=0)
    return log_img

def gaussian_filter(image, k_size, sigma):
    height, width = image.shape[0], image.shape[1]
    dst_height = height - k_size + 1
    dst_width = width - k_size + 1

    image_array = zeros((dst_height * dst_width, k_size * k_size))
    row = 0
    for i, j in product(range(dst_height), range(dst_width)):
        window = ravel(image[i : i + k_size, j : j + k_size])
        image_array[row, :] = window
        row += 1

    gaussian_kernel = gen_gaussian_kernel(k_size, sigma)
    filter_array = ravel(gaussian_kernel)

    dst = dot(image_array, filter_array).reshape(dst_height, dst_width).astype(uint8)

    return dst

if __name__ == "__main__":
    img = imread(r"image.jpg")
    img = cvtColor(img, COLOR_BGR2GRAY)
    gaussian = gaussian_filter(img, 3, sigma=1)

    log = laplace(gaussian)

    img = Image.fromarray(log)
    pixels = img.load()
    width, height = img.size

    for x in range(width - 1):
        for y in range(height - 1):
            if pixels[x, y] == 0:
                img.putpixel((x, y), 1)
            else:
                img.putpixel((x, y), 100)


    img.show()

    cv2.waitKey(0)