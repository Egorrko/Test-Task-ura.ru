import pytest

from fizzbuzz import FizzBuzz


@pytest.fixture
def default_rules():
    return {3: 'Fizz', 5: 'Buzz'}


@pytest.fixture
def more_rules():
    return {2: 'Second', 3: 'Fizz', 5: 'Buzz'}


@pytest.fixture
def empty_rules():
    return {}


def test_default(default_rules):
    fb = FizzBuzz(rules=default_rules)
    original = [1, 2, 'Fizz', 4, 'Buzz', 'Fizz',
                7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
    assert list(fb.generator()) == original


def test_more(more_rules):
    fb = FizzBuzz(rules=more_rules)
    original = [1, 'Second', 'Fizz', 'Second',
                'Buzz', 'SecondFizz', 7,
                'Second', 'Fizz', 'SecondBuzz', 11,
                'SecondFizz', 13, 'Second', 'FizzBuzz']
    assert list(fb.generator()) == original


def test_empty(empty_rules):
    fb = FizzBuzz(rules=empty_rules)
    assert list(fb.generator()) == [1, 2, 3, 4, 5, 6, 7,
                                    8, 9, 10, 11, 12, 13, 14, 15]
