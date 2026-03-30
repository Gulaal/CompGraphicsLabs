import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np

def draw_circle(radius: int, center: tuple[int, int], num_points: int):
    xc, yc = center
    angles = np.linspace(0, 2*np.pi, num_points)
    xs = xc + radius * np.cos(angles)
    ys = yc + radius * np.sin(angles)
    plt.plot(xs, ys)

def bresenham_circle(radius: int, center: tuple[int, int]) -> plt:
    
    draw_circle(radius, center, 100)

    xc, yc = center
    x, y = 0, radius
    d0 = 3 - 2 * y

    while x <= y:

        plt.scatter(xc + x, yc + y, color='red')
        plt.scatter(xc + y, yc + x, color='red')

        plt.scatter(xc - x, yc + y, color='red')
        plt.scatter(xc - y, yc + x, color='red')

        plt.scatter(xc + x, yc - y, color='red')
        plt.scatter(xc + y, yc - x, color='red')

        plt.scatter(xc - x, yc - y, color='red')
        plt.scatter(xc - y, yc - x, color='red')

        if d0 <= 0:
            x += 1
            d0 = d0 + 4 * x + 6
        else:
            x += 1
            y -= 1
            d0 = d0 + 4 * (x - y) + 10

    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(1))
    plt.grid(True, linestyle='--', alpha=0.5)

    return plt
