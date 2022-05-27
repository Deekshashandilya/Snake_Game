from turtle import *


from scoreboard import ScoreBoard
from snake import *
import time
from food import *

screen = Screen()
scores = ScoreBoard()
# turt = Turtle()

screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.colormode(255)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scores.game_over()
        game_is_on = False

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scores.increase_score()

    # Detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scores.game_over()

    # if head collides with any segment in the tail:
    # trigger Game over

screen.exitonclick()
