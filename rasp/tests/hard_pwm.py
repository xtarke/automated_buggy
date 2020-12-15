import pigpio
import time

GPIO.VERSION

# http://abyz.me.uk/rpi/pigpio/

def main():

    pi = pigpio.pi()

    # Hardware PWM available on GPIO12, GPIO13,
    # GPIO18, GPIO19
    pi.hardware_PWM(12, 1000, 200000)
    pi.hardware_PWM(13, 1000, 500000)
    pi.hardware_PWM(18, 1000, 700000)
    pi.hardware_PWM(19, 1000, 950000)
    

if __name__ == '__main__':
    main()