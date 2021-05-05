import logging
from tqdm import tqdm
import random

logger = logging.getLogger(__name__)


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


def gcd(p, q):
    """check the greatest common denominator, Euclid's algorithm"""
    # make sure p > q
    if p < q:
        p, q = q, p
    while True:
        if p % q == 0:
            return q
        p, q = q, p % q


def is_prime_solovay_and_strassen(b: int, num_trials: int = 10) -> bool:
    """Solovay and Strassen algorithm to check for primeness
    Solovay, R., and Strassen, V. A Fast Monte-Carlo test for primality. SIAM J.Comptng. (March 1977), 84-85

    """
    # test not even
    assert b % 2 != 0

    # check for a 100 times
    for i in tqdm(range(num_trials)):
        a = random.randint(3, b - 1)
        logger.debug(f"{a=}")
        # a shouldn't be even
        if a % 2 == 0:
            continue

        # the check
        logger.debug("gcd")
        # a shouldn't be even
        if gcd(a, b) != 1:
            return False

        # get the jacobi sign
        logger.debug("jacobi")
        _jacobi_mod_b = jacobi(a, b) % b

        # calculate (a**(b-1)/2 % b)
        logger.debug("a**(b-1)/2 % b")
        _a_pow_half_b_mod_b = m_pow_e_mod_n(a, int((b - 1) / 2), b)

        logger.debug(f"{_jacobi_mod_b=}, {_a_pow_half_b_mod_b=}")
        if _jacobi_mod_b != _a_pow_half_b_mod_b:
            return False
    return True


def jacobi(a, b):
    """the jacobi subroutine, has a value in {-1, 1}"""
    logger.debug(f"jacobi, {a=}, {b=}")
    assert a <= b
    assert b % 2 == 1
    # a shouldn't be even
    if a == 1:
        return 1
    if a % 2 == 0:
        return jacobi(int(a / 2), b) * jacobi_sign_even(b)
    return jacobi(b % a, a) * jacobi_sign_odd(a, b)


def jacobi_sign_even(b):
    """calculate -1 ** ((b**2 - 1)/8)
    but without multiplication (because the results are too big)
    """
    part1 = (b + 1) / 2
    part2 = (b - 1) / 2
    # either part1 or part2 will be able to divide by 4
    if part1 % 2 == 0:
        part1 /= 2
    else:
        part2 /= 2

    # check the sign of part1 * part2
    if part1 % 2 == 0:
        return 1
    if part2 % 2 == 0:
        return 1
    return -1


def jacobi_sign_odd(a, b):
    """calculate (-1)**((a-1) * (b-1)/4)
    but without multiplication (because the results are too big)
    """
    part1 = (a - 1) / 2
    part2 = (b - 1) / 2

    # check the sign of part1 * part2
    if part1 % 2 == 0:
        return 1
    if part2 % 2 == 0:
        return 1
    return -1
