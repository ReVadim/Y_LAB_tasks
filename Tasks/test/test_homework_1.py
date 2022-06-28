import pytest
from ..homework_1.Homework_1 import (
    domain_name,
    int32_to_ip,
    the_trailing_factorial_zeros,
    bananas,
    count_find_num,
)


# task_1
def test_task_1():
    assert domain_name("http://google.com") == "google"
    assert domain_name("http://google.co.jp") == "google"
    assert domain_name("www.xakep.ru") == "xakep"
    assert domain_name("https://youtube.com") == "youtube"


# task_2
def test_int32_to_ip():
    assert int32_to_ip(2154959208) == "128.114.17.104"
    assert int32_to_ip(0) == "0.0.0.0"
    assert int32_to_ip(2149583361) == "128.32.10.1"


# task_3
def test_the_trailing_factorial_zeros():
    assert the_trailing_factorial_zeros(0) == 0
    assert the_trailing_factorial_zeros(6) == 1
    assert the_trailing_factorial_zeros(30) == 7


# task_4
def test_bananas():
    assert bananas("banann", 'banana', '-') == set()
    assert bananas("banana", 'banana', '-') == {"banana"}
    assert bananas("bbananana", 'banana', '-') == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                                    "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                                    "-ban--ana", "b-anana--"}
    assert bananas("bananaaa", 'banana', '-') == {"banan-a-", "banana--", "banan--a"}
    assert bananas("bananana", 'banana', '-') == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}


# task_5
def test_count_find_num():
    primes_list = [2, 3]
    limit = 200
    assert count_find_num(primes_list, limit) == [13, 192]

    primes_list = [2, 5]
    limit = 200
    assert count_find_num(primes_list, limit) == [8, 200]

    primes_list = [2, 3, 5]
    limit = 500
    assert count_find_num(primes_list, limit) == [12, 480]

    primes_list = [2, 3, 5]
    limit = 1000
    assert count_find_num(primes_list, limit) == [19, 960]

    primes_list = [2, 3, 47]
    limit = 200
    assert count_find_num(primes_list, limit) == []
