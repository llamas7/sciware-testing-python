import pytest
from sciware_testing_python import sum_numbers, add_vectors


def test_sum_numbers_123():
    # basic test to see if we get the expected answer for a simple case.
    sum = sum_numbers([1, 2, 3])
    assert sum == 6


def test_sum_numbers_yours():
    # write another test of the sum_numbers function
    sum = sum_numbers([1, -1, 0.0])
    assert sum == 0


def test_sum_numbers_empty():
    # what's the sum of an empty list?
    sum = sum_numbers([])
    pass


@pytest.mark.xfail(strict=True, raises=TypeError)
def test_sum_strings():
    assert sum_numbers(["1", "2", "3"]) == "123"


# Write a test for the add_vectors function
def test_add_vectors():
    assert add_vectors([1, 2, 3, 4], [3, 4, 5, 6]) == [4, 6, 8, 10]


# Write a test for sum_numbers on a list of booleans
