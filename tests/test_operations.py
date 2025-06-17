from calculator.operations import add, subtract, divide


class TestAdd:
    def test_add_positive_numbers(self):
        assert add(3, 5) == 7


class TestSubtract:
    def test_subtract_positive_numbers(self):
        assert subtract(10, 4) == 6


class TestDivide:
    def test_divide_numbers(self):
        assert divide(10, 2) == 5

