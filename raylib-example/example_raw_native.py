from library.native.core_functions import *
from library.native.core_abstractions import *

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
