"""
==============================================================================================================================
Written by: Andrew Sahm
Date: 11.26.23

General settings module for puck-robot. 
==============================================================================================================================
"""

# Servo Pins for the individual legs
LEFT_MOTOR_PIN = 0
RIGHT_MOTOR_PIN = 1

FRONT_LEFT_TRIGGER_PIN = 26
FRONT_RIGHT_TRIGGER_PIN = 19
BACK_LEFT_TRIGGER_PIN = 13
BACK_RIGHT_TRIGGER_PIN = 6

FRONT_LEFT_ECHO_PIN = 21
FRONT_RIGHT_ECHO_PIN = 25
BACK_LEFT_ECHO_PIN = 20
BACK_RIGHT_ECHO_PIN = 16


# Servo Pulse Width Mins and Maxs
#MIN = 425    MAX = 2575
LEFT_MOTOR_MIN = 400
LEFT_MOTOR_MAX = 2450

RIGHT_MOTOR_MIN = 425
RIGHT_MOTOR_MAX = 2400

            # Servo Pin,  Min Pulse, Max Pulse
SERVO_PINS = [[LEFT_MOTOR_PIN, LEFT_MOTOR_MIN, LEFT_MOTOR_MAX],
            [RIGHT_MOTOR_PIN, RIGHT_MOTOR_MIN, RIGHT_MOTOR_MAX]]


FORWARD = 1
BACKWARD = -1
STOP = 0

TRIGGER = 0
ECHO = 1

FRONT_LEFT = 0
FRONT_RIGHT = 1
BACK_LEFT = 2
BACK_RIGHT = 3

ULTRASONIC_SENSORS = [[FRONT_LEFT_TRIGGER_PIN, FRONT_LEFT_ECHO_PIN],
                      [FRONT_RIGHT_TRIGGER_PIN, FRONT_RIGHT_ECHO_PIN],
                      [BACK_LEFT_TRIGGER_PIN, BACK_LEFT_ECHO_PIN],
                      [BACK_RIGHT_TRIGGER_PIN, BACK_RIGHT_ECHO_PIN]]