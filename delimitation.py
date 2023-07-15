from turtle import Turtle


# Délimitation du terrain

class Delimitation(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 300)
        self.setheading(270)
        self.line()
        # self.square_area()

    def line(self):
        for _ in range(60):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)

    """def square_area(self):

        self.setheading(0)
        self.penup()
        self.goto(-400, -300)
        self.pendown()
        self.pensize(10)
        for _ in range(1, 5):
            if _ % 2 == 0:
                self.forward(600)
            else:
                self.forward(800)
            self.left(90)"""


"""""
tim = Turtle()
screen = Screen()
tim.setheading(-45)
tim.forward(10)

tim.setheading(-135)
tim.forward(10)"""





