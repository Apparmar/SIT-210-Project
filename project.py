from smbus import SMBus
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

trig = 7
echo = 12
echoTwo = 13

GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)
GPIO.setup(echoTwo,GPIO.IN)

GPIO.output(trig, 0)

addr = 0x8
bus = SMBus(1)

numb = 1


time.sleep(0.1)
print ("Starting measurement...")


def distanceMeas():
    GPIO.output(trig,1)
    time.sleep(0.00001)
    GPIO.output(trig,0)
        
    while GPIO.input(echo) == 0:
        pass
    start = time.time()
    
    while GPIO.input(echo) == 1:
        pass
    end = time.time()
    
    distanceOne = (end - start) * 17000
    return distanceOne

def distanceMeasTwo():
    GPIO.output(trig,1)
    time.sleep(0.00001)
    GPIO.output(trig,0)
    while GPIO.input(echoTwo) == 0:
        pass
    start = time.time()
    
    while GPIO.input(echoTwo) == 1:
        pass
    end = time.time()
    
    distanceTwo = (end - start) * 17000
    
    return distanceTwo


try:
    while True:
#         distOne = 500
        distOne = distanceMeas()
        distTwo = distanceMeasTwo()
        #distance = (distOne + distTwo) / 2
        distance = min(distOne , distTwo)
        print(distance)
        
        if distance < 10 :
            bus.write_byte(addr, 0x1)            
        #else :
        #    bus.write_byte(addr, 0x0)
        time.sleep(1)          
except KeyboardInterrupt:
    print("End")

 
GPIO.cleanup()
