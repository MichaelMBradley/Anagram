from math import sqrt


def get_n_primes(n) -> list[int]:
    """
    Gets the first n primes using a fairly inefficient method.
    Should be suitable for generating just a few primes though.

    Parameters
    ----------
    n : int
        The number of primes to generate

    Returns
    -------
    list[int]
        A list of prime numbers
    """
    if n < 0:
        raise Exception(f"n must be at least 0 (was {n})")
    if n == 0:
        return []
    primes = [2]
    i = 3
    while True:
        if len(primes) == n:
            break
        for p in primes:
            if i % p == 0:
                break
            if p > sqrt(i):
                primes.append(i)
                break
        i += 1
    return primes


if __name__ == "__main__":
    print(get_n_primes(10))
