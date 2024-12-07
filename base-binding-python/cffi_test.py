from native import library_cffi

print(library_cffi.lib.cmult(2, 4))
ffi = library_cffi.ffi
lib = library_cffi.lib

point = ffi.new("Point *")
point.x = 10
point.y = 20
# create point from struct
print(f"Point coordinates: ({point.x}, {point.y})")
lib.move(point[0], 5, -3)

lib.move_pointer(point, 5, -3)
print(f"Point coordinates ({point.x}, {point.y})")

