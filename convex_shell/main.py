import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time

def read_data():
    return pd.read_csv("convex_shell\\points.csv")

def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def redraw(fig, ax, pts, lower_chain, upper_chain, current_p, stage_name):
    ax.clear()
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.set_title(f"Алгоритм Эндрю: {stage_name}", fontsize=12)
    
    xs, ys = zip(*pts)
    ax.scatter(xs, ys, color='gray', label='Все точки')
    for p in pts:
        ax.text(p[0]+0.1, p[1]+0.1, f"({p[0]},{p[1]})", fontsize=8, color='gray')

    if current_p:
        ax.scatter(current_p[0], current_p[1], color='red', label='Текущая точка')
        

    if len(lower_chain) > 0:
        lx, ly = zip(*lower_chain)
        ax.plot(lx, ly, color='green', linewidth=2, marker='o', label='Нижняя цепь')

    if len(upper_chain) > 0:
        ux, uy = zip(*upper_chain)
        ax.plot(ux, uy, color='blue', linewidth=2, marker='o', label='Верхняя цепь')
        
    ax.legend(loc='upper left')
    fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(0.8)

def visualize_andrew(points_df):
    pts = sorted(list(set(tuple(x) for x in points_df.values)))
    
    plt.ion()
    fig, ax = plt.subplots(figsize=(8, 6))

    lower = []
    for p in pts:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
            redraw(fig, ax, pts, lower, [], p, "Удаление точки (правый поворот в нижней цепи)")
        lower.append(p)
        redraw(fig, ax, pts, lower, [], p, "Добавление точки в нижнюю цепь")

    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
            redraw(fig, ax, pts, lower, upper, p, "Удаление точки (правый поворот в верхней цепи)")
        upper.append(p)
        redraw(fig, ax, pts, lower, upper, p, "Добавление точки в верхнюю цепь")

    plt.ioff()
    final_hull = lower[:-1] + upper[:-1]
    final_hull.append(final_hull[0])
    
    ax.clear()
    ax.grid(True)
    ax.set_title("Алгоритм Эндрю: Выпуклая оболочка построена!", fontsize=12, fontweight='bold')
    xs, ys = zip(*pts)
    ax.scatter(xs, ys, color='black', s=80, zorder=2)
    
    hx, hy = zip(*final_hull)
    ax.plot(hx, hy, color='purple', linewidth=3, marker='o', label='Итоговая оболочка')
    ax.legend()
    plt.show()

if __name__ == "__main__":
    points = read_data()
    visualize_andrew(points)
