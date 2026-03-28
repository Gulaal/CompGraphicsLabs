import matplotlib.pyplot as plt

def draw_line(xs: tuple[int, int], ys: tuple[int, int], plot: plt):
    plot.plot(xs, ys)

def bresenham_line(first_point: tuple[int, int], second_point: tuple[int, int]) -> plt:
    xs = (first_point[0], second_point[0])
    ys = (first_point[1], second_point[1])
    draw_line(xs, ys, plt)

    dx = abs(xs[1] - xs[0])
    dy = abs(ys[1] - ys[0])
    sigx = 1 if xs[0] < xs[1] else -1
    sigy = 1 if ys[0] < ys[1] else -1
    err = dx - dy
    x, y = xs[0], ys[0]
    while True:
        plt.scatter(x, y, color='red')
        if x == xs[1] and y == ys[1]:
            break
        err2 = err * 2
        if err2 > -dy:
            err -= dy
            x += sigx
        if err2 < dx:
            err += dx
            y += sigy
    return plt