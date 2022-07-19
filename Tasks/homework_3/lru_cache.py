from functools import lru_cache, wraps


@lru_cache(maxsize=64)
def multiplier(number: int) -> int:
    """ Adding caching to the function.
    The maxsize argument tells lru_cache how many last values to remember
    """
    return number * 2


# base method
def caching(function):
    results_storage = {}

    @wraps(function)
    def wrapper(*args):
        try:
            return results_storage[args]
        except KeyError:
            result = function(*args)
            results_storage[args] = result
            return result

    return wrapper


@caching
def quadratic_multiplier(number: int) -> int:
    """ We use our own decorator for caching
    """
    return number * number


print(quadratic_multiplier(72))
print(quadratic_multiplier(19))
print(quadratic_multiplier(72))
