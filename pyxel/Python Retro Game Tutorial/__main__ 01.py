import pyxel


class App:
    def __init__(self) -> None:
        pyxel.init(192, 128, capture_scale=8, title="Game", fps=60)
        self.x = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = (self.x + 1) % pyxel.width

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, 0, 8, 8, 9)


App()