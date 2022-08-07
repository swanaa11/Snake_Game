from turtle import *
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
setup(600, 600)
bgcolor("black")
title("Snake Game")
tracer(0)

"""
Method - 1

segment_1 = Turtle("square")
segment_1.color("white")

segment_2 = Turtle("square")
segment_2.color("white")
segment_2.goto(-20, 0)

segment_3 = Turtle("square")
segment_3.color("white")
segment_3.goto(-40, 0)
"""
snake = Snake()
food = Food()
score = Score()

listen()
onkey(snake.up, "Up")
onkey(snake.down, "Down")
onkey(snake.left, "Left")
onkey(snake.right, "Right")

flag = True
while flag:
    update()
    time.sleep(0.1)
    snake.move()
    """collision with food"""
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase()

    """collision with wall"""
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # flag = False
        score.reset()
        snake.reset()

    """collision with tail"""
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            # flag = False
            score.reset()
            snake.reset()

screen.exitonclick()
