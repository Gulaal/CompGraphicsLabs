import math

def task1(first_point: tuple, second_point: tuple) -> tuple:
    """y = kx + b"""
    if first_point == second_point:
        raise ValueError("Точки должны быть разными")
    if second_point[0] - first_point[0] == 0:
        print(f"x = {first_point[0]}")
        k = math.inf
        b = first_point[0]
        return k, b
    elif second_point[1] - first_point[1] == 0:
        print(f"y = {first_point[1]}")
        k = 0
        b = first_point[1] - k * first_point[0]
        return k, b
    k = (second_point[1] - first_point[1]) / (second_point[0] - first_point[0])
    b = first_point[1] - k * first_point[0]
    print(f"y = {k}x + {b}")
    return k, b


def task2(first_point: tuple, second_point: tuple, third_point: tuple) -> bool:
    (k, b) = task1(first_point, second_point)
    if math.isinf(k):
        if third_point[0] == first_point[0] and \
                min(first_point[1], second_point[1]) <= third_point[1] <= max(first_point[1], second_point[1]):
            return True
        else:
            return False
    if third_point[1] == k * third_point[0] + b:
        if (min(first_point[0], second_point[0]) <= third_point[0] <= max(first_point[0], second_point[0])) and \
                min(first_point[1], second_point[1]) <= third_point[1] <= max(first_point[1], second_point[1]):
            return True
    return False

def task3(A: tuple, B: tuple, C: tuple) -> str:
    BA = (A[0] - B[0], A[1] - B[1])
    BC = (C[0] - B[0], C[1] - B[1])
    scalar_product = BA[0]*BC[0] + BA[0]*BC[0]
    if scalar_product == 0:
        return "Прямой"
    elif scalar_product > 0:
        return "Острый"
    return "Тупой"


def task4(first_point: tuple, second_point: tuple, third_point: tuple) -> tuple:
    """Ax + By + Cz + D = 0"""
    AB = (second_point[0] - first_point[0],
          second_point[1] - first_point[1],
          second_point[2] - first_point[2])
    AC = (third_point[0] - first_point[0],
          third_point[1] - first_point[1],
          third_point[2] - first_point[2])

    cross = (AB[1] * AC[2] - AB[2] * AC[1],
             AB[2] * AC[0] - AB[0] * AC[2],
             AB[0] * AC[1] - AB[1] * AC[0])

    if all(abs(coord) < 1e-9 for coord in cross):
        raise ValueError("Точки не должны лежать на одной прямой")

    A, B, C = cross
    D = - (A * first_point[0] + B * first_point[1] + C * first_point[2])

    A_str = f"{A}x"
    if B < 0:
        B_str = f"- {abs(B)}y"
    else:
        B_str = f"+ {B}y"
    if C < 0:
        C_str = f"- {abs(C)}z"
    else:
        C_str = f"+ {C}z"
    if D < 0:
        D_str = f"- {abs(D)}"
    else:
        D_str = f"+ {D}"

    print(f"{A_str} {B_str} {C_str} {D_str} = 0")
    return A, B, C, D

def main():
    task4((0, 0, 0), (0, 1, 0), (0, 0, 1))
    return

if __name__ == '__main__':
    main()
