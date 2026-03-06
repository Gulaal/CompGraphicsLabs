import numpy as np
from vispy import plot as plt
from calculations import task1, task2, task3, task4

def vispy_task1_plt(first_point: tuple, second_point: tuple):
    """y = kx + b"""
    k, b = task1(first_point, second_point)
    x = np.linspace(-10, 10, 100)
    y = k * x + b
    fig = plt.Fig(size=(800,800))
    ax = fig[0,0]
    ax.plot((x,y))
    fig.show(run=True)

def vispy_task2_plt(first_point: tuple, second_point: tuple, third_point: tuple):
    line_x = (first_point[0], second_point[0])
    line_y = (first_point[1], second_point[1])
    print(task2(first_point, second_point, third_point))

    fig = plt.Fig(bgcolor='white')

    ax = fig[0,0]
    ax.plot((line_x, line_y))
    ax.plot(third_point, color='white')

    fig.show(run=True)