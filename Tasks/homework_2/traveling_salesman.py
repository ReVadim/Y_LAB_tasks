from math import sqrt
from itertools import permutations


points_list = [(0, 1), (1, 4), (4, 1), (5, 5), (7, 2)]


def calculate_length(point_1, point_2):
    """ Calculates the distance between two points
    """
    return sqrt((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2)


def find_all_possible_ways(points: list):
    """ Re-sorting all possible combinations
    """
    return permutations(points, len(points))


def final_length(p1, p_list):
    """ Calculates the total length
    """
    p_list.insert(0, p1)
    p_list.append(p1)

    result_length = 0
    for i in range(1, len(p_list)):
        result_length += calculate_length(p_list[i - 1], p_list[i])

    return result_length


def find_min_length(point, p_list):
    """ Find the shortest path of all possible options
    """
    all_possible_ways = []
    for i in p_list:
        i = list(i)
        length = final_length(point, i)
        all_possible_ways.append((i, length))

    return min(all_possible_ways)


def display_result(data):
    """ Displaying result value
    """
    result = ''
    length = 0
    for i in range(1, len(data[0])):
        length += calculate_length(data[0][i - 1], data[0][i])
        result += f'{data[0][i - 1]} -> {data[0][i]}[{length}]'

    return f'{result} = {str(data[-1])}'


def main():
    """ Main function
    """
    all_ways = find_all_possible_ways(points_list[1:])
    result = find_min_length(points_list[0], all_ways)
    print(display_result(result))


if __name__ == '__main__':
    main()
