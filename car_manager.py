from turtle import Turtle
from random import choice
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_LENGTH = 40
CAR_WIDTH = 20

class CarManager:
    
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        car = Turtle()
        car.color(choice(COLORS))
        car.shape("square")
        car.penup()
        car.shapesize(stretch_wid=CAR_WIDTH//20, stretch_len=CAR_LENGTH//20)
        car.goto(305, randint(-260, 280))
        car.setheading(180)
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.move_distance)
    
    def speed_up(self):
        self.move_distance += MOVE_INCREMENT

    def is_collision(self, player):
        for car in self.cars:
            if abs(player.xcor() - car.xcor()) < 30 and abs(player.ycor() - car.ycor()) < 20:
                return True
        return False