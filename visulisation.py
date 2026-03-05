from calculations import task1, task2, task3, task4
import matplotlib.pyplot as plt
import matplotlib.backend_bases as bb
import numpy as np

def task1_plt(first_point: tuple, second_point: tuple):
    """y = kx + b"""
    k, b = task1(first_point, second_point)
    x = np.linspace(-10, 10, 100)
    y = k * x + b

    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')

    plt.plot(x, y)

    plt.show()

def task2_plt(first_point: tuple, second_point: tuple, third_point):
    line_x = (first_point[0], second_point[0])
    line_y = (first_point[1], second_point[1])
    print(task2(first_point, second_point, third_point))
    
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')

    plt.plot(line_x, line_y)
    plt.scatter(third_point[0], third_point[1], color="red")
    
    plt.show()

def task3_plt(first_point: tuple, second_point: tuple, third_point):
    print(angle := task3(first_point, second_point, third_point))
    line1_x = (first_point[0], second_point[0])
    line1_y = (first_point[1], second_point[1])
    line2_x = (second_point[0], third_point[0])
    line2_y = (second_point[1], third_point[1])

    if angle == 90:
        plt.xlabel(f"Прямой, {angle}")
    elif angle > 90:
        plt.xlabel(f"Тупой, значения acos не определено")
    else:
        plt.xlabel(f"Острый, {angle}")

    plt.plot(line1_x, line1_y, color="red")
    plt.plot(line2_x, line2_y, color="red")

    plt.show()

def task4_plt(first_point: tuple, second_point: tuple, third_point):
    A, B, C, D = task4(first_point,second_point,third_point)

    x = np.linspace(-10, 10, 10)
    y = np.linspace(-10, 10, 10)
    X, Y = np.meshgrid(x,y)
    Z = (A/C)*X + (B/C)*Y + D/C

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    surf = ax.plot_surface(X, Y, Z)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()
