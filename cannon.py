"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.
"""

from random import randrange
from turtle import *

from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []


def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball):
        ball.x = -195 #cambio a la posición en x de pelota.
        ball.y = -195 #cambio a la posición en y de pelota.
        speed.x = (x + 200) / 25 #cambia a velocidad: 5/25 o 1/5
        speed.y = (y + 200) / 25 #cambia a velocidad: 5/25 o 1/5

        #Cambio en general: Se le aumento la velocidad a los objetivos y a la bala. 

def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """Draw ball and targets."""
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


def move():
    """Move ball and targets."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.25 #se le resto .25 de la velocidad (anterior = 0.5)

    if inside(ball):
        speed.y -= 0.15 #se le resto .20 de la velocidad (anterior = 0.35)
        ball.move(speed)

        #Cambio en general: Se le aumento la velocidad a los objetivos y a la bala. 

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            return

    ontimer(move, 50)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
