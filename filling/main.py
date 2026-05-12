import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def read_data():
    file_path = "filling\polygon.csv"
    file_data = pd.read_csv(file_path)
    polygon = file_data[:]
    return polygon

def build_edge_table(polygon):
    et = {}
    points = polygon.values.tolist()
    n = len(points)

    for i in range(n):
        p1 = points[i]
        p2 = points[(i + 1) % n]
        if p1[1] == p2[1]:
            continue
        if p1[1] < p2[1]:
            y_min, y_max = int(p1[1]), int(p2[1])
            x_at_y_min = float(p1[0])
        else:
            y_min, y_max = int(p2[1]), int(p1[1])
            x_at_y_min = float(p2[0])
        
        dx = float(p2[0] - p1[0]) / float(p2[1] - p1[1])
        edge = {"y_max": y_max, "x_curr": x_at_y_min, "dx": dx, "id": f"Ребро {i+1}"}
        
        if y_min not in et:
            et[y_min] = []
        et[y_min].append(edge)
    return et

def demo_scanline_fill(polygon, et):
    if not et:
        return

    plt.ion()
    fig, ax = plt.subplots(figsize=(10, 8))
    
    y_start = min(et.keys())
    y_end = max(edge['y_max'] for edges in et.values() for edge in edges)
    
    aet = []
    accumulated_x = []
    accumulated_y = []
    
    xs = polygon['X'].tolist() + [polygon['X'].iloc[0]]
    ys = polygon['Y'].tolist() + [polygon['Y'].iloc[0]]

    for y in range(y_start, y_end + 1):
        aet = [edge for edge in aet if edge['y_max'] > y]
        
        if y in et:
            aet.extend(et[y])
            
        aet.sort(key=lambda edge: edge['x_curr'])
        
        ax.clear()
        ax.plot(xs, ys, color='black', linewidth=2, label='Контур многоугольника')
        ax.grid(True, linestyle='--')
        
        ax.set_xticks(range(int(polygon['X'].min())-1, int(polygon['X'].max())+2))
        ax.set_yticks(range(int(polygon['Y'].min())-1, int(polygon['Y'].max())+2))
        
        ax.axhline(y=y, color='red', linewidth=1.5)
        
        current_step_x = []
        current_step_y = []
        
        for i in range(0, len(aet) - 1, 2):
            x_start = int(np.ceil(aet[i]['x_curr']))
            x_end = int(np.floor(aet[i+1]['x_curr']))
            print(x_start, x_end)
            for x in range(x_start, x_end + 1):
                current_step_x.append(x)
                current_step_y.append(y)

        accumulated_x.extend(current_step_x)
        accumulated_y.extend(current_step_y)
        
        if accumulated_x:
            ax.scatter(accumulated_x, accumulated_y, color='lightblue', marker='s', s=150, label='Закрашенные пиксели')

        if current_step_x:
            ax.scatter(current_step_x, current_step_y, color='blue', marker='s', s=150, label='Текущие пиксели')
            
        ax.set_title(f"Текущий шаг Y = {y}")
        ax.legend(loc='upper right')
        fig.canvas.draw()
        fig.canvas.flush_events()

        for edge in aet:
            edge['x_curr'] += edge['dx']
            
        input()
        
    plt.ioff()
    plt.show()

if __name__ == "__main__":
    polygon = read_data()
    et = build_edge_table(polygon)
    demo_scanline_fill(polygon, et)
