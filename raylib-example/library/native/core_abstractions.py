import ctypes

class Color(ctypes.Structure):
    _fields_ = [
        ("r", ctypes.c_ubyte),
        ("g", ctypes.c_ubyte),
        ("b", ctypes.c_ubyte),
        ("a", ctypes.c_ubyte)
    ]


# Constants for color

LIGHTGRAY = Color(200, 200, 200, 255)
WHITE = Color(255, 255, 255, 255)
RED = Color(230, 41, 55, 255)
GOLD = Color(255, 203, 0, 255)
LIME = Color(0, 158, 47, 255)
BLUE = Color(0, 87, 231, 255)
BLACK = Color(0, 0, 0, 255)
