from skimage import io
import math
import numpy as np
import os

#  calculate the cluster centers and radius of image dataset 
def cluster_center_radius(path):
    name_list = os.listdir(path)
    mean_list = []
    variance_list = []
    cluster_center_x = 0
    cluster_center_y = 0
    eu_dist_sum = 0

    for i in range(len(name_list)):

        img_path = os.path.join(path, name_list[i])
        img = io.imread(img_path, as_grey=True)
        row = len(img)
        column = len(img[0])
        summary = 0
        diff_sum = 0
        
        for c in range(row):
            for n in range(column):
                summary += img[c][n]
        mean = summary / (row * column)
        mean_list.append(mean)
        
        for a in range(row):
            for b in range(column):
                diff_sum += (img[a][b] - mean) ** 2
        variance = math.sqrt(diff_sum / (row * column))
        variance_list.append(variance)
        
 # cluster centers
    for k in range(len(name_list)):
        cluster_center_x += mean_list[k]
        cluster_center_y += variance_list[k]
    x_mean = cluster_center_x / len(name_list)
    y_mean = cluster_center_y / len(name_list)
    cluster_center = np.array([x_mean, y_mean])
    
# euclidean distance
    for p in range(len(name_list)):
        eu_dist = math.sqrt((mean_list[p] - x_mean) ** 2 + (variance_list[p] - y_mean) ** 2)
        eu_dist_sum += eu_dist
# cluster radius
    cluster_r = eu_dist_sum / len(name_list)
    return cluster_center, cluster_r




