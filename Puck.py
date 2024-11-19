import time
import Servo_Utility as SU
import Parameters as P

from adafruit_servokit import ServoKit

def setup():

    global pca

    pca = SU.get_pca_handle()

def turnLeft():
    SU.pca_driveMotors(pca, P.FORWARD, P.FORWARD)

def turnRight():
    SU.pca_driveMotors(pca, P.BACKWARD, P.BACKWARD)

def stopMotors():
    SU.pca_driveMotors(pca, P.STOP, P.STOP)

def driveBackward():
    SU.pca_driveMotors(pca, P.BACKWARD, P.FORWARD)

def driveForward():
    SU.pca_driveMotors(pca, P.FORWARD, P.BACKWARD)
    
if __name__ == "__main__":

    setup()

    while True:
        driveForward()
        time.sleep(3)
        driveBackward()
        time.sleep(3)
        turnRight()
        time.sleep(3)
        turnLeft()
        time.sleep(3)
        stopMotors()
        time.sleep(3)