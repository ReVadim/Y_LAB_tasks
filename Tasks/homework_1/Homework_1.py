from ipaddress import IPv4Address
from itertools import combinations
from math import prod


# Task 1
def domain_name(url):
    """ The method that will return the domain from the url """

    return url.replace('www.', '//').split('//')[-1].split('.')[0]


# Task 2
def int32_to_ip(int32):
    """ 32-bit integer as input and returns a string representation of it as an IPv4 address """

    return str(IPv4Address(int32))


# Task 3
def the_trailing_factorial_zeros(factorial):
    """ Calculation of the last zeros of the factorial """

    zeros_count = 0
    _ = 5
    while (factorial / _) >= 1:
        zeros_count += int(factorial / _)
        _ *= 5
    return int(zeros_count)


# Task 4
def bananas(letters: str = 'bbananana', search_phrase: str = 'banana', substitute: str = '-') -> set:
    """ Search for all variants of a given word from a set of letters """

    result = set()
    len_letters, len_search_phrase = len(letters), len(search_phrase)
    length_difference = len_letters - len_search_phrase
    if length_difference < 0:
        return result

    for combination in combinations(range(len_letters), length_difference):
        letters_list = list(letters)

        for index in combination:
            letters_list[index] = substitute

        sample_text = ''.join(letters_list)
        if sample_text.replace(substitute, '') == search_phrase:
            result.add(sample_text)
    return result


# Task 5
def count_find_num(primes_list: list, limit: int) -> list:
    """ Generate all the numbers in order. Smaller limit values, only prime factors of prime numbers """

    multiplication = prod(primes_list)
    result = [multiplication]
    if multiplication > limit:
        return []

    for value in primes_list:
        for x in result:
            x *= value
            if x <= limit:
                result.append(x)

    return [len(result), max(result)]
