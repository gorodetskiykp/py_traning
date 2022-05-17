import pyxel
import enum


class Direction(enum.Enum):
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3


class Apple:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 24, 0, self.w, self.h)


class SnakeSection:
    def __init__(self, x, y, is_head=False) -> None:
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8
        self.is_head = is_head

    def draw(self, direction):
        width = self.w
        height = self.h
        sprite_x = 0
        sprite_y = 0
        if self.is_head:
            if direction == Direction.RIGHT:
                sprite_x = 8
                sprite_y = 0
            
        pyxel.blt(self.x, self.y, 0, 24, 0, self.w, self.h)


class App:
    def __init__(self) -> None:
        pyxel.init(192, 128, capture_scale=8, title="Game", fps=60)
        pyxel.load('assets/my_resource.pyxres')
        self.apple = Apple(64, 32)
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        self.apple.draw()


App()