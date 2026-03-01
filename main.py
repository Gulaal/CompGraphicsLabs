import math

def task1(first_point: tuple, second_point: tuple) -> tuple:
    """y = kx + b"""
    if second_point[0] - first_point[0] == 0:
        print(f"x = {first_point[0]}")
        k = math.inf
        b = 0
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
    A = (second_point[1]-first_point[1])*(third_point[2]-first_point[2]) -\
          (third_point[1]-first_point[1])*(second_point[2]-first_point[2])
    B = (third_point[0]-first_point[0])*(second_point[2]-first_point[2]) -\
          (second_point[0]-first_point[0])*(third_point[2]-first_point[2])
    C = (second_point[0]-first_point[0])*(third_point[1]-first_point[1]) -\
          (third_point[0]-first_point[0])*(second_point[1]-first_point[1])
    D = -first_point[0] * A + (-first_point[1] * B) + (-first_point[2] * C)

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
    first_point = (0, 2)
    second_point = (0, 0)
    third_point = (10000, 0)

    P1, P2, P3 = (3,3,1), (2,5,1), (3,1,2)

    print(task2(first_point, second_point, third_point))
    print(task3(first_point, second_point, third_point))
    print(task4(P1, P2, P3))
    return


if __name__ == '__main__':
    main()
