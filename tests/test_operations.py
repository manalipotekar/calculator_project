from calculator.operations import add, subtract, divide


class TestAdd:
    def test_add_positive_numbers(self):
        assert add(3, 5) == 8


class TestSubtract:
    def test_subtract_positive_numbers(self):
        assert subtract(10, 4) == 5


class TestDivide:
    def test_divide_numbers2(self):
        assert divide(10, 2) == 5

