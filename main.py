import turtle
import time

KEY_REPEAT_RATE = 20  # in milliseconds

# Creation and setup of screen
s = turtle.Screen()
s.setup(760, 560)
s.bgcolor("darkslategray")

# Creation of the player. He's called "h". Idk Y.
h = turtle.Turtle()
h.shape("square")
h.color("cyan")
h.speed(60)
h.penup()
h.goto(-260, 0)
h.speed(10)

upToggle = False
downToggle = False
leftToggle = False
rightToggle = False


def plr_speed():
    h.forward(10)


# Registering the shape that the player has while moving.

s.register_shape('plr_move_animation',
                 ((-8, 12), (8, 12), (8, -12), (-8, -12)))

# Registering all the transition shapes once the player has stopped moving.
s.register_shape("plr_trans1", ((-12, 8), (12, 8), (12, -8), (-12, -8)))

s.register_shape("plr_trans2", ((-8, 12), (8, 12), (8, -12), (-8, -12)))

# Defining the player's stop animation.


def plr_stop_animation():
    #h.shape('plr_trans1')
    #h.shape('square')
    #h.shape('plr_trans2')
    h.shape('square')


# List of keys and functions because I couldn't figure out another way to go diagonal.


def process_events():
    events = tuple(sorted(key_events))
    if events and events in key_event_handlers:
        (key_event_handlers[events])()

    key_events.clear()

    s.ontimer(process_events, 20)


def up(toggle):
    global upToggle
    upToggle = toggle
    if leftToggle == True:
        start_repeat(up_left, toggle)
    elif rightToggle == True:
        start_repeat(up_right, toggle)
    else:
        key_events.add('W')


def down(toggle):
    global downToggle
    downToggle = toggle
    if leftToggle == True:
        start_repeat(down_left, toggle)
    elif rightToggle == True:
        start_repeat(down_right, toggle)
    else:
        key_events.add('S')


def left(toggle):
    global leftToggle
    leftToggle = toggle
    if upToggle == True:
        start_repeat(up_left, toggle)
    elif downToggle == True:
        start_repeat(down_left, toggle)
    else:
        key_events.add('A')


def right(toggle):
    global rightToggle
    rightToggle = toggle
    if upToggle == True:
        start_repeat(up_right, toggle)
    elif downToggle == True:
        start_repeat(down_right, toggle)
    else:
        key_events.add('D')


def up_left(toggle):
    key_events.add('A', )
    key_events.add('W', )


def up_right(toggle):
    key_events.add('D', )
    key_events.add('W', )


def down_left(toggle):
    key_events.add('A', )
    key_events.add('S', )


def down_right(toggle):
    key_events.add('D', )
    key_events.add('S', )


def dash():
    key_events.add('SPACE')


def do_dash():
    dash_circle = turtle.Turtle()
    dash_circle.hideturtle()
    dash_circle.speed(0)
    dash_circle.penup()
    dash_circle.setpos(h.xcor(), h.ycor())
    dash_circle.shape('circle')
    dash_circle.color('white', 'darkslategray')
    dash_circle.shapesize(1)
    dash_circle.speed(5)
    dash_circle.showturtle()
    h.forward(150)
    dash_circle.right(10)
    dash_circle.shapesize(1.5)
    dash_circle.right(10)
    dash_circle.shapesize(2)
    dash_circle.right(10)
    dash_circle.shapesize(2.5)
    dash_circle.right(10)
    dash_circle.shapesize(3)
    dash_circle.hideturtle()


def move_up():
    h.setheading(90)
    h.shape('plr_move_animation')
    plr_speed()
    if repeating:
        s.ontimer(move_up, KEY_REPEAT_RATE)
    else:
        #h.setheading(0)
        plr_stop_animation()


def move_down():
    h.setheading(270)
    h.shape('plr_move_animation')
    plr_speed()
    if repeating:
        s.ontimer(move_down, KEY_REPEAT_RATE)
    else:
        #h.setheading(0)
        plr_stop_animation()


def move_left():
    h.setheading(180)
    h.shape('plr_move_animation')
    plr_speed()
    if repeating:
        s.ontimer(move_left, KEY_REPEAT_RATE)
    else:
        #h.setheading(0)
        plr_stop_animation()


def move_right():
    h.setheading(0)
    h.shape('plr_move_animation')
    plr_speed()
    if repeating:
        s.ontimer(move_right, KEY_REPEAT_RATE)
    else:
        #h.setheading(0)
        plr_stop_animation()


def move_up_right():
    h.setheading(45)
    h.shape('plr_move_animation')
    plr_speed()
    if repeating:
        s.ontimer(move_up_right, KEY_REPEAT_RATE)
    else:
        #h.setheading(0)
        plr_stop_animation()


def move_down_right():
    h.setheading(315)
    h.shape('plr_move_animation')
    plr_speed()
    if repeating:
        s.ontimer(move_down_right, KEY_REPEAT_RATE)
    else:
        #h.setheading(0)
        plr_stop_animation()


def move_up_left():
    h.setheading(135)
    h.shape('plr_move_animation')
    plr_speed()
    if repeating:
        s.ontimer(move_up_left, KEY_REPEAT_RATE)
    else:
        #h.setheading(0)
        plr_stop_animation()


def move_down_left():
    h.setheading(225)
    h.shape('plr_move_animation')
    plr_speed()
    if repeating:
        s.ontimer(move_down_left, KEY_REPEAT_RATE)
    else:
        #h.setheading(0)
        plr_stop_animation()


def start_repeat(func, toggle):
    global repeating
    repeating = True
    func(True)


def no_up():
    global upToggle
    upToggle = False


def no_down():
    global downToggle
    downToggle = False


def no_left():
    global leftToggle
    leftToggle = False


def no_right():
    global rightToggle
    rightToggle = False


def stop_repeat(func):
    global repeating
    repeating = False
    func()

key_event_handlers = { \
  ('D', 'W'): move_up_right, \
  ('D', 'S'): move_down_right, \
  ('A', 'W'): move_up_left, \
  ('A', 'S'): move_down_left, \
  ('W',): move_up, \
  ('S',): move_down, \
  ('A',): move_left, \
  ('D',): move_right, \
  ('SPACE',): do_dash, \
}

key_events = set()

repeating = False

s.onkeypress(lambda: start_repeat(up, upToggle), 'w')
s.onkeyrelease(lambda: stop_repeat(no_up), 'w')

s.onkeypress(lambda: start_repeat(down, downToggle), 's')
s.onkeyrelease(lambda: stop_repeat(no_down), 's')

s.onkeypress(lambda: start_repeat(left, leftToggle), 'a')
s.onkeyrelease(lambda: stop_repeat(no_left), 'a')

s.onkeypress(lambda: start_repeat(right, rightToggle), 'd')
s.onkeyrelease(lambda: stop_repeat(no_right), 'd')
'''s.onkeypress(lambda: start_repeat(up_left), 'w', 'a')
s.onkeyrelease(lambda: stop_repeat(upToggle), 'w', 'a')

s.onkeypress(lambda: start_repeat(up_right), 'w', 'd')
s.onkeyrelease(lambda: stop_repeat(downToggle), 'w', 'd')

s.onkeypress(lambda: start_repeat(down_left), 's', 'a')
s.onkeyrelease(lambda: stop_repeat(leftToggle), 's', 'a')

s.onkeypress(lambda: start_repeat(down_right), 's', 'd')
s.onkeyrelease(lambda: stop_repeat(rightToggle), 's', 'd')'''

s.onkey(dash, 'space')

# Tell the screen to listen for key presses
s.listen()

process_events()

#from attacks import circleshootrandom

s.mainloop()
