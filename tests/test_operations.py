import pytest
from calculator.operations import add, subtract, multiply, divide


class TestAdd:
    def test_add_positive_numbers(self):
        assert add(3, 5) == 8

    def test_add_negative_numbers(self):
        assert add(-3, -5) == -8


class TestSubtract:
    def test_subtract_positive_numbers(self):
        assert subtract(10, 4) == 6

    def test_subtract_result_negative(self):
        assert subtract(3, 5) == -2


class TestMultiply:
    def test_multiply_integers(self):
        assert multiply(4, 5) == 20

    def test_multiply_by_zero(self):
        assert multiply(7, 0) == 0


class TestDivide:
    def test_divide_numbers(self):
        assert divide(10, 2) == 5

    def test_divide_by_zero_raises_error(self):
        with pytest.raises(ValueError, match="Cannot divide by zero."):
            divide(10, 0)
