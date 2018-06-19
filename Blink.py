import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW)

while(1):
  GPIO.output(25, GPIO.HIGH)
  print("on")
  time.sleep(2)
  GPIO.output(25, GPIO.LOW)
  print("off")
  time.sleep(2)
