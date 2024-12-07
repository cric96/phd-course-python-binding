from native import library_cffi

ffi = library_cffi.ffi
lib = library_cffi.lib

class PointWrapper:
    def __init__(self, x=0, y=0):
        # Allocate memory for a C Point structure
        self._c_point = ffi.new("Point *")
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._c_point.x

    @x.setter
    def x(self, value):
        self._c_point.x = value

    @property
    def y(self):
        return self._c_point.y

    @y.setter
    def y(self, value):
        self._c_point.y = value

    def move(self, dx, dy):
        # Call the C move function to create a new Point
        new_c_point = lib.move(self._c_point[0], dx, dy)
        return PointWrapper(new_c_point.x, new_c_point.y)

    def move_in_place(self, dx, dy):
        # Modify the C Point in-place using move_pointer
        lib.move_pointer(self._c_point, dx, dy)

    def __repr__(self):
        return f"PointWrapper(x={self.x}, y={self.y})"

    def __del__(self):
        print(f"Freeing memory for Point({self.x}, {self.y})")
        ffi.release(self._c_point)  # Explicitly free memory

