from pathlib import Path

import pyxel

GAME_TITLE = "Space Rescue"


class App:
    def __init__(self):
        pyxel.init(160, 120, title=GAME_TITLE)
        pyxel.load(str(Path(__file__).with_name("my_resource.pyxres")))
        self.is_title = True
        self.ship_x = 76
        self.ship_y = 104
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)
        self.draw_ship()

    def draw_ship(self):
        pyxel.blt(self.ship_x, self.ship_y, 0, 32, 0, 8, 8, 0)
from my_pyxel import main


if __name__ == "__main__":
    main()