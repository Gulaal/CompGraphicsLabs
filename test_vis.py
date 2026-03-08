import numpy as np
import matplotlib.pyplot as plt

def star_points(center=(0, 0), outer_radius=5, inner_radius=2, num_points=5):
    x0, y0 = center
    angles = np.linspace(0, 2*np.pi, 2*num_points, endpoint=False)
    radii = [outer_radius, inner_radius] * num_points
    points = []
    for angle, r in zip(angles, radii):
        x = x0 + r * np.cos(angle)
        y = y0 + r * np.sin(angle)
        points.append([x, y])
    points.append(points[0])
    return np.array(points)

def translation_matrix(tx, ty):
    return np.array([[1, 0, tx], [0, 1, ty], [0, 0, 1]])

def scaling_matrix(sx, sy):
    return np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])

def rotation_matrix(angle):
    c, s = np.cos(angle), np.sin(angle)
    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])

def transform(points, matrix):
    N = points.shape[0]
    ones = np.ones((N, 1))
    points_h = np.hstack([points, ones])
    points_transformed_h = (matrix @ points_h.T).T
    return points_transformed_h[:, :2]

pts = star_points(center=(0, 0), outer_radius=5, inner_radius=2)

R = rotation_matrix(np.pi/4)
pts_rot = transform(pts, R)

S = scaling_matrix(0.5, 1.2)
pts_scale = transform(pts, S)

M = translation_matrix(10, 5) @ scaling_matrix(0.5, 1.2) @ rotation_matrix(np.pi/4)
pts_combined = transform(pts, M)

plt.figure(figsize=(8, 8))
plt.plot(pts[:, 0], pts[:, 1], 'b-', linewidth=2, label='Исходная')
plt.plot(pts_rot[:, 0], pts_rot[:, 1], 'g-', linewidth=2, label='Поворот 45°')
plt.plot(pts_scale[:, 0], pts_scale[:, 1], 'r-', linewidth=2, label='Масштабирование (0.5, 1.2)')
plt.plot(pts_combined[:, 0], pts_combined[:, 1], 'm-', linewidth=2, label='Поворот → масштаб → перенос')
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.title('Аффинные преобразования звезды')
plt.show()