from turtle import Screen, Turtle
from random import randrange

main_circle = Turtle('circle')
main_circle.shapesize(2)
main_circle.color('deeppink')
main_circle.penup()

main_bullet = Turtle('circle')
main_bullet.shapesize(0.5)
main_bullet.color('deeppink')
main_bullet.speed(0)
main_bullet.penup()

def move_bullet(bullet):
    bullet.forward(15)

    if bullet.distance((0, 0)) > 400:
        bullets.append(bullet)
    else:
        screen.ontimer(lambda b=bullet: move_bullet(b), 50)

    screen.update()

def shoot_bullet():
    bullet = bullets.pop() if bullets else main_bullet.clone()
    bullet.hideturtle()
    bullet.speed(0)
    bullet.home()
    bullet.setheading(randrange(0, 360))
    bullet.showturtle()

    move_bullet(bullet)

bullets = []

screen = Screen()

tghj = False

def shoot_buncha_bullets():
  while tghj == False:
    screen.ontimer(shoot_bullet(), 2)

shoot_buncha_bullets()

screen.listen()
screen.mainloop()