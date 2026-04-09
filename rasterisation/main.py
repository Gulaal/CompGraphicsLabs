from bresenham_line import bresenham_line
from bresenham_circle import draw_circle, bresenham_circle
import matplotlib.pyplot as plt

def main():
    
    bresenham_circle(10, (0,0))
    # bresenham_line((-5, -1),(-7,-7))
    plt.grid(True)
    plt.axis('equal')
    plt.show()


if __name__ == "__main__":
    main()