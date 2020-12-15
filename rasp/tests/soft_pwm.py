import RPi.GPIO as IO
import time


def main():
    
    print(IO.VERSION)

    # Use GPIOs names 
    IO.setmode (IO.BCM)

    # Software PWM available on all pins
    # GPIOs as output
    pwm_pins = [17, 18, 27, 22]
        
    IO.setup(pwm_pins, IO.OUT)
    
    # motors mapping
    m1 = IO.PWM(17, 1000)
    m1n = IO.PWM(18, 1000)
    m2 = IO.PWM(27, 1000)
    m2n = IO.PWM(22, 1000)

    m1.start(20);
    m1n.start(50);

    m2.start(70);
    m2n.start(95);
    
    time.sleep(30)
        

if __name__ == '__main__':
    main()



