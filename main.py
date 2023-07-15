from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from delimitation import Delimitation
import time
# Initialisation du terrain de jeu

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
delimitation = Delimitation()

# Initialisation des joueurs, formes et déplacements

paddle_1 = Paddle((350, 0))
paddle_2 = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_1.up, 'Up')
screen.onkey(paddle_1.down, 'Down')
screen.onkey(paddle_2.up, 'z')
screen.onkey(paddle_2.down, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.speed_ball)
    screen.update()

    ball.move()

    # Détection de la balle avec le haut et le bas
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Détection entre la balle et les rackette
    if ball.distance(paddle_1) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Détecte si la rackette 1 a raté la balle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.scored_paddle2()

    # Détecte si la rackette 2 a raté la balle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.scored_paddle1()


screen.exitonclick()


