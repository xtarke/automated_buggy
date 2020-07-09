import pigpio
import time

# http://abyz.me.uk/rpi/pigpio/

def cbf(gpio, level, tick):
    print(gpio, level, tick)

def main():

    pi = pigpio.pi()
    
    if not pi.connected:
      exit(0)

    cb1 = pi.callback(26, pigpio.FALLING_EDGE, cbf)
    
    while True:
        
        
        
        time.sleep(1)
    

if __name__ == '__main__':
    main()
