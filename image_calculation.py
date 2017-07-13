from skimage import io
import math
import numpy as np


class ImageDigitalExpress(object):
    def __init__(self, image_path):
        self._image_path = image_path
        
#   calculate an image mean and variance , return a tuple 

    def image_mean_variance(self):
        summary = 0
        diff_sum = 0
        img = io.imread(self._image_path, as_grey=True)
        row = len(img)
        column = len(img[0])

        for i in range(column):
            for n in range(column):
                summary += img[i][n]
        mean = summary / (row*column)

        for a in range(row):
            for b in range(column):
                diff_sum += (img[a][b] - mean) ** 2

        variance = math.sqrt(diff_sum / (row * column))
        return mean, variance
    
# calculate an image information entropy 

    def image_infoentropy(self):
        img = io.imread(self._image_path, as_grey=True)
        img_size = img.size
        hist = np.histogram(img, bins=256)[0] / img_size
        hist_list = list(hist)
        num = 0

        for i in range(len(hist_list)):
            if hist_list[i] == 0:
                num += 1

        for n in range(num):
            hist_list.remove(0)

        sum_num = len(hist_list)
        add_sum = 0

        for k in range(sum_num):
            add_sum += hist_list[k] * math.log(hist_list[k], 2)

        img_entropy = -add_sum
        return img_entropy


















