import time
import Servo_Utility as SU
import Parameters as P

from adafruit_servokit import ServoKit

def setup():

    global pca

    pca = SU.get_pca_handle()
    
if __name__ == "__main__":

    setup()

    while True:
        SU.pca_driveMotors(pca, P.FORWARD, P.FORWARD)
        time.sleep(3)
        SU.pca_driveMotors(pca, P.BACKWARD, P.BACKWARD)
        time.sleep(3)
        SU.pca_driveMotors(pca, P.FORWARD, P.BACKWARD)
        time.sleep(3)
        SU.pca_driveMotors(pca, P.BACKWARD, P.FORWARD)
        time.sleep(3)
        SU.pca_driveMotors(pca, P.STOP, P.STOP)
        time.sleep(3)