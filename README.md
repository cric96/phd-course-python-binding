---
marp: true
---
<!--
theme: gaia
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
- How to handle (conceptually) python - native interaction
- Main alternative in the current panorama
- A guided example with [raylib](https://www.raylib.com/index.html)

---

# Create Binding from Native 
## Agenda :thought_balloon:
- What you want to **expose**?
    - Low level or pythonic?
- How to **manage** the different types?
    - Marshalling?
- How to handle the **memory**?
    - GC vs Manual

---

# What you want to expose?
- It is important to define what you want to expose to the Python side.

- Typically, native code is note pythonic, so you need to create a pythonic interface.

- **Flow**: Native :arrow_right: Direct Python Binding  :arrow_right: Pythonic Interface

---

# How to manage the different types?
- **Marshalling**: the process of transforming the data to be passed between the two platform.

- Two mindset:
    - C :arrow_right: Focused on performance,
    - Python :arrow_right: Focused on simplicity
- Examples:
    - Integers: C has int, short, long, long long, Python has int
    - Floats: C has float, double, Python has double

---

# How to mannage memory?

---

# Main alternatives

In python, there are several ways to create a binding with native code, from completaly manual to automatic.

- [**ctypes**](https://docs.python.org/3/library/ctypes.html): Python standard library, it is a foreign function interface (FFI) for Python.

- [**cffi**](https://cffi.readthedocs.io/en/stable/): A foreign function interface for Python calling C code.

- [**Cython**](https://cython.org/): A language that makes writing C extensions for Python as easy as Python itself.

- [**Swig**](https://www.swig.org/): A code generator for create several bidings in different languages (among them, Python).

---

