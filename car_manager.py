import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
HEADING_ANGLE = 180
MAX_NO_CARS = 25


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = MOVE_INCREMENT
        self.create_car()

    def create_car(self):
        for i in range(MAX_NO_CARS):
            car = Turtle(shape='square')
            car.ht()
            car.shapesize(stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            car.setpos((random.randint(300, 900), random.randint(-240, 280)))
            car.setheading(HEADING_ANGLE)
            car.showturtle()
            self.cars.append(car)

    def moving_traffic(self):
        for car_ in self.cars:
            car_.forward(self.speed)
            if car_.xcor() < -320:
                car_.setpos((random.randint(300, 900), car_.ycor()))

    def increase_speed(self):
        self.speed += 5

    def clear_cars(self):
        self.cars = []
