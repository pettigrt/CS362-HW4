import unittest
import cube_volume

class TestCubeVolume(unittest.TestCase):
    #Test to ensure calculation itself is correct. Should return true
    def test_volume_calc(self):
        self.assertEqual(cube_volume.cube_volume(10, 2, 5), 100)

    #Test to ensure input is positive. Should return true
    def test_volume_positive(self):
        self.assertRaises(ValueError, cube_volume.cube_volume, 2, -4, 5)
        
    #Test to ensure function can take float input. Should return true
    def test_volume_float(self):
        self.assertEqual(cube_volume.cube_volume(2.5, 4.5, 6.5), 73.125)

    #Test to ensure only floats or ints are accepted. Should return true
    def test_volume_input(self): 
        self.assertEqual(-1, cube_volume.cube_volume(24, 'b', 2))


if __name__ == "__main__":
    unittest.main()