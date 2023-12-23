import numpy as np

def calculate_hypervolume(points, reference_point):
    # Sort the points based on the first objective (x-axis)
    points_sorted = points[np.argsort(points[:, 0])]

    # Initialize hypervolume to zero
    volume = 0.0

    # Calculate hypervolume
    for i in range(len(points_sorted)):
        if i == 0:
            # Base case: calculate the volume of the first point
            volume += (reference_point[0] - points_sorted[i][0]) * (reference_point[1] - points_sorted[i][1])
        else:
            # Calculate volume difference between consecutive points
            volume += (points_sorted[i - 1][0] - points_sorted[i][0]) * (reference_point[1] - points_sorted[i][1])

    return volume

# Example points in a 2D space
points = np.array([[4, 3], [2, 6], [8, 1], [4, 8], [7, 5]])

# Reference point (upper bound)
reference_point = [10, 10]

# Calculate hypervolume
hv = calculate_hypervolume(points, reference_point)
print(f"The hypervolume with reference point {reference_point} is: {hv}")
