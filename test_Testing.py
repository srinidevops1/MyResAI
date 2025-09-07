import unittest
from unittest.mock import patch
from io import StringIO
from Testing import add_two_numbers, multiply_two_numbers, divide_two_numbers, subtract_two_numbers


class TestAddTwoNumbers(unittest.TestCase):

    @patch('builtins.input', side_effect=['10', '5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_add_two_numbers_success(self, mock_stdout, _mock_input):
        add_two_numbers()
        self.assertEqual(mock_stdout.getvalue().strip(), 'The sum of 10.0 and 5.0 is: 15.0')

    @patch('builtins.input', side_effect=['-5', '3'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_add_with_negative_number(self, mock_stdout, _mock_input):
        add_two_numbers()
        self.assertEqual(mock_stdout.getvalue().strip(), 'The sum of -5.0 and 3.0 is: -2.0')

    @patch('builtins.input', side_effect=['ten', '5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_add_invalid_input(self, mock_stdout, _mock_input):
        add_two_numbers()
        self.assertEqual(mock_stdout.getvalue().strip(), 'Invalid input. Please enter numeric values.')


class TestMultiplyTwoNumbers(unittest.TestCase):

    @patch('builtins.input', side_effect=['6', '7'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_multiply_two_numbers_success(self, mock_stdout, _mock_input):
        multiply_two_numbers()
        self.assertEqual(mock_stdout.getvalue().strip(), 'The product of 6.0 and 7.0 is: 42.0')

    @patch('builtins.input', side_effect=['100', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_multiply_by_zero(self, mock_stdout, _mock_input):
        multiply_two_numbers()
        self.assertEqual(mock_stdout.getvalue().strip(), 'The product of 100.0 and 0.0 is: 0.0')

    @patch('builtins.input', side_effect=['6', 'xyz'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_multiply_invalid_input(self, mock_stdout, _mock_input):
        multiply_two_numbers()
        self.assertEqual(mock_stdout.getvalue().strip(), 'Invalid input. Please enter numeric values.')


class TestDivideTwoNumbers(unittest.TestCase):

    @patch('builtins.input', side_effect=['10', '2'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_divide_two_numbers_success(self, mock_stdout, _mock_input):
        divide_two_numbers()
        self.assertEqual(mock_stdout.getvalue().strip(), 'The quotient of 10.0 and 2.0 is: 5.0')

    @patch('builtins.input', side_effect=['10', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_divide_by_zero(self, mock_stdout, _mock_input):
        divide_two_numbers()
        self.assertEqual(mock_stdout.getvalue().strip(), 'Error: Division by zero is not allowed.')

    @patch('builtins.input', side_effect=['abc', '2'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_divide_invalid_input(self, mock_stdout, _mock_input):
        divide_two_numbers()
        self.assertEqual(mock_stdout.getvalue().strip(), 'Invalid input. Please enter numeric values.')


class TestSubtractTwoNumbers(unittest.TestCase):

    @patch('builtins.input', side_effect=['20', '5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_subtract_two_numbers_success(self, mock_stdout, _mock_input):
        subtract_two_numbers()
        self.assertEqual(mock_stdout.getvalue().strip(), 'The difference of 20.0 and 5.0 is: 15.0')

    @patch('builtins.input', side_effect=['10', '-5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_subtract_negative_number(self, mock_stdout, _mock_input):
        subtract_two_numbers()
        self.assertEqual(mock_stdout.getvalue().strip(), 'The difference of 10.0 and -5.0 is: 15.0')

    @patch('builtins.input', side_effect=['twenty', '5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_subtract_invalid_input(self, mock_stdout, _mock_input):
        subtract_two_numbers()
        self.assertEqual(mock_stdout.getvalue().strip(), 'Invalid input. Please enter numeric values.')


if __name__ == '__main__':
    unittest.main()
