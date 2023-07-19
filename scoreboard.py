from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self, level):
        super().__init__()
        self.level = level
        self.hideturtle()
        self.penup()
        self.goto(x=-200, y=270)
        self.color("black")

    def level_update(self, level):
        self.clear()
        self.write(arg=f"Level:{level}", move=False, align="center", font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg=f"Game Over", move=False, align="center", font=FONT)
