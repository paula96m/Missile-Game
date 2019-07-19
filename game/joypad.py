import pygame

STEERING_AXIS = 4
DIRECTION_AXIS = 3

pygame.init()
pygame.joystick.init()

joystick = pygame.joystick.Joystick(0)
joystick.init()

def refresh_joystick():
    pygame.event.pump()


#brake_button_pressed = int(self.device.joystick.get_button(BRAKE_BUTTON))
#start_button_pressed = int(self.device.joystick.get_button(START_BUTTON))
def get_steering():
    steering = joystick.get_axis(STEERING_AXIS)
    return steering
def get_direction():
    direction = joystick.get_axis(DIRECTION_AXIS)
    return direction
