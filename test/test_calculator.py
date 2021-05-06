from app import Calculator


class TestCalculator:

    def test_add(self):
        calculator = Calculator()
        assert calculator.add(2, 2) == 4

    def test_subtract(self):
        calculator = Calculator()
        assert calculator.subtract(4, 2) == 2

    def test_multiply(self):
        calculator = Calculator()
        assert calculator.multiply(2, 3) == 6

    def test_division(self):
        calculator = Calculator()
        assert calculator.division(10, 2) == 5
