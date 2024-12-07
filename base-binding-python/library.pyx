# distutils: language=python3

# point.pyx
cdef struct Point:
    int x
    float y

cdef class PyPoint:
    cdef Point p

    def __init__(self, x=0, y=0.0):
        self.p.x = x
        self.p.y = y

    def move(self, dx, dy):
        self.p.x += dx
        self.p.y += dy

    @property
    def x(self):
        return self.p.x

    @property
    def y(self):
        return self.p.y
