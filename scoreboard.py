from turtle import Turtle

LEVEL_FONT = ("Courier", 12, "normal")
LEVEL_POS = (-230, 250)
END_GAME_FONT = ("Courier", 24, "normal")
END_GAME_POS = (0, 0)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.level = 0
        self.goto(LEVEL_POS)
        self.update_level()

    def update_level(self):
        self.level += 1
        self.clear()
        self.write(f'Level: {self.level}', align='center', font=LEVEL_FONT)

    def game_over(self):
        self.goto(END_GAME_POS)
        self.write('GAME OVER!', align='center', font=END_GAME_FONT)
