from rsa_scratch.rsa import (
    prime_larger_than,
    is_prime,
    multiplicative_inverse,
    m_pow_e_mod_n,
)
import pytest


def test_prime_larger_than():
    assert prime_larger_than(4) == 5
    assert prime_larger_than(10) == 11


def test_is_prime():
    assert is_prime(11)
    assert not is_prime(10)


def test_multiplicative_inverse():
    assert multiplicative_inverse(3, 20) == 7
    assert multiplicative_inverse(7, 20) == 3

    with pytest.raises(RuntimeError):
        multiplicative_inverse(4, 20)

    # test the test to break
    # multiplicative_inverse(5, 20)


def test_m_pow_e_mod_n():
    # p = 3, q=11
    assert m_pow_e_mod_n(4, 17, 33) == (4 ** 17) % 33
