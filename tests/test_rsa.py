from rsa_scratch.rsa import (
    prime_larger_than,
    is_prime,
    multiplicative_inverse,
    m_pow_e_mod_n,
    gcd,
    is_prime_solovay_and_strassen,
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


def test_gcd():
    assert gcd(4, 20) == 4
    assert gcd(5, 20) == 5
    assert gcd(35, 20) == 5
    # test the test
    # assert gcd(120, 56) == 7


def test_is_prime_solovay_and_strassen():
    assert is_prime_solovay_and_strassen(8191)
    assert is_prime_solovay_and_strassen(65537)
    assert is_prime_solovay_and_strassen(999999000001)
    assert is_prime_solovay_and_strassen(67280421310721)
    # assert is_prime_solovay_and_strassen(170141183460469231731687303715884105727)
