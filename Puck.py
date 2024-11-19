import time
import Servo_Utility as SU
import Parameters as P

def setup():

    global pca

    pca = SU.get_pca_handle()
    
if __name__ == "__main__":

    setup()

    while True:
        pca.continuous_servo[P.LEFT_MOTOR_PIN].throttle = 1
        pca.continuous_servo[P.RIGHT_MOTOR_PIN].throttle = 1
        time.sleep(1)
        pca.continuous_servo[P.LEFT_MOTOR_PIN].throttle = -1
        pca.continuous_servo[P.RIGHT_MOTOR_PIN].throttle = -1
        time.sleep(1)
        pca.continuous_servo[P.LEFT_MOTOR_PIN].throttle = 0
        pca.continuous_servo[P.RIGHT_MOTOR_PIN].throttle = 0