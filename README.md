---
marp: true
---
<!--
footer: ''
-->

# Creating Python Bindings for Native Code

:microphone: **Speaker**: _Gianluca Aguzzi_, University of Bologna
:email: Email: gianluca.aguzzi@unibo.it
:globe_with_meridians: Personal site: [https://cric96.github.io/](https://cric96.github.io/)
PDF slides @ [https://cric96.github.io/phd-course-python-binding/index.pdf](https://cric96.github.io/phd-course-python-binding/index.pdf)

---
 
# Outline
- How to handle (conceptually) Python-native interaction
- Main alternatives in the current landscape (see [/base-binding-python](/base-binding-python/))
    - For more details, please refer to this [guide](https://realpython.com/python-bindings-overview/)
- A guided example with [raylib](https://www.raylib.com/index.html) (see [/raylib-binding-python](/raylib-binding-python/))

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
- General guideline:
    - Native interface :arrow_right: language-specific binding :arrow_right: Idiomatic (language-based) interface
    - In Python, **Flow**: Native :arrow_right: Direct Python Binding :arrow_right: Pythonic Interface 
    - Sometimes, the Python Binding is created automatically

---
# What "Idiomatic" Means

- **Idiomatic Code**
    - Code that is natural to the target programming language
    - Follows design principles and community best practices
        - Namely, idioms (common patterns) and conventions (coding style)

- **Examples**
    - *Effective Java*: [Effective Java](https://www.amazon.com/Effective-Java-Joshua-Bloch/dp/0134685997)
    - *The Zen of Python*: [The Zen of Python](https://www.python.org/dev/peps/pep-0020/)

- **Different Languages, Different Styles**
    - **Python**: Readability, simplicity, elegance
    - **C**: Performance, control, efficiency

- **Creating an Interface** :arrow_right: Map between idiomatic styles

---

# Managing Different (Platform) Types
- **Marshalling**: the process of transforming data to pass between the two *platforms*

- Two mindsets:
    - C :arrow_right: Focused on performance
    - Python :arrow_right: Focused on simplicity
- Examples:
    - Integers: C has int, short, long, long long; Python has int
    - Floats: C has float, double; Python has float
- In the *binding* layer, you need to handle these differences

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

# How to run

- Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate
```
- Install the dependencies
```bash
pip install -r requirements.txt
```
- Build the shared library
```bash
invoke build-libray
```
- Run the Python script
```bash
python ctypes_test.py
```
---

# On Invoke

- [**Invoke**](http://www.pyinvoke.org/) is a Python library for managing tasks
- It's a simple way to define and run tasks
- It's similar to Makefiles, but in Python
- It's a good way to automate tasks in Python projects
- There are other alternatives like [**Ninja**](https://ninja-build.org/)

---
# How to use Invoke

- Install Invoke
```bash
pip install invoke
```
- Create a file called `tasks.py` with the following content:
```python
from invoke import task

@task
def hello(c):
    print("Hello, world!")
```
- Run the task
```bash
invoke hello
```

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

---

# Pass pointer to functions

You can also pass pointers to C functions
```c
void move_point(Point *p, int dx, float dy) {
    p->x += dx;
    p->y += dy;
}
```

In Python you can call it like this:
```python
move_point = lib.move_point
move_point.argtypes = [ctypes.POINTER(Point), ctypes.c_int, ctypes.c_float]
move_point.restype = None
point = Point(1, 2.0)
move_point(ctypes.byref(point), 3, 4.0)
```
:exclamation: it is important to use `ctypes.byref` to pass a pointer to the struct :exclamation:


---

# Ctypes Summary

- **Pros** :fire::
    - Part of the Python standard library
    - No need to write C code
    - No need to compile anything
- **Cons** :cry::
    - Low level API
    - Limited functionality (Class? Templates?)

---

# CFFI

- Modern alternative to ctypes with an auto-generated API
- Two main modes for creating bindings:
    - ABI mode: Call C functions directly
    - API mode: Use a C header file to generate a Python API

CFFI need to be installed with pip:
```bash
pip install cffi
```

---

# CFFI Module Creation
- CFFI creates a **full Python module**
- Steps to create CFFI bindings:
    1. Write Python code for bindings
    2. Generate loadable module
    3. Import and use the module

---

## Writing Bindings
```python
import cffi
ffi = cffi.FFI()

# Process header file
ffi.cdef(header_content)

# Configure source
ffi.set_source(
    "module_name",
    '#include "library.h"',
    libraries=["library"],
    library_dirs=[dir_path],
    extra_link_args=["-Wl,-rpath,."]
)
```

---

# Generating Module
```python
ffi.compile()
```

- This will generate a shared library that can be imported in Python using the module name given in `set_source` :fire:

- You don't need to write any manual marshalling code, CFFI will handle it for you :boom:

- Unfortunately, CFFI doesn't support C++ :cry:
    - Typical workaround: Create a C wrapper around the C++ code

--- 

# Python wrapper

- Starting from the CFFI module, you can create a Python wrapper


```python

class PointWrapper:
    def __init__(self, x=0, y=0):
        # Allocate memory for a C Point structure
        self._c_point = ffi.new("Point *")
        self.x = x
        self.y = y

    ## Utility methods

    # Functions from Point
    def move(self, dx, dy): #[...]
    
    def move_in_place(self, dx, dy): #[...]

    def __del__(self):
        ffi.release(self._c_point)  # Explicitly free memory
```

---

# Alternatives?
- **Cython** :rocket:: A language that makes writing C extensions for Python as easy as Python itself
    - :zap: Static compiler that converts Python code to C
    - :chart_with_upwards_trend: Excellent performance for numerical computations
    - :handshake: Can handle both Python and C code seamlessly
    - :heavy_plus_sign: Direct support for C++ (unlike CFFI)
    - :microscope: Popular in scientific computing ([NumPy](https://github.com/numpy/numpy), [SciPy](https://scipy.org/))
    - :warning: Steeper learning curve than ctypes/CFFI

---

## How it works?
- Write a `.pyx` file with a Python-like syntax
- Compile it with Cython
- Import the compiled module in Python

---

## Example
```python
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
```

---

And compile with:
```python
# setup.py
from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("point.pyx")
)
```

or do it manually

```bash
invoke.run("cython --cplus -3 library.pyx")
invoke.run("g++ -shared -std=c++11 -fPIC $(python3-config --includes) -o library.so library.cpp")
```

---

# Cython Summary
- **Pros** :fire::
    - Excellent performance :rocket:
    - Direct support for C++ :heavy_plus_sign::heavy_plus_sign:
    - Seamless integration with Python :snake:
- **Cons** :cry::
    - Steeper learning curve :mountain:
        - Requires to learn ``another'' language :book:
    - Requires compilation step :hammer_and_wrench:
    - Not as easy as ctypes/CFFI :confused:

---

# SWIG
- Simplified Wrapper and Interface Generator: [](https://www.swig.org/)
- A code generator for creating bindings in different languages
    - Supports Python, Scala,
- **Pros** :fire::
    - Supports multiple languages :globe_with_meridians:
    - Can generate bindings automatically :gear:
    - Can handle C++ code :heavy_plus_sign:
- **Cons** :cry::
    - Complex to use :construction:
    - Not as popular as ctypes/CFFI/Cython :chart_with_downwards_trend:

---

# Raylib Example :video_game: :joystick:

- [**Raylib**](https://www.raylib.com/index.html) is a simple and easy-to-use library to learn videogame programming :rocket:

- Written in **C** with focus on clean and efficient API :gear:

- We will create a **Python binding** for Raylib using ctypes :snake:

### Requirements
- Raylib installed on your system
    - follow the instructions [here](https://www.raylib.com/index.html)

---

# First level: Native Interface :construction_worker:

- **First step**: Create Python binding for Raylib using ctypes :snake:

- Start by selecting core functions to expose :dart::
    - :window: Window management
    - :pencil2: Drawing simple text
    - :broom: Clear the screen functionality

- Design principles in mind: **KISSéé (Keep It Simple, Stupid) :bulb:
    - map the main functions and structure from Raylib to Python

---

# How to?
- Look at the [Raylib documentation](https://www.raylib.com/cheatsheet/cheatsheet.html): 
- Load the shared library
```python
try: 
    lib = ctypes.CDLL(ctypes.util.find_library("raylib"))
except OSError:
    print("Error loading the shared library, try to install it!")
    sys.exit(1)
```

- Extract some main structures
```python
class Color(ctypes.Structure):
    _fields_ = [
        ("r", ctypes.c_ubyte), 
        ("g", ctypes.c_ubyte), 
        ("b", ctypes.c_ubyte), 
        ("a", ctypes.c_ubyte)
    ]
```

---

# How to? :wrench:

- Define the functions you want to expose with **ctypes**
    - It's **recommended** to explicitly define parameters and return types
```python
init_window = lib.InitWindow
init_window.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_char_p]
init_window.restype = None
```

- Why Types? :thinking:

    - :shield: Prevents errors in marshalling/unmarshalling
    - :recycle: Helps avoid memory leaks
    - :book: Makes code self-documenting and more readable
    - :warning: **Remember**: Clear type definitions are crucial for reliable native bindings!
---

# Simple example
```python
width = 800
height = 450
fps = 60
speed = 10
init_window(width, height, b"Hello, World!")
set_target_fps(fps)

move = 0
while not window_should_close():
    begin_drawing()
    clear_background(BLACK)
    draw_text(b"Hello, World!", move, 10, 40, LIGHTGRAY)
    end_drawing()
    move = (move + speed) % width
close_window()
```
---

# Assignment

- *Goal*: Create a binding between two different platforms
    - **Native** (C/C++) and **Python**; or **Native** and **Kotlin**; or **Python** and **Java**

- *Requirements*:
    - **Native** code with at least one function and one structure (minimum): look at [awesome c libraries](https://github.com/oz123/awesome-c) 
    - Create an idiomatic interface in the target language

- *Deliverables*:
    - A **GitHub repository** with the code and a report which includes (**at least**):
        - **Design choices** what makes your binding idiomatic