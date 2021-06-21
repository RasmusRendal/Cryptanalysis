import math

def trial_division_prime_check(n: int) -> bool:
    """ Check whether a given integer is prime

    Trial division is very slow. I just needed
    this to implement other prime stuff"""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True


def prime_check(n: int) -> bool:
    """Checks whether a given integer is prime

    This method just uses the fastest method
    in the general case that is already implemented
    """

    return trial_division_prime_check(n)


def next_prime(n: int) -> int:
    """Generates the next prime after n"""
    while True:
        if prime_check(n):
            return n
        n += 1
