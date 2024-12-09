from library.native.core_functions import *
from library.native.core_abstractions import *

width = 800
height = 450
fps = 60
speed = 10
font_size = 40
text_y = 10

init_window(width, height, b"Hello, World!")
set_target_fps(fps)

dx = 0
while not window_should_close():
    begin_drawing()
    clear_background(BLACK)
    draw_text(b"Hello, World!", dx, text_y, font_size, LIGHTGRAY)
    end_drawing()
    dx = (dx + speed) % width
close_window()