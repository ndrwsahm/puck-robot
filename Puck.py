import time
import Servo_Utility as SU
import Parameters as P
import Ultrasonic_Utility as UU

from adafruit_servokit import ServoKit

def setup():

    global pca

    pca = SU.get_pca_handle()
    print("here we go!!!")
    UU.ultrasonic_init()

def driveForward():
    SU.pca_driveMotors(pca, P.BACKWARD, P.FORWARD)
 
def driveBackward():
    SU.pca_driveMotors(pca, P.FORWARD, P.BACKWARD)
   
def turnRight():
    SU.pca_driveMotors(pca, P.FORWARD, P.FORWARD)

def turnLeft():
    SU.pca_driveMotors(pca, P.BACKWARD, P.BACKWARD)

def stopMotors():
    SU.pca_driveMotors(pca, P.STOP, P.STOP)
    
if __name__ == "__main__":

    setup()

    while True:

        distance = UU.ultrasonic_distance(P.ULTRASONIC_SENSORS[0])
        print(distance)

        time.sleep(1)
        """
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
        """
    