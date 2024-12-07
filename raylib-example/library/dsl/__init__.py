import string

from library.native.core_abstractions import WHITE, Color
from library.native.core_functions import init_window, close_window, window_should_close, clear_background, draw_text, \
    set_target_fps, begin_drawing, end_drawing


class Node:
    """
    Base class for all nodes in the DSL
    This a renderable node, which can contains other nodes
    """

    def __init__(self, x: int, y: int):
        self.parent_node = None
        self.x = x
        self.y = y

    def children(self):
        pass

    def add_parent(self, parent):
        if self.parent_node is not None:
            raise Exception("Node already has a parent")
        self.parent_node = parent

    def layout_x(self):
        if self.parent_node is None:
            return self.x
        return self.parent_node.layout_x() + self.x

    def layout_y(self):
        if self.parent_node is None:
            return self.y
        return self.parent_node.layout_y() + self.y
    def render(self):
        pass

    def add_child(self, text2):
        pass


class Text(Node):
    """
    A text node, which can be rendered
    """

    def __init__(self, text: string, x: int, y: int, font_size: int, color: Color):
        super().__init__(x, y)
        # covert text to string to byte
        self.text = text.encode()
        self.x = x
        self.y = y
        self.font_size = font_size
        self.parent_node = Node
        self.color = color

    def render(self):
        draw_text(self.text, self.layout_x(), self.layout_y(), self.font_size, self.color)

    def add_parent(self, parent):
        self.parent_node = parent
        return self


class Panel(Node):
    """
    A panel node, which can contain other nodes
    It has a relative position to its parent
    """

    def __init__(self, x=0, y=0):
        super().__init__(0, 0)
        self.x = x
        self.y = y
        self.children = []

    def add_child(self, child) -> Node:
        self.children.append(child)
        child.add_parent(self)
        return self

    def render(self):
        # get parent
        for child in self.children:
            child.render()
class Window:
    """
    A window node, which can contain other nodes
    """

    def __init__(self, width, height, title, root):
        self.width = width
        self.height = height
        self.title = title.encode()
        self.update_fn = None
        self.panel = root

    def add_child(self, child):
        self.panel.add_child(child)

    def set_update_fn(self, fn):
        self.update_fn = fn
    def render(self):
        init_window(self.width, self.height, self.title)
        set_target_fps(60)
        while not window_should_close():
            # clear background
            begin_drawing()
            clear_background(WHITE)
            self.update_fn()
            self.panel.render()
            end_drawing()
        close_window()
