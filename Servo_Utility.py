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
pca  :  double  :  handle for the pca motor controller
==========================================================================
"""
def get_pca_handle(void):

    pca = ServoKit(channels=16, address=0x40)

    return pca

"""
==========================================================================
function : pca_init

description: Initializes the pca servo motor controller

Inputs
----------

Outputs
---------
pca  :  double  :  handle for the pca motor controller
==========================================================================
"""
def pca_init(void):

    pca = get_pca_handle()

    for x in range(len(P.SERVO_PINS)):
        pca.servo[P.SERVO_PINS[x][0]].set_pulse_width_range(P.SERVO_PINS[x][1], P.SERVO_PINS[x][2])

    return pca
