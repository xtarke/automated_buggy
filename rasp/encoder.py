import pigpio
import time

# http://abyz.me.uk/rpi/pigpio/

wheel_pulses = 20
counter = 0

def cbf(gpio, level, tick):
    global counter
    counter = counter + 1

def main():
    global counter

    pi = pigpio.pi()
    
    if not pi.connected:
      exit(0)

    cb1 = pi.callback(26, pigpio.FALLING_EDGE, cbf)
    
    while True:
        
        time.sleep(1)
        
        # rpm = (60 * 1000 / wheel_pulses ) / (millis() - timeold) * counter;
        rpm = (60 * 1000 / wheel_pulses ) / 1000 * counter;
        counter = 0;
        
        print(rpm)
    

if __name__ == '__main__':
    main()
