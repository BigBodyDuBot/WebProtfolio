
import numpy as np
import matplotlib.pyplot as plt
from math import cos, sin, radians

# Data matrix D (homogeneous coordinates)
D = np.array([
    [-6.5, -6.5, -6.5, -6.5, -2.5, -2.5, -0.75, -0.75, 3.25, 3.25, 4.5, 4.5, 6.5, 6.5, 6.5, 6.5],
    [-2, -2, 0.5, 0.5, 0.5, 0.5, 2, 2, 2, 2, 0.5, 0.5, 0.5, 0.5, -2, -2],
    [-2.5, 2.5, 2.5, -2.5, -2.5, 2.5, -2.5, 2.5, -2.5, 2.5, -2.5, 2.5, -2.5, 2.5, 2.5, -2.5],
    [1] * 16
])

# Adjacency matrix C
C = np.array([
    [0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
    [0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0],
    [1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0],
    [0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0],
    [0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0]
])

# Create perspective projection matrix
def perspective_matrix(b, c, d):
    return np.array([
        [1, 0, -b/d, 0],
        [0, 1, -c/d, 0],
        [0, 0, 0,    0],
        [0, 0, -1/d, 1]
    ])

# Create rotation matrices
def rotation_matrix_y(theta_degrees):
    theta = radians(theta_degrees)
    return np.array([
        [cos(theta), 0, sin(theta), 0],
        [0, 1, 0, 0],
        [-sin(theta), 0, cos(theta), 0],
        [0, 0, 0, 1]
    ])

def rotation_matrix_z(theta_degrees):
    theta = radians(theta_degrees)
    return np.array([
        [cos(theta), -sin(theta), 0, 0],
        [sin(theta), cos(theta), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

# Zoom matrix
def zoom_matrix(factor):
    return np.array([
        [factor, 0, 0, 0],
        [0, factor, 0, 0],
        [0, 0, factor, 0],
        [0, 0, 0, 1]
    ])

# Plotting function
def plot_projection(D_transformed, C, title):
    x, y = D_transformed[0], D_transformed[1]
    plt.figure(figsize=(6, 6))
    for i in range(16):
        for j in range(i+1, 16):
            if C[i][j] == 1:
                plt.plot([x[i], x[j]], [y[i], y[j]], 'k-')
    plt.scatter(x, y, c='red')
    plt.title(title)
    plt.axis('equal')
    plt.grid(True)
    plt.show()

# Apply a transformation and perspective projection
def apply_transform_and_project(D, transform, b, c, d):
    T = transform @ D
    P = perspective_matrix(b, c, d)
    PD = P @ T
    PD /= PD[3]
    return PD

# Q1
D1 = apply_transform_and_project(D, np.identity(4), -5, 10, 10)
plot_projection(D1, C, "Q1: Projection from (-5, 10, 10)")

# Q2
D2 = apply_transform_and_project(D, np.identity(4), 0, 10, 25)
plot_projection(D2, C, "Q2: Projection from (0, 10, 25)")

# Q3
Ry30 = rotation_matrix_y(30)
D3 = apply_transform_and_project(D, Ry30, 0, 10, 25)
plot_projection(D3, C, "Q3: Rotate 30° about Y-axis, then project")

# Q4
Rz45 = rotation_matrix_z(45)
D4 = apply_transform_and_project(D, Rz45, 0, 10, 25)
plot_projection(D4, C, "Q4: Rotate 45° about Z-axis, then project")

# Q5
Zoom = zoom_matrix(1.5)
D5 = apply_transform_and_project(D, Zoom, 0, 10, 25)
plot_projection(D5, C, "Q5: Zoom 150%, then project")
