---
marp: true
---
<!--
footer: ''
-->

# TODO
## Multi-platform binding with Python!

:microphone: **Speaker**: _Gianluca Aguzzi_, University of Bologna
:email: Email: gianluca.aguzzi@unibo.it
:globe_with_meridians: Personal site: [https://cric96.github.io/](https://cric96.github.io/)
PDF slides @ [https://cric96.github.io/phd-course-python-binding/index.pdf](https://cric96.github.io/phd-course-python-binding/)

---
 
# Outline
- How to handle (conceptually) Python-native interaction
- Main alternatives in the current landscape
- A guided example with [raylib](https://www.raylib.com/index.html)

---

# Creating Bindings from Native Code
## Agenda :thought_balloon:
- What do you want to **expose**?
    - Low level or Pythonic?
- How to **manage** different types?
    - Marshalling?
- How to handle **memory**?
    - GC vs Manual Management

---

# What to Expose?
- It's important to define what you want to expose to the Python side
- Typically, native code **isn't** Pythonic, so you need to create a Pythonic interface
- **Flow**: Native :arrow_right: Direct Python Binding :arrow_right: Pythonic Interface


---

# Managing Different Types
- **Marshalling**: the process of transforming data to pass between the two platforms

- Two mindsets:
    - C :arrow_right: Focused on performance
    - Python :arrow_right: Focused on simplicity
- Examples:
    - Integers: C has int, short, long, long long; Python has int
    - Floats: C has float, double; Python has float

---

# Managing Memory

- Different paradigms:
    - C :arrow_right: Manual memory management
    - Python :arrow_right: Garbage collection

- Key challenges:
    - Memory ownership tracking
    - Cross-language memory management
    - Object lifetime synchronization

- Important considerations:
    - Memory allocation origin
    - Immutability concerns
---

# Main Alternatives

Python offers several ways to create bindings with native code, from completely manual to automatic:
- [**ctypes**](https://docs.python.org/3/library/ctypes.html): Built-in Python library for calling C functions directly
- [**cffi**](https://cffi.readthedocs.io/en/stable/): Modern alternative to ctypes with cleaner API and better performance
- [**Cython**](https://cython.org/): A language that makes writing C extensions for Python as easy as Python itself
- [**SWIG**](https://www.swig.org/): A code generator for creating bindings in different languages (including Python)

---

# Ctypes
- Built-in Python library for calling C functions directly
    - No need to write C code
    - No need to compile anything
    - Part of the Python standard library

- How it works:
    - Load a shared library
    - Wrap input for C functions (marshalling)
    - Wrap output from C functions (unmarshalling)

---

# Load a Shared Library

Ctypes needs to load a shared library to access C functions
```python
import ctypes

# Load the shared library (local)
lib = ctypes.CDLL('path/to/shared/library.so')

# Find a library by name

lib = ctypes.CDLL(find_library("library"))

``` 

---

# Wrap Input for C Functions

Giving this simple C function:
```c
float cmult(int int_param, float float_param) 
```

You can call it from Python like this:
```python
# Define the function signature
cmult = lib.cmult
cmult.argtypes = [ctypes.c_int, ctypes.c_float]
cmult.restype = ctypes.c_float

# Call the function
result = cmult(2, 3.14)
```

---

# Wrap structs

You can also wrap C structs in Python
```c
typedef struct {
    int x;
    float y;
} Point;
```
In python you can define the struct like this:
```python
class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_float)]
```

---

# Pass structs to functions

You can pass structs to C functions
```c
void move_point(Point p, int dx, float dy) {
    p-x += dx;
    p.y += dy;
}
```

In Python you can call it like this:
```python
move_point = lib.move_point
move_point.argtypes = [Point, ctypes.c_int, ctypes.c_float]
move_point.restype = None

p = Point(1, 2.0)
move_point(p, 3, 4.0)
```