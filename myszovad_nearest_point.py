"""
Find the nearest point to coord [0,0]
"""
import numpy as np

data = np.loadtxt("points.csv")
euclids_distances = np.linalg.norm(data, axis = 1)
lowest_distance_index = np.argmin(euclids_distances)
nearest_point = data[lowest_distance_index]

print(f"The index of the nearest point to [0,0] is {lowest_distance_index}.")
print(f"The coordinates of the nearest point to [0,0] are {nearest_point}.")
