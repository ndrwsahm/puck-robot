import RPi.GPIO as GPIO
import Parameters as P
import time

"""
==========================================================================
function : ultrasonic_init

description: Sets the initial settings for the ultrasonic sensors

Inputs
----------

Outputs
---------
pca  :  object  :  object for the pca motor controller
==========================================================================
"""
def ultrasonic_init():

    print("just starting")
    GPIO.setmode(GPIO.BOARD)
    print("at least got here")

    # Set triggers as outputs
    GPIO.setup(P.FRONT_LEFT_TRIGGER_PIN, GPIO.OUT)
    GPIO.setup(P.FRONT_RIGHT_TRIGGER_PIN, GPIO.OUT)
    GPIO.setup(P.BACK_LEFT_TRIGGER_PIN, GPIO.OUT)
    GPIO.setup(P.BACK_RIGHT_TRIGGER_PIN, GPIO.OUT)

    print("looks like we suck")

    # Set echos as inputs
    GPIO.setup(P.FRONT_LEFT_ECHO_PIN, GPIO.IN)
    GPIO.setup(P.FRONT_RIGHT_ECHO_PIN, GPIO.IN)
    GPIO.setup(P.BACK_LEFT_ECHO_PIN, GPIO.IN)
    GPIO.setup(P.BACK_RIGHT_ECHO_PIN, GPIO.IN)

"""
==========================================================================
function : ultrasonic_distance

description: Sets the initial settings for the ultrasonic sensors

Inputs
----------

Outputs
---------
pca  :  object  :  object for the pca motor controller
==========================================================================
"""
def ultrasonic_distance(ultrasonic_sensor):
    print("ultrasonic here")
    print(ultrasonic_sensor)
    GPIO.output(ultrasonic_sensor[P.TRIGGER], True)

    time.sleep(0.00001)

    GPIO.output(ultrasonic_sensor[P.TRIGGER], False)
    print("Sent Trigger")
    start_time = time.time()
    stop_time = time.time()

    # save start time
    while GPIO.input(ultrasonic_sensor[P.ECHO]) == 0:
        start_time = time.time()

    # save time of arrival
    while GPIO.input(ultrasonic_sensor[P.ECHO]) == 1:
        stop_time = time.time()

    print("Here")

    elapased_time = stop_time - start_time
    distance = (elapased_time * 34300) / 2

    return distance