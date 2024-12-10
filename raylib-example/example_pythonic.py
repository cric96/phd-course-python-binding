from library import dsl
from library.native.core_abstractions import *
import random

width = 800
height = 450
font_size = 40
text_y = 10
dx = 10

panel = dsl.Panel()
text = dsl.Text("Hello, World!", 0, 0, font_size, LIGHTGRAY)
text2 = dsl.Text("Hello, World!", 0, font_size + text_y, font_size, LIGHTGRAY)

def update():
    panel.x = (panel.x + random.randint(0, dx)) % width
    panel.y = (panel.y + random.randint(0, dx)) % height

panel.add_children([text, text2])
window = dsl.Window(width, height, "Hello, World!", panel)
window.update_fn = update
window.render()
