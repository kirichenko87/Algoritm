import pytest
from src.HW1 import factorial


@pytest.mark.parametrize("value, expend_result",
                         [(5, 120),
                          (1, 1),
                          (20, 2432902008176640000)
                          ])
def test_factorial_positive(value, expend_result):
    assert factorial(value) == expend_result


