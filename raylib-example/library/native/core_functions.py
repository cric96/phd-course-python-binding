import ctypes
from library.native import raylib
from library.native.core_abstractions import Color

init_window = raylib.InitWindow
init_window.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_char_p]
init_window.restype = None

close_window = raylib.CloseWindow
close_window.argtypes = None
close_window.restype = None

window_should_close = raylib.WindowShouldClose
window_should_close.argtypes = None
window_should_close.restype = ctypes.c_bool

set_target_fps = raylib.SetTargetFPS
set_target_fps.argtypes = [ctypes.c_int]
set_target_fps.restype = None

begin_drawing = raylib.BeginDrawing
begin_drawing.argtypes = None
begin_drawing.restype = None

end_drawing = raylib.EndDrawing
end_drawing.argtypes = None
end_drawing.restype = None

draw_text = raylib.DrawText
draw_text.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, Color]
draw_text.restype = None

clear_background = raylib.ClearBackground
clear_background.argtypes = [Color]
clear_background.restype = None