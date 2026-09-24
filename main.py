from pathlib import Path

import pyxel

GAME_TITLE = "Space Rescue"
SHIP_SPEED = 2
SCREEN_WIDTH = 160
SCREEN_HEIGHT = 120
SHIP_WIDTH = 8
SHIP_HEIGHT = 8


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

        if (pyxel.btn(pyxel.KEY_LEFT)
                or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT)):
            self.ship_x -= SHIP_SPEED
        if (pyxel.btn(pyxel.KEY_RIGHT)
                or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT)):
            self.ship_x += SHIP_SPEED
        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
            self.ship_y -= SHIP_SPEED
        if (pyxel.btn(pyxel.KEY_DOWN)
                or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN)):
            self.ship_y += SHIP_SPEED

        self.ship_x = max(0, min(self.ship_x, SCREEN_WIDTH - SHIP_WIDTH))
        self.ship_y = max(0, min(self.ship_y, SCREEN_HEIGHT - SHIP_HEIGHT))

    def draw(self):
        pyxel.cls(0)
        pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)
        self.draw_ship()

    def draw_ship(self):
        pyxel.blt(self.ship_x, self.ship_y, 0, 32, 0, 8, 8, 0)

App()