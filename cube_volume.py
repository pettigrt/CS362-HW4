import unittest

def cube_volume(l, w, h):
    #Initial input handling
    try:
        l = float(l)
        w = float(w)
        h = float(h)
    except ValueError:
        return -1
    #Ensure values are greater than 0
    if (l < 0 or w < 0 or h < 0):
        raise ValueError("Dimensions must be non negative values")
    #Calculation and returns value as a float
    return l*w*h


