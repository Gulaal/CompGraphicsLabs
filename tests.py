
from main import task1, task2, task3, task4
from math import inf
import pytest

def test_task1():
    assert task1((1, 2), (3, 4)) == (1.0, 1.0)
    assert task1((3, 4), (1, 2)) == (1.0, 1.0)
    assert task1((2, 5), (7, 5)) == (0.0, 5.0)
    assert task1((4, 1), (4, 8)) == (inf, 4.0)

    k, b = task1((-1, 3), (2, -3))
    assert k == pytest.approx(-2.0)
    assert b == pytest.approx(1.0)

    assert task1((0, 0), (5, 5)) == (1.0, 0.0)

    with pytest.raises(ValueError):
        task1((2, 3), (2, 3))

def test_task2():
    assert task2((0,0),(10,10),(5,5)) == True
    assert task2((0,0),(10,10),(12,12)) == False
    assert task2((0,0),(10,10),(-2,-2)) == False
    assert task2((0,5),(5,0),(2,3)) == True
    assert task2((1,2),(5,2),(3,2)) == True
    assert task2((1,2),(5,2),(3,3)) == False
    assert task2((3,1),(3,7),(3,3)) == True
    assert task2((3,1),(3,7),(4,3)) == False
    assert task2((0,0),(3,1),(2,2/3)) == True
    assert task2((0.5, 1.2),(2.5,3.2),(1.5,2.2)) == True

def test_task3():
    assert task3((0, 2), (0, 0), (3, 0)) == "Прямой"
    assert task3((2, 0), (0, 0), (0, 3)) == "Прямой"
    assert task3((1, 4), (1, 1), (5, 1)) == "Прямой"
    assert task3((1, 2), (0, 0), (4, 1)) == "Острый"
    assert task3((0.1, 0.2), (0, 0), (0.3, 0.1)) == "Острый"
    assert task3((-2, 1), (0, 0), (3, 1)) == "Тупой"
    assert task3((-0.1, 0.2), (0, 0), (0.3, -0.1)) == "Тупой"
    assert task3((4, 1), (0, 0), (1, 2)) == "Острый"

def test_task4():
    A, B, C, D = task4((1, 0, 0), (0, 1, 0), (0, 0, 1))
    assert abs(A * 1 + B * 0 + C * 0 + D) < 1e-9
    assert abs(A * 0 + B * 1 + C * 0 + D) < 1e-9
    assert abs(A * 0 + B * 0 + C * 1 + D) < 1e-9
    assert not (A == 0 and B == 0 and C == 0)
    A, B, C, D = task4((0, 0, 0), (1, 0, 0), (0, 1, 0))
    assert abs(A * 0 + B * 0 + C * 0 + D) < 1e-9
    assert abs(A * 1 + B * 0 + C * 0 + D) < 1e-9
    assert abs(A * 0 + B * 1 + C * 0 + D) < 1e-9
    assert abs(A * 0 + B * 0 + C * 1 + D) > 1e-9

    pts = [(0.5, 1.2, -0.3), (2.3, 3.4, 1.5), (-1.0, 2.5, 0.7)]
    A, B, C, D = task4(*pts)
    for x, y, z in pts:
        assert abs(A * x + B * y + C * z + D) < 1e-9

    pts_shuffled = [pts[1], pts[2], pts[0]]
    A2, B2, C2, D2 = task4(*pts_shuffled)
    for x, y, z in pts:
        assert abs(A2 * x + B2 * y + C2 * z + D2) < 1e-9

    A, B, C, D = task4((1000, 0, 0), (0, 1000, 0), (0, 0, 1000))
    assert abs(A * 1000 + D) < 1e-6
    assert abs(B * 1000 + D) < 1e-6
    assert abs(C * 1000 + D) < 1e-6