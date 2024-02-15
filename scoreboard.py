from turtle import Turtle

SCOREBOARD_POSITION = (0, 260)
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(SCOREBOARD_POSITION)
        self.color("black")
        self.display()

    def increment(self):
        self.level += 1
        self.display()
    
    def display(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)