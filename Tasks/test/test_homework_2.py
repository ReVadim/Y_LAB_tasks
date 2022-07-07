import pytest

from Tasks.homework_2.traveling_salesman import calculate_length, find_all_possible_ways


def test_calculate_length():
    assert calculate_length((0, 1), (1, 4)) == 3.1622776601683795


def test_find_all_possible_ways():
    test_list = [(0, 1), (1, 2), (2, 3)]
    ways = find_all_possible_ways(test_list)
    count = 0
    for _ in ways:
        count += 1
    assert count == 6
