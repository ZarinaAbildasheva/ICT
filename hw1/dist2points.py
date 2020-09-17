av_radius = 6371.01
arr = list(map(float, input().split()))
arr1 = list(map(float, input().split()))
import numpy as np
radians = np.radians(arr)
radians1 = np.radians(arr1)
import math
res = av_radius*(math.acos((math.sin(radians[0])*math.sin(radians1[0]) + (math.cos(radians[0])*math.cos(radians1[0])*math.cos(radians[1]-radians1[1]) ) ) ))
#distance=6371.01×arccos(sin(t1)×sin(t2)+cos(t1)×cos(t2)×cos(g1−g2))
print(res)