from pathlib import Path

import pyxel

GAME_TITLE = "Space Rescue"
SHIP_SPEED = 2
SCREEN_WIDTH = 160
SCREEN_HEIGHT = 120
SHIP_WIDTH = 8
SHIP_HEIGHT = 8
BALL_SIZE = 4
INITIAL_BALL_COUNT = 1
BALL_ADD_INTERVAL = 15 * 30


class App:
    def __init__(self):
        pyxel.init(160, 120, title=GAME_TITLE)
        pyxel.load(str(Path(__file__).with_name("my_resource.pyxres")))
        self.reset_game()
        pyxel.run(self.update, self.draw)

    def reset_game(self):
        self.ship_x = 76
        self.ship_y = 104
        self.game_over = False
        self.elapsed_frames = 0
        self.balls = []

        for _ in range(INITIAL_BALL_COUNT):
            self.add_ball()

    def add_ball(self):
        self.balls.append({
            "x": pyxel.rndi(0, SCREEN_WIDTH - BALL_SIZE),
            "y": pyxel.rndi(0, SCREEN_HEIGHT - BALL_SIZE),
            "vx": 1 if pyxel.rndi(0, 1) == 1 else -1,
            "vy": 1 if pyxel.rndi(0, 1) == 1 else -1,
        })

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if self.game_over:
            if (pyxel.btnp(pyxel.KEY_R)
                    or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_START)):
                self.reset_game()
            return

        self.elapsed_frames += 1
        if self.elapsed_frames % BALL_ADD_INTERVAL == 0:
            self.add_ball()

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

        for ball in self.balls:
            ball["x"] += ball["vx"]
            ball["y"] += ball["vy"]

            if ball["x"] <= 0 or ball["x"] >= SCREEN_WIDTH - BALL_SIZE:
                ball["vx"] *= -1
            if ball["y"] <= 0 or ball["y"] >= SCREEN_HEIGHT - BALL_SIZE:
                ball["vy"] *= -1

            if self.is_colliding(ball):
                self.game_over = True

    def is_colliding(self, ball):
        return (
            self.ship_x < ball["x"] + BALL_SIZE
            and self.ship_x + SHIP_WIDTH > ball["x"]
            and self.ship_y < ball["y"] + BALL_SIZE
            and self.ship_y + SHIP_HEIGHT > ball["y"]
        )

    def draw(self):
        pyxel.cls(0)
        for ball in self.balls:
            pyxel.circ(ball["x"] + 1, ball["y"] + 1, 2, 8)
        self.draw_ship()

        if self.game_over:
            pyxel.text(48, 48, "GAME OVER", 8)
            pyxel.text(32, 58, "Press R or A", 7)

    def draw_ship(self):
        pyxel.blt(self.ship_x, self.ship_y, 0, 32, 0, 8, 8, 0)

App()