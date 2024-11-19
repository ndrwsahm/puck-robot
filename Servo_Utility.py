import time
from adafruit_servokit import ServoKit

import Parameters as P

"""
==========================================================================
function : get_pca_handle

description: Gets the handle for pca servo motor controller

Inputs
----------

Outputs
---------
pca  :  object  :  object for the pca motor controller
==========================================================================
"""
def get_pca_handle():

    pca = ServoKit(channels=16)

    return pca

"""
==========================================================================
function : pca_init

description: Initializes the pca servo motor controller

Inputs
----------

Outputs
---------
pca  :  object  :  object for the pca motor controller
==========================================================================
"""
def pca_init():

    pca = get_pca_handle()

    for x in range(len(P.SERVO_PINS)):
        pca.servo[P.SERVO_PINS[x][0]].set_pulse_width_range(P.SERVO_PINS[x][1], P.SERVO_PINS[x][2])

    return pca

"""
==========================================================================
function : pca_driveMotors

description: Drives the motors 

Inputs
----------
    pca:  object  :  deterimine which object to drive
    left_motor  :  int  : Forward = 1, Backward = -1, Stop = 0
    right_motor  :  int  : Forward = 1, Backward = -1, Stop = 0

Outputs
---------

==========================================================================
"""
def pca_driveMotors(pca, left_motor, right_motor):

    pca.continuous_servo[P.LEFT_MOTOR_PIN].throttle = left_motor
    pca.continuous_servo[P.RIGHT_MOTOR_PIN].throttle = right_motor

