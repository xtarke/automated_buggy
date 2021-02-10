import pigpio, time

def onChange(gpio,level,tick):
    global data_level
    global phrase, init
    global count, correct_count

    count = count + 1
    

if __name__ == '__main__':
   
   CLK_pin=5
   
   phrase=""
   data_level = 0

   count = 0
   correct_count = 0
   init = False
   
   pi = pigpio.pi()
   pi.set_mode(CLK_pin, pigpio.INPUT)
  
   cb1 = pi.callback(CLK_pin, pigpio.RISING_EDGE, onChange)
   
   print('Start Benchmark')
   time.sleep(1)

   print('Frequency XX:',count,'-',correct_count)