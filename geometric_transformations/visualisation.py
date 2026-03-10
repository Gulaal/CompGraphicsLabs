import numpy as np
import matplotlib.pyplot as plt
from calculations import *

pts = star_points(center=(0, 0), outer_radius=5, inner_radius=2)
square_pts = bounding_square(pts)

R = rotation_matrix(np.pi/2)
pts = transform(pts, R)
square_pts = transform(square_pts, R)

plt.figure(figsize=(8, 8))
plt.plot(pts[:,0], pts[:,1], color='red')
plt.plot(square_pts[:,0], square_pts[:,1], 'b-')
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.title('Аффинные преобразования звезды')
plt.show()