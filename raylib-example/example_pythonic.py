from library import dsl
from library.native.core_abstractions import *
import random

width = 800
height = 450
fps = 60

panel = dsl.Panel()
text = dsl.Text("Hello, World!", 0, 10, 40, LIGHTGRAY)
text2 = dsl.Text("Hello, World!", 0, 50, 40, LIGHTGRAY)


def update():
    panel.x += random.randint(0, 10)
    panel.y += random.randint(0, 10)
    if panel.x > width:
        panel.x = 0
    if panel.y > height:
        panel.y = 0


panel.add_child(text).add_child(text2)
window = dsl.Window(width, height, "Hello, World!", panel)
window.update_fn = update
window.render()
