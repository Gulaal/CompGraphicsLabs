from bresenham_line import bresenham_line
from bresenham_circle import draw_circle, bresenham_circle

def main():
    plot = bresenham_circle(10, (0, 0))
    plot.grid(True)
    plot.axis('equal')
    plot.show()


if __name__ == "__main__":
    main()