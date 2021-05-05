def prime_larger_than(x: int) -> int:
    """Find a prime stricly larger than x"""
    assert x > 0
    prime_candidate = x + 1
    while True:
        if is_prime(prime_candidate):
            return prime_candidate
        # this is the most naive version which will only work on
        # very small numbers, but for the moment it's good
        prime_candidate += 1


def is_prime(x: int) -> bool:
    """Check whether x is prime"""
    # the most naive version, yet for the moment should suffice
    assert x > 0
    # check for the smallest numbers
    if x in [1, 2]:
        return True
    # loop through all numbers, and check if it can be factorized
    for i in range(2, x):
        if x % i == 0:
            return False
    # if it can't, it's prime
    return True


def multiplicative_inverse(x: int, m: int) -> int:
    """Find the multiplicative inveserse of x, modulo m
    In other words, find y such that y * x == 1 (modulo m)
    """
    for i in range(2, m):
        if i * x % m == 1:
            return i

    raise RuntimeError(
        f"Could not find a multiplicative inverse for {x=}, {m=}."
        " maybe they were not relatively prime"
    )


def m_pow_e_mod_n(M: int, e: int, n: int) -> int:
    """calculate M^e (mod n).
    this implements the "exponation by repeated squaring and multiplication" method
    not the most effcient but amazingly simple
    """
    C = 1
    # loop through the binary representation of e
    for e_i in f"{e:b}":
        # C = C**2 % n
        C = ((C % n) ** 2) % n
        if e_i == "1":
            # C = C * M % n
            C = ((C % n) * (M % n)) % n
    return C
