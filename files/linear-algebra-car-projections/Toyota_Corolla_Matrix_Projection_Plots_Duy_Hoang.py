import numpy as np
import matplotlib.pyplot as plt
from math import cos, sin, radians, pi

# points are in format [x, y, z, w] where w=1 for homogeneous coordinates

corolla_pts = np.array([
    [-6.5, -6.5, -6.5, -6.5, -2.5, -2.5, -0.75, -0.75, 3.25, 3.25, 4.5, 4.5, 6.5, 6.5, 6.5, 6.5],
    [-2, -2, 0.5, 0.5, 0.5, 0.5, 2, 2, 2, 2, 0.5, 0.5, 0.5, 0.5, -2, -2],
    [-2.5, 2.5, 2.5, -2.5, -2.5, 2.5, -2.5, 2.5, -2.5, 2.5, -2.5, 2.5, -2.5, 2.5, 2.5, -2.5],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])

# This matrix defines which points are connected
connections = np.array([
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]
])


class MatrixTransformations:
    @staticmethod
    def get_persp_matrix(eye_x, eye_y, eye_z):
        return np.array([
            [1, 0, -eye_x / eye_z, 0],
            [0, 1, -eye_y / eye_z, 0],
            [0, 0, 0, 0],
            [0, 0, -1 / eye_z, 1]
        ])

    @staticmethod
    def get_y_rotation(angle_deg):
        theta = angle_deg * pi / 180 
        return np.array([
            [cos(theta), 0, sin(theta), 0],
            [0, 1, 0, 0],
            [-sin(theta), 0, cos(theta), 0],
            [0, 0, 0, 1]
        ])

    @staticmethod
    def get_z_rotation(angle_deg):
        theta = radians(angle_deg)
        return np.array([
            [cos(theta), -sin(theta), 0, 0],
            [sin(theta), cos(theta), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

    @staticmethod
    def zoom(scale_factor):
        zoom_mtx = np.array([
            [scale_factor, 0, 0, 0],
            [0, scale_factor, 0, 0],
            [0, 0, scale_factor, 0],
            [0, 0, 0, 1]
        ])
        return zoom_mtx

def visualize_proj(transformed_pts, connection_matrix, plot_title="Car Projection",
                   point_color='blue', line_color='darkblue', bg_color='#f0f0f8'):
    x_coords, y_coords = transformed_pts[0], transformed_pts[1]

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)

    for i in range(len(x_coords)):
        for j in range(len(x_coords)):
            if connection_matrix[i][j] == 1:
                ax.plot([x_coords[i], x_coords[j]], [y_coords[i], y_coords[j]],
                        color=line_color, linewidth=1.5)

    ax.scatter(x_coords, y_coords, color=point_color, s=30, zorder=5)

    ax.set_facecolor(bg_color)
    ax.set_title(plot_title, fontsize=14)
    ax.set_xlabel('X-axis projection')
    ax.set_ylabel('Y-axis projection')
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.set_aspect('equal')

    plt.figtext(0.02, 0.02, "AMAT 240 - Duy Hoang", fontsize=8)

    plt.tight_layout()
    plt.show()


def apply_transformations(points, transform_matrix, eye_pos):
    b, c, d = eye_pos

    # First apply the transformation matrix (rotation, scaling, etc)
    transformed = transform_matrix @ points

    #Then apply the perspective projection
    projection_matrix = MatrixTransformations.get_persp_matrix(b, c, d)
    projected = projection_matrix @ transformed

    # Normalize the homogeneous coordinates
    for i in range(projected.shape[1]):
        projected[:, i] = projected[:, i] / projected[3, i]

    return projected

results = {}

# Q1: Projection from eye position (-5, 10, 10)
eye_pos1 = (-5, 10, 10)
identity = np.identity(4)  # no transformation, just projection
projected1 = apply_transformations(corolla_pts, identity, eye_pos1)
visualize_proj(projected1, connections, "Q1: Perspective from left-rear elevated position (-5, 10, 10)")
results["q1"] = projected1

# Q2: Projection from eye position (0, 10, 25)
eye_pos2 = (0, 10, 25)
projected2 = apply_transformations(corolla_pts, identity, eye_pos2)
visualize_proj(projected2, connections,
               "Q2: Perspective from behind and above (0, 10, 25)",
               point_color='darkred', line_color='red')
results["q2"] = projected2

# Q3: Rotate 30° about Y-axis, then project from (0, 10, 25)
transform_y = MatrixTransformations.get_y_rotation(30)
projected3 = apply_transformations(corolla_pts, transform_y, eye_pos2)
visualize_proj(projected3, connections,
               "Q3: 30° Y-rotation + projection from (0, 10, 25)",
               point_color='darkgreen', line_color='green')
results["q3"] = projected3

# Q4: Rotate 45° about Z-axis, then project from (0, 10, 25)
transform_z = MatrixTransformations.get_z_rotation(45)
projected4 = apply_transformations(corolla_pts, transform_z, eye_pos2)
visualize_proj(projected4, connections,
               "Q4: 45° Z-rotation + projection from (0, 10, 25)",
               point_color='purple', line_color='darkviolet')
results["q4"] = projected4

# Q5: Zoom 150% (scale by 1.5), then project from (0, 10, 25)
transform_zoom = MatrixTransformations.zoom(1.5)
projected5 = apply_transformations(corolla_pts, transform_zoom, eye_pos2)
visualize_proj(projected5, connections,
               "Q5: 150% Zoom + projection from (0, 10, 25)",
               point_color='darkorange', line_color='orange')
results["q5"] = projected5
