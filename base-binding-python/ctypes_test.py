import ctypes

# Load the shared library into ctypes
lib = ctypes.CDLL("./native/shared.so")

# Define the function signature for the C++ function
lib.cmult.argtypes = [ctypes.c_int, ctypes.c_float]
lib.cmult.restype = ctypes.c_float
cmult = lib.cmult
# Call the C++ function
result = cmult(5, 6)
print("The result of 5 * 6 is: ", result)

# create the struct
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

# Load the shared library into ctypes
move = lib.move
move.argtypes = [Point, ctypes.c_int, ctypes.c_int]
move.restype = Point
point = Point(5, 6)
moved = move(point, 10, 20)
print("The result of translating (5, 6) by (10, 20) is: ", moved.x, moved.y)

# Move point pointer
move_pointer = lib.move_pointer
move_pointer.argtypes = [ctypes.POINTER(Point), ctypes.c_int, ctypes.c_int]
move_pointer.restype = None
point = Point(5, 6)
point_pointer = ctypes.byref(point)
move_pointer(point_pointer, 10, 20)
print("The result of translating (5, 6) by (10, 20) is: ", point.x, point.y)

# Find GSL
gsl = ctypes.CDLL("libgsl.so")
# Bessel function: https://en.wikipedia.org/wiki/Bessel_function
gsl.gsl_sf_bessel_J0.argtypes = [ctypes.c_double] 
gsl.gsl_sf_bessel_J0.restype = ctypes.c_double
bessel = gsl.gsl_sf_bessel_J0
result = bessel(5)

print("The result of J0(5) is: ", result)