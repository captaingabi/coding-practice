#!/bin/python3
import pytest


def find_sign(number: int) -> str:
    if number > 0:
        ans = "positive"
    elif number < 0:
        ans = "negative"
    else:
        ans = "zero"
    return ans


@pytest.mark.parametrize("number, result", [
    [2, "positive"],
    [-2, "negative"],
    [0, "zero"],
])
def test_return_value(number, result):
    assert find_sign(number) == result
