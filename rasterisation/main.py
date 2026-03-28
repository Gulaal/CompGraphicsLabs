from bresenham_line import bresenham_line

def main():
    plot = bresenham_line((1,25), (22,2))
    plot.grid(True)
    plot.show()

if __name__ == "__main__":
    main()