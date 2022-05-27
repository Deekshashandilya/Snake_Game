from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for positions in STARTING_POSITION:
            self.add_segment(positions)

    def add_segment(self,positions):
        new_Turt = Turtle("square")
        new_Turt.color("white")
        new_Turt.penup()
        new_Turt.goto(positions)
        self.segments.append(new_Turt)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            next_x = self.segments[seg_num - 1].xcor()
            next_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(next_x, next_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
