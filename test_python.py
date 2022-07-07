import math
from main import filter_odd_num, return_sum_with_ten


# В модуле написать тесты для встроенных функций filter, map, sorted,
# а также для функций из библиотеки math: pi, sqrt, pow, hypot


def test_filter():
    nums = [0, 1, 4, 5, 2, 9, 6, 7]
    assert list(filter(filter_odd_num, nums)) == [0, 4, 2, 6]


def test_map():
    nums = [1, 4]
    assert list(map(return_sum_with_ten, nums)) == [11, 14]


def test_sorted():
    nums = [0, 1, 4, 5, 2, 9, 6, 7]
    assert sorted(nums) == [0, 1, 2, 4, 5, 6, 7, 9]


def test_pi():
    assert math.pi == 3.141592653589793


def test_sq():
    assert math.sqrt(4) == 2


def test_pow():
    assert math.pow(2, 3) == 8


def test_hypot():
    assert math.hypot(2, 2) == math.hypot(2, 2)


