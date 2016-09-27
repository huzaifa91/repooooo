
import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BCM)
LIGHT=4

GPIO.setup(LIGHT,GPIO.OUT)

try:
   while True:
      GPIO.OUT(LIGHT,True)
      Time.sleep(0.5)
      GPIO.OUT(LIGHT,False)
      Time.sleep(0.5)
      print ("blink")
 except KeyboardInterrupt:
     GPIO.cleanup()		
