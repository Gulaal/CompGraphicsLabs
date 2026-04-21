import matplotlib.pyplot as plt
import pandas as pd

def read_data():
    file_path = 'cutting_off_segment/cyrus_beck_input.csv'
    file_data = pd.read_csv(file_path)
    polygon = file_data.iloc[:-2]
    line = file_data.iloc[-2:]
    return polygon, line

def dot(a, b):
    return a[0]*b[0] + a[1]*b[1]

def sub(a, b):
    return (a[0]-b[0], a[1]-b[1])

def add(a, b):
    return (a[0]+b[0], a[1]+b[1])

def mult(a, t):
    return (a[0]*t, a[1]*t)

def polygon_area(polygon):
    area = 0
    n = polygon.shape[0]
    for i in range(n):
        x1, y1 = polygon.iloc[i]
        x2, y2 = polygon.iloc[(i+1)%n]
        area += x1*y2 - x2*y1
    return area / 2

def get_edges(polygon):
    edges = []
    n = polygon.shape[0]
    signed_area = polygon_area(polygon)
    ccw = signed_area > 0
    for i in range(n):
        a = (polygon.iloc[i, 0], polygon.iloc[i, 1])
        b = (polygon.iloc[(i+1)%n, 0], polygon.iloc[(i+1)%n, 1])
        vec = (b[0]-a[0], b[1]-a[1])
        if ccw:
            norm = (-vec[1], vec[0])
        else:
            norm = (vec[1], -vec[0])
        edges.append((a, norm))
    return edges

def cyrus_beck(line, edges, eps=1e-9):
    p0 = (line.iloc[0, 0], line.iloc[0, 1])
    p1 = (line.iloc[1, 0], line.iloc[1, 1])
    dx = p1[0] - p0[0]
    dy = p1[1] - p0[1]
    t_in, t_out = 0.0, 1.0
    candidates_in = []
    candidates_out = []

    for idx, (point_on_edge, norm) in enumerate(edges):
        num = dot(norm, sub(p0, point_on_edge))
        den = dot(norm, (dx, dy))
        if abs(den) < eps:
            if num < -eps:
                return None, None, False, [], []
        else:
            t = -num / den
            point = add(p0, mult((dx, dy), t))
            if den > 0:
                candidates_in.append((t, point, idx))
                t_in = max(t_in, t)
            else:
                candidates_out.append((t, point, idx))
                t_out = min(t_out, t)

    if t_in <= t_out + eps:
        p_in = add(p0, mult((dx, dy), t_in))
        p_out = add(p0, mult((dx, dy), t_out))
        return p_in, p_out, True, candidates_in, candidates_out
    else:
        return None, None, False, candidates_in, candidates_out

def plot_clipping(polygon, line, result, visible, candidates_in, candidates_out):
    fig, ax = plt.subplots(figsize=(8, 8))

    poly_x = polygon.iloc[:, 0].tolist()
    poly_y = polygon.iloc[:, 1].tolist()
    poly_x.append(poly_x[0])
    poly_y.append(poly_y[0])
    ax.fill(poly_x, poly_y, alpha=0.3, color='lightblue', edgecolor='blue', linewidth=2, label='Отсекатель')

    p0 = (line.iloc[0, 0], line.iloc[0, 1])
    p1 = (line.iloc[1, 0], line.iloc[1, 1])
    ax.plot([p0[0], p1[0]], [p0[1], p1[1]], 'gray', linewidth=1.5, label='Исходный отрезок')

    for t, pt, idx in candidates_in:
        ax.plot(pt[0], pt[1], 'gs', markersize=8, label='Потенциальный вход' if idx == 0 else "")

    for t, pt, idx in candidates_out:
        ax.plot(pt[0], pt[1], 'yD', markersize=8, label='Потенциальный выход' if idx == 0 else "")

    if visible and result is not None:
        p_in, p_out = result
        ax.plot([p_in[0], p_out[0]], [p_in[1], p_out[1]], 'r-', linewidth=3, label='Отсечённый отрезок')
        ax.plot(p_in[0], p_in[1], 'ro', markersize=8, label='Реальная точка входа')
        ax.plot(p_out[0], p_out[1], 'ro', markersize=8, label='Реальная точка выхода')
    else:
        ax.text(0.5, 0.5, "Отрезок полностью не видим", transform=ax.transAxes,
                ha='center', va='center', fontsize=12, color='red')

    ax.set_aspect('equal')
    ax.grid(True, linestyle='--', alpha=0.7)
    plt.show()

if __name__ == "__main__":
    P, L = read_data()
    edges = get_edges(P)
    p_in, p_out, visible, cand_in, cand_out = cyrus_beck(L, edges)
    result = (p_in, p_out) if visible else None
    plot_clipping(P, L, result, visible, cand_in, cand_out)