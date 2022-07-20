# Algoritmo 1

from hashlib import new
from itertools import product

from PIL import Image
from cv2 import COLOR_BGR2GRAY, cvtColor, imread, imshow, threshold, waitKey
from numpy import dot, exp, mgrid, pi, ravel, square, uint8, zeros
import math
import cv2
import numpy as np
import numpy

from matplotlib.image import imread
import matplotlib.pyplot as plt

def fig2img(fig):
    import io
    buf = io.BytesIO()
    fig.savefig(buf)
    buf.seek(0)
    img = Image.open(buf)
    return img

# k_size é o do kernel
# sigma é a raiz quadrada das dimensões
# o kernel é uma matriz que possui um centro
def gen_gaussian_kernel(k, sigma):
    center = k // 2
    x, y = mgrid[0 - center : k - center, 0 - center : k - center]
    g = 1 / (2 * pi * sigma) * exp(-(square(x) + square(y)) / (2 * square(sigma)))
    return g

# aplicação do filtro gaussiano na imagem
# no filtro, a matriz da imagem é percorrida passando o centro do kernel pelo
# centro do pixel
def gaussian_filter(image, k, sigma):
    height, width = image.shape[0], image.shape[1]
    dst_height = height - k + 1
    dst_width = width - k + 1

    image_array = zeros((dst_height * dst_width, k * k))
    row = 0
    for i, j in product(range(dst_height), range(dst_width)):
        window = ravel(image[i : i + k, j : j + k])
        image_array[row, :] = window
        row += 1

    gaussian_kernel = gen_gaussian_kernel(k, sigma)
    filter_array = ravel(gaussian_kernel)

    dst = dot(image_array, filter_array).reshape(dst_height, dst_width).astype(uint8)

    return dst

if __name__ == "__main__":
    img = imread(r"image.jpg")
    img = cvtColor(img, COLOR_BGR2GRAY)
    gaussian = gaussian_filter(img, 3, sigma=1)

    matrixA = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
    matrixB = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) 
    
    imgA = Image.fromarray(matrixA)
    pixels = imgA.load()
    width, height = imgA.size

    for x in range(width - 1):
        for y in range(height - 1):
            imgA.putpixel((x, y), pixels[x, y]**2)

    imgB = Image.fromarray(matrixB)
    pixels = imgB.load()
    width, height = imgB.size

    for x in range(width - 1):
        for y in range(height - 1):
            imgB.putpixel((x, y), pixels[x, y]**2)

    # imgB.show()

    im_npA = np.asarray(imgA)
    im_npB = np.asarray(imgB)

    imgC = Image.fromarray(numpy.add(im_npA, im_npB))
    pixels = imgC.load()
    width, height = imgC.size

    threshold_n = 5000.0

    for x in range(width - 1):
        for y in range(height - 1):
            if pixels[x, y] < threshold_n:
                imgC.putpixel((x, y), 0)
            else:
                imgC.putpixel((x, y), 100)

    imgC.show()

    cv2.waitKey(0)