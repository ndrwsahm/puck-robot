import time
import Servo_Utility as SU
import Parameters as P

from adafruit_servokit import ServoKit

def setup():

    global pca

    pca = SU.get_pca_handle()
    
if __name__ == "__main__":

    #setup()
    pca = ServoKit(channels=16)

    while True:
       # pca.servo[P.LEFT_MOTOR_PIN].angle = 180
        pca.servo[1].angle = 180
        #pca.continuous_servo[P.LEFT_MOTOR_PIN].throttle = 1
        #pca.continuous_servo[P.RIGHT_MOTOR_PIN].throttle = 1
        time.sleep(1)
        #pca.continuous_servo[P.LEFT_MOTOR_PIN].throttle = -1
        #pca.continuous_servo[P.RIGHT_MOTOR_PIN].throttle = -1
        time.sleep(1)
        #pca.servo[P.LEFT_MOTOR_PIN].angle = 0
        pca.servo[1].angle = 0
        #pca.continuous_servo[P.LEFT_MOTOR_PIN].throttle = 0
        #pca.continuous_servo[P.RIGHT_MOTOR_PIN].throttle = 0