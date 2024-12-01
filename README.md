---
marp: true
---
<!--
theme: gaia

-->

# TODO
## Multi-plaform binding with Python!

:microphone: **Speaker**: _Gianluca Aguzzi_, University of Bologna
:email: Email: gianluca.aguzzi@unibo.it
:globe_with_meridians: Personal site: [https://cric96.github.io/](https://cric96.github.io/)

---
 
# Outline
- How to handle (conceptually) python - native interaction
- Main alternative in the current panorame
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
