import ctypes
from ctypes import util

# Check if the library exists
try:
    raylib = ctypes.CDLL(ctypes.util.find_library("raylib"))
except OSError:
    raise ImportError(f"Raylib not found, install it!: https://www.raylib.com/index.html")