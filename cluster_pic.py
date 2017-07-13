from skimage import io
import math
import os
import matplotlib.pyplot as plt

# generate the 2D scatter
def cluster(path):
    name_list = os.listdir(path)
    mean_list = []
    variance_list = []
    
# produce the x,y data
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
    return mean_list, variance_list

des1 = 'D:/fonts/class/0/'
des2 = 'D:/fonts/class/1/'
des3 = 'D:/fonts/class/2/'
 
#  plot the x,y scatter
cluster1 = cluster(des1)
plt.scatter(cluster1[0], cluster1[1], c='r')
cluster2 = cluster(des2)
plt.scatter(cluster2[0], cluster2[1], c='b')
cluster3 = cluster(des3)
plt.scatter(cluster3[0], cluster3[1], c='y')
plt.show()


