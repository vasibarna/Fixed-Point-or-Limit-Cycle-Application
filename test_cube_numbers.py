import pytest
from fixed_point_limit_cycle import cube_digits_sum, fixed_point_or_limit_cycle



def test_cube():
    assert cube_digits_sum(0) == 0
    assert cube_digits_sum(123) == 36



