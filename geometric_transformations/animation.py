import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from calculations import scaling_matrix

x = np.linspace(-2.5, 2.5, 400)
y = np.linspace(-2.5, 2.5, 400)
X, Y = np.meshgrid(x, y)

coords = np.vstack([X.flatten(), Y.flatten(), np.ones_like(X.flatten())])

fig, ax = plt.subplots(figsize=(8, 8))

def update(frame):
    ax.clear()
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.5, 2.5)
    ax.grid(True, linestyle='--', alpha=0.4)
    s = 1 + 0.4 * np.sin(frame / 100)
    M = scaling_matrix(s, s)
    new_coords = M @ coords
    X_new = new_coords[0].reshape(X.shape)
    Y_new = new_coords[1].reshape(Y.shape)
    Z = (X_new**2 + Y_new**2 - 1)**3 - X_new**2 * Y_new**3
    cont = ax.contour(X, Y, Z, levels=[0], colors='crimson', linewidths=2)
    ax.set_title(f"{s:.2f}")
    return cont,

ani = animation.FuncAnimation(fig, update, frames=60, interval=10, blit=False)
plt.show()