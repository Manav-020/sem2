import numpy as np

def cartesian(points):
    x, y = points[:, 0], points[:, 1]
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    return np.column_stack((r, theta))

n=int(input("enter numeber of inputs you want to generate:"))
cartesian_points = np.random.rand(n, 2) * 20 - 10 


polar= cartesian(cartesian_points)

print("Cartesian Points:")
print(cartesian_points)
print("\nPolar Points:")
print(polar)
