import turtle
import pygame
import time
from joypad import get_steering, refresh_joystick, get_direction
ROCKET_STEERING_SPEED = 2
ROCKET_DIRECTION_SPEED = 2


window = turtle.Screen()
window.title("Joc Drăgut")
window.bgcolor("black")
window.bgpic('imgg.gif')
window.setup(width=800, height=600)
window.tracer(0)
image = "rr.gif"
window.register_shape(image)

racket1 = turtle.Turtle()
racket1.speed(0)
racket1.shape(image)
racket1.penup()
racket1.goto(0, -200)





def move_rocket_horizontally(distance):
    x = racket1.xcor()
    if (((x+distance) > -400) and ((x+distance) < 400)):
        racket1.setx(x + distance * ROCKET_STEERING_SPEED)
        
        
        
        
def move_rocket_vertically(distance):
    y = racket1.ycor()
    if (((y-distance) > -300) and ((y-distance) < 300)):
        
        racket1.sety(y - distance * ROCKET_DIRECTION_SPEED)
        
            
def bullet():
    bullet = turtle.Turtle()
    bullet.speed(0)
    bullet.shape("square")
    bullet.penup()
    bullet.shapesize(2,0.5)
    bullet.color("orange")
    bullet.setpos(0, 0)
    
while True:
    window.update()
    refresh_joystick()
    steering = get_steering()
    move_rocket_horizontally(steering)
    direction = get_direction()
    move_rocket_vertically(direction)
    bullet()
    
