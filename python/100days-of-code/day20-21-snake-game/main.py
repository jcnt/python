from time import sleep
from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import ScoreBoard

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


is_running = True

while is_running:
    screen.update()
    sleep(0.1)
    snake.move()
    scoreboard


    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.snake_grow()

    # Detect collision with walls
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.reset()
        snake.reset()


    # Detect collision with tail
    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 1:
            scoreboard.reset()
            snake.reset()





screen.exitonclick()
