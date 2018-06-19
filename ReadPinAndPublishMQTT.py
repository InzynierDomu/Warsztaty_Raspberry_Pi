import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

client = mqtt.Client()
client.connect("127.0.0.1")

while(1):
  print GPIO.input(4)
  if (GPIO.input(4) == 1):
    client.publish("/warsztaty/test", "1" ,0)
  time.sleep(2)
