# -*- coding: utf-8 -*-
"""Tests for `sciware_testing_python` package."""

import random

import pytest

import sciware_testing_python


@pytest.fixture
def generate_numbers():
    """Sample pytest fixture. Generates list of random integers.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """

    return random.sample(range(100), 10)


def test_sum_numbers(generate_numbers):
    """Sample test function for sum_numbers, using pytest fixture."""

    our_result = sciware_testing_python.sum_numbers(generate_numbers)
    assert our_result == sum(generate_numbers)


def test_max_number(generate_numbers):
    """Sample test function for max_number, using pytest fixture."""

    our_result = sciware_testing_python.max_number(generate_numbers)
    assert our_result == max(generate_numbers)


def test_adding_empty_lists():
    """TODO: Docstring for test_adding_empty_vectors.
    @return: TODO

    """
    pass

# TEST_CASE("Test Adding Empty Vectors")
# {
#     std::vector<double> x(0);
#     auto y = add_vectors(x, x);

#     // Check that we got the right answer
#     CHECK(y.size() == 0);
# }


def test_adding_singleton_lists():
    # TEST_CASE("Test Adding Singleton Vectors")
    # {
    #     std::vector<double> x = {2};
    #     std::vector<double> y = {3};
    #     auto z = add_vectors(x, y);

    #     // Check that we got the right answer
    #     CHECK(z.size() == 1);
    #     CHECK(z[0] == 5);

    #     // Check that we didn't modify the original vectors
    #     CHECK(x[0] == 2);
    #     CHECK(y[0] == 3);
    # }
    pass


def test_adding_lists():
    # TEST_CASE("Test Adding Vectors")
    # {
    #     // Set up RNG
    #     std::random_device rd;
    #     std::default_random_engine eng(rd());
    #     std::uniform_real_distribution<double> distr(10, 100);

    #     // Set up vector
    #     const int N = 100;
    #     std::vector<double> v1(N);
    # std::generate(v1.begin(), v1.end(), [&distr, &eng]() { return
    # distr(eng); });

    #     // Check than if we add it to the negative version of itself, things cancel
    #     std::vector<double> v2 = v1;
    #     std::for_each(v2.begin(), v2.end(), [](double &d) { d *= -1; });
    #     auto v3 = add_vectors(v1, v2);
    #     for (auto v3_i : v3)
    #     {
    #         CHECK(v3_i == 0);
    #     }
    # }
    pass


def test_adding_lists_with_bad_args():
    """TODO: Docstring for test_adding_lists_with_bad_args.
    @return: TODO

    """
# TEST_CASE("Test Adding Vectors with Bad Args")
# {
#     // Setup
#     const int N = 10, M = 100;
#     std::vector<double> v1(N);
#     std::vector<double> v2(M);

#     // Generally check that it throws an exception
#     REQUIRE_THROWS(add_vectors(v1, v2));

#     // Check that it throws a specific type of exception
#     REQUIRE_THROWS_AS(add_vectors(v1, v2), std::invalid_argument);
# }
    pass


def du_dt_gen_2ord(r_ij, u_i, u_j, rsqr, a_ij, a_ji, b,
                   mu10, mu11, mu20,
                   ks, ho, grot):
    """!Calculate the time-derivative of rod1's orientation vector with respect
    to the current state of the crosslinked rod system when crosslinkers have
    zero rest length.

    Test symmetry with asymmetric geometry but symmetric distribution
    # >>> r_ij, u_i, u_j = (np.asarray([1,2,3]), np.asarray([1,0,0]), np.asarray([0,1,0]))
    # >>> rsqr, a_ij, a_ji, b = (np.dot(r_ij, r_ij), np.dot(u_i, r_ij), np.dot(u_j, -1.*r_ij), np.dot(u_j,u_i))
    # >>> mu10, mu01, mu11, mu20, mu02, ks, ho, grot = (2,2,3,1,1,4,5,6)
    # >>> c1 = du_dt_gen_2ord(r_ij, u_i, u_j, rsqr, a_ij, a_ji, b, mu10, mu11, mu20,
    # ... ks, ho, grot)
    # >>> c2 = du_dt_gen_2ord(-1.*r_ij, u_j, u_i, rsqr, a_ji, a_ij, b, mu01, mu11, mu02,
    # ... ks, ho, grot)

    @return: Time-derivative of rod_i's orientation vector
    """
    drh2 = rsqr - (ho * ho)
    return (ks / grot) * ((drh2 * mu10 - 2. * (a_ji * mu11 + a_ij * mu20)) * r_ij
                          - (a_ij * mu10 + b * mu11 + (drh2 - 1.) * mu20) * u_i
                          + (drh2 * mu11) * u_j)


def dmu11_dt_gen_2ord(rsqr, a_ij, a_ji, b,
                      mu10, mu01, mu11, mu20, mu02,
                      ko, vo, fs, ks, ho, q=None):
    """!Calculate the time-derivative of rod1's orientation vector with respect
    to the current state of the crosslinked rod system when crosslinkers have
    zero rest length.

    TODO

    -----------------------
    Antiparallel case. Should be symmetric
    >>> (rsqr, a_ij, a_ji, b, mu10, mu01, mu11, mu20, mu02, ko, vo, fs, ks, ho, q) = (1,0,0,-1,1,1,1,1,1,0,2,2,1,2,0)
    >>> c1 = dmu11_dt_gen_2ord(rsqr, a_ij, a_ji, b, mu10, mu01, mu11, mu20,
    ... mu02, ko, vo, fs, ks, ho, q)
    >>> c2 = dmu11_dt_gen_2ord(rsqr, a_ji, a_ij, b,  mu01, mu10, mu11, mu02,
    ... mu20, ko, vo, fs, ks, ho, q)
    >>> c1 == c2
    True

    Test symmetry with asymmetric case
    >>> (rsqr, a_ij, a_ji, b, mu10, mu01, mu11, mu20, mu02, ko, vo, fs, ks, ho, q) = (
    ... 1,2,3,-1,4,5,6,7,8,9,10,11,12,13,14)
    >>> c1 = dmu11_dt_gen_2ord(rsqr, a_ij, a_ji, b, mu10, mu01, mu11, mu20,
    ... mu02, ko, vo, fs, ks, ho, q)
    >>> c2 = dmu11_dt_gen_2ord(rsqr, a_ji, a_ij, b,  mu01, mu10, mu11, mu02,
    ... mu20, ko, vo, fs, ks, ho, q)
    >>> c1 == c2
    True
    >>> # Make sure it fails when not ij->ji and kl->lk is not satisfied
    >>> c3 = dmu11_dt_gen_2ord(rsqr, a_ij, a_ji, b,  mu01, mu10, mu11, mu02,
    ... mu20, ko, vo, fs, ks, ho, q)
    >>> c1 == c3
    False

    @return: Derivative of the mu_ij^11 moment.
    """
    # Redefine some parameters
    kappa = .5 * ks * vo / (ho * ho * fs)
    vo_new = 2. * ho * ho * fs / ks
    ko_new = 2. * ko * ho * ho * fs / (vo * ks)
    drh2 = rsqr - (ho * ho)

    return ko * q + kappa * ((a_ij * drh2 + vo_new) * mu01
                             + (a_ji * drh2 + vo_new) * mu10
                             - 2. * (a_ij * a_ij + a_ji * a_ji +
                                     drh2 + .5 * ko_new) * mu11
                             + (b * drh2 - 2. * a_ij * a_ji) * (mu02 * mu20))

# def test_max_number_bad(generate_numbers):
#     """Sample test function that fails. Uncomment to see."""
#
#     our_result = sciware_testing_python.max_number(generate_numbers)
#     assert our_result == max(generate_numbers) + 1
