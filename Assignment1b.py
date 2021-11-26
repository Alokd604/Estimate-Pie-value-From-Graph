import numpy as np
import matplotlib.pyplot as plt
import math
np.random.seed(0)

xmin = -2
ymin = -2
xmax = 3
ymax = 4

n = 1000
hit = 0

hit_x = []
hit_y = []

miss_x = []
miss_y = []

for i in range(n):
    x = np.random.uniform(low=xmin, high=xmax)
    y = np.random.uniform(low=ymin, high=ymax)

    # Hit condition
    if x**2+y**2 <= 4:
        hit += 1
        hit_x.append(x)
        hit_y.append(y)
    else:
        miss_x.append(x)
        miss_y.append(y)
p1 = [-2,-2]
p2 = [3,-2]
width= math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
# print(width)
p1 = [-2,-2]
p2 = [-2,4]
height = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
# print(height)

est_pi=((height*width)*hit)/(n*(2**2))
print(est_pi)
plt.scatter(hit_x, hit_y, c='green')
plt.scatter(miss_x, miss_y,c="white")
plt.show()