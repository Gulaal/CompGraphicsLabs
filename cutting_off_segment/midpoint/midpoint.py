import matplotlib.pyplot as plt
import pandas as pd

def read_data():
    file_path = 'cutting_off_segment/sutherland_cohen/sutherland_cohen_input.csv'
    file_data = pd.read_csv(file_path)
    polygon = file_data.iloc[:-2]
    line = file_data.iloc[-2:]
    return polygon, line

def compute_region_code(x, y, xmin, ymin, xmax, ymax):
    code = 0
    if x < xmin:
        code |= 1
    elif x > xmax:
        code |= 2
    if y < ymin:
        code |= 4
    elif y > ymax:
        code |= 8
    return code

def midpoint_clip(x1, y1, x2, y2, xmin, ymin, xmax, ymax, eps=1e-6):
    
    code1 = compute_region_code(x1, y1, xmin, ymin, xmax, ymax)
    code2 = compute_region_code(x2, y2, xmin, ymin, xmax, ymax)

    if code1 == 0 and code2 == 0:
        return x1, y1, x2, y2, True
    if (code1 & code2) != 0:
        return None, None, None, None, False

    if abs(x2 - x1) < eps and abs(y2 - y1) < eps:
        if code1 == 0:
            return x1, y1, x1, y1, True
        else:
            return None, None, None, None, False

    xm = (x1 + x2) / 2.0
    ym = (y1 + y2) / 2.0

    left = midpoint_clip(x1, y1, xm, ym, xmin, ymin, xmax, ymax, eps)
    right = midpoint_clip(xm, ym, x2, y2, xmin, ymin, xmax, ymax, eps)

    if left[4] and right[4]:
        return left[0], left[1], right[2], right[3], True
    elif left[4]:
        return left[0], left[1], left[2], left[3], True
    elif right[4]:
        return right[0], right[1], right[2], right[3], True
    else:
        return None, None, None, None, False

def plot_clipping(polygon, line, result_midpoint, visible_midpoint):
    fig, ax = plt.subplots(figsize=(8, 8))

    poly_x = polygon.iloc[:, 0].tolist()
    poly_y = polygon.iloc[:, 1].tolist()
    poly_x.append(poly_x[0])
    poly_y.append(poly_y[0])
    ax.fill(poly_x, poly_y, alpha=0.3, color='lightblue', edgecolor='blue', linewidth=2, label='Отсекатель')

    p0 = (line.iloc[0, 0], line.iloc[0, 1])
    p1 = (line.iloc[1, 0], line.iloc[1, 1])
    ax.plot([p0[0], p1[0]], [p0[1], p1[1]], 'gray', linewidth=1.5, label='Исходный отрезок')

    if visible_midpoint and result_midpoint is not None:
        x1, y1, x2, y2 = result_midpoint
        ax.plot([x1, x2], [y1, y2], 'r-', linewidth=3, label='Результат (Midpoint)')
        ax.plot(x1, y1, 'ro', markersize=6)
        ax.plot(x2, y2, 'ro', markersize=6)
    else:
        ax.text(0.5, 0.5, "Отрезок полностью не видим", transform=ax.transAxes,
                ha='center', va='center', fontsize=12, color='red')

    ax.set_aspect('equal')
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.legend()
    ax.set_title("Отсечение отрезка (алгоритм средней точки)")
    plt.show()

if __name__ == "__main__":
    P, L = read_data()

    xmin, xmax = P['x'].min(), P['x'].max()
    ymin, ymax = P['y'].min(), P['y'].max()

    x1, y1 = L.iloc[0, 0], L.iloc[0, 1]
    x2, y2 = L.iloc[1, 0], L.iloc[1, 1]

    res = midpoint_clip(x1, y1, x2, y2, xmin, ymin, xmax, ymax)
    visible = res[4]
    result = (res[0], res[1], res[2], res[3]) if visible else None

    plot_clipping(P, L, result, visible)