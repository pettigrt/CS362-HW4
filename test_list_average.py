import list_average
import unittest

class TestListAverage(unittest.TestCase):
    #Ensures empty lists raises an error. Should return true
    def test_list_empty(self):
        self.assertRaises(Warning, list_average.list_average, [])

    #Catches non-numeric values in a list. Test should return true
    def test_list_bad_value(self):
        self.assertRaises(TypeError, list_average.list_average, [3, 4, 'a', 6])

    #Tests for general correctness and that an integer list can return a floating value
    def test_list_correct(self):
        self.assertEqual(list_average.list_average([5, 6, 7, 8]), 26/4.0)


if __name__ == "__main__":
    unittest.main()