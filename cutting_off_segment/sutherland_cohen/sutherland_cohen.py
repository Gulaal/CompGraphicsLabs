import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def read_data():
    file_path = 'cutting_off_segment\sutherland_cohen\sutherland_cohen_input.csv'
    file_data = pd.read_csv(file_path)
    rect = file_data.iloc[:4]
    line = file_data.iloc[4:]
    print(rect, line, sep='\n')
    return rect, line

def compute_code(point, xmin, xmax, ymin, ymax):
    code = 0
    x = point[0]
    y = point[1]
    if x < xmin:
        code |= 1
    elif x > xmax:
        code |= 2
    if y < ymin:
        code |= 4
    elif y > ymax:
        code |= 8
    return code

def sutherland_cohen(line, xmin, xmax, ymin, ymax):
    x0_curr, y0_curr = line.iloc[0, 0], line.iloc[0, 1]
    x1_curr, y1_curr = line.iloc[1, 0], line.iloc[1, 1]

    while True:
        code_start = compute_code((x0_curr, y0_curr), xmin, xmax, ymin, ymax)
        code_end = compute_code((x1_curr, y1_curr), xmin, xmax, ymin, ymax)
        
        if code_start == 0 and code_end == 0:
            return (x0_curr, y0_curr), (x1_curr, y1_curr), True
        
        if (code_start & code_end) != 0:
            return None, None, False
        
        code_out = code_start if code_start != 0 else code_end

        x = x0_curr
        y = y0_curr

        if abs(x0_curr - x1_curr) < 1e-9:

            if code_out & 8:
                x = x0_curr
                y = ymax
            elif code_out & 4:
                x = x0_curr
                y = ymin
            elif code_out & 2:
                x = xmax
                y = y0_curr
            elif code_out & 1:
                x = xmin
                y = y0_curr

        else:
            k = (y1_curr - y0_curr) / (x1_curr - x0_curr)
            if code_out & 8:
                x = x0_curr + (ymax - y0_curr) / k
                y = ymax
            elif code_out & 4:
                x = x0_curr + (ymin - y0_curr) / k
                y = ymin
            elif code_out & 2:
                y = y0_curr + k * (xmax - x0_curr)
                x = xmax
            elif code_out & 1:
                y = y0_curr + k * (xmin - x0_curr)
                x = xmin
        
        if code_out == code_start:
            x0_curr, y0_curr = x, y
        else:
            x1_curr, y1_curr = x, y

import matplotlib.pyplot as plt

def draw(R, L, result, visible):
    fig, ax = plt.subplots(figsize=(8, 6))

    rect_xs = R['x'].tolist()
    rect_ys = R['y'].tolist()
    rect_xs.append(rect_xs[0])
    rect_ys.append(rect_ys[0])
    ax.fill(rect_xs, rect_ys, alpha=0.3, color='lightblue', edgecolor='blue', linewidth=2, label='Отсекатель')

    line_xs = L['x'].tolist()
    line_ys = L['y'].tolist()
    ax.plot(line_xs, line_ys, 'gray', linestyle='--', linewidth=1.5, label='Исходный отрезок')

    if visible and result is not None:
        (x1, y1), (x2, y2) = result
        ax.plot([x1, x2], [y1, y2], 'red', linewidth=3, label='Отсечённый отрезок')
        ax.plot(x1, y1, 'ro', markersize=8)
        ax.plot(x2, y2, 'ro', markersize=8)
    else:
        ax.text(0.5, 0.5, 'Отрезок полностью не видим',
                transform=ax.transAxes, ha='center', va='center',
                fontsize=12, color='red',
                bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'))

    ax.set_aspect('equal')
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Алгоритм отсечения Сазерленда-Коэна')
    ax.legend(loc='best')
    plt.show()

if __name__ == "__main__":
    R, L = read_data()
    xmin, xmax, ymin, ymax = R.iloc[:, 0].min(), R.iloc[:, 0].max(), R.iloc[:, 1].min(), R.iloc[:, 1].max()
    p1, p2, visible = sutherland_cohen(L, xmin, xmax, ymin, ymax)
    result = (p1, p2) if visible else None
    draw(R, L, result, visible)