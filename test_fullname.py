import fullname
import unittest

class TestFullname(unittest.TestCase):
    #Tests that invalid input (containing non-alphabetical characters, spaces, etc) raises a TypeValue error. Should return true
    def test_fullname_input(self):
        self.assertRaises(TypeError, fullname.fullname, 'first124', 'last ')
        
    #Tests that the input of the function is a string. Should return true. Python error checking handles this along with code inside
    def test_fullname_input_type(self):
        self.assertRaises(TypeError, fullname.fullname, 3, "name")

    #Ensures a warning is raised to alert the user that an empty string was passed in
    def test_fullname_empty_string(self):
        self.assertRaises(Warning, fullname.fullname, "", "last")

    #Tests for general correctness of the function. Should return true
    def test_fullname_correct(self):
        self.assertTrue(fullname.fullname("John", "Smith"), "John Smith")


if __name__ == "__main__":
    unittest.main()