import turtle
import time
from math import *

screen = turtle.Screen()
screen.setup(width=1200, height=800)
screen.tracer(50)

sidebar = turtle.Turtle()
sidebar.hideturtle()
sidebar.penup()
sidebar.goto(400, 300)
sidebar.write("Planet Info", align="left", font=("Arial", 16, "bold"))

sun = turtle.Turtle()
sun.shape('circle')
sun.color('yellow')
sun.shapesize(2)
sun.penup()
sun.goto(-300, 0)

class Planet(turtle.Turtle):
    def __init__(self, name, radius, color, size, speed, days):
        super().__init__(shape='circle')
        self.name = name
        self.radius = radius
        self.c = color
        self.color(self.c)
        self.shapesize(size)
        self.speed = speed
        self.days = days
        self.up()
        self.pd()
        self.angle = 0

    def move(self):
        x = self.radius * cos(self.angle)
        y = self.radius * sin(self.angle)
        self.goto(sun.xcor() + x, sun.ycor() + y)

mercury = Planet("Mercury", 40, 'grey', 0.5, 0.05, 88)
venus = Planet("Venus", 80, 'orange', 0.9, 0.03, 225)
earth = Planet("Earth", 100, 'blue', 1, 0.01, 365)
mars = Planet("Mars", 150, 'red', 0.8, 0.007, 687)
jupiter = Planet("Jupiter", 180, 'brown', 1.2, 0.02, 4333)
saturn = Planet("Saturn", 230, 'pink', 1.1, 0.018, 10759)
uranus = Planet("Uranus", 250, 'light blue', 1, 0.016, 30687)
neptune = Planet("Neptune", 280, 'black', 1, 0.005, 60190)

myList = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

y_offset = 280
for planet in myList:
    sidebar.goto(400, y_offset)
    sidebar.write(f"{planet.name}: {planet.days} days, Color: {planet.c}", align="left", font=("Arial", 12, "normal"))
    y_offset -= 20

while True:
    screen.update()
    for i in myList:
        i.move()
    mercury.angle += mercury.speed
    venus.angle += venus.speed
    earth.angle += earth.speed
    mars.angle += mars.speed
    jupiter.angle += jupiter.speed
    saturn.angle += saturn.speed
    uranus.angle += uranus.speed
    neptune.angle += neptune.speed
