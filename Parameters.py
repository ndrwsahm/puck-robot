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

# Servo Pulse Width Mins and Maxs
#MIN = 425    MAX = 2575
LEFT_MOTOR_MIN = 400
LEFT_MOTOR_MAX = 2450

RIGHT_MOTOR_MIN = 425
RIGHT_MOTOR_MAX = 2400

            # Servo Pin,  Min Pulse, Max Pulse
SERVO_PINS = [[LEFT_MOTOR_PIN, LEFT_MOTOR_MIN, LEFT_MOTOR_MAX],
            [RIGHT_MOTOR_PIN, RIGHT_MOTOR_MIN, RIGHT_MOTOR_MAX]]

