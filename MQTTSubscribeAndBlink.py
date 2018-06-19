import socket
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW)

def on_connect(client, userdata, flags, rc):
    print("error = "+str(rc))
    client.subscribe("/warsztaty/test")

def on_message(client, userdata, msg):
    print("msg!")
    print(msg.payload)
	if (msg.payload == "msg"):
	    GPIO.output(25, GPIO.HIGH)
        print("on")
        time.sleep(2)
        GPIO.output(25, GPIO.LOW)
        print("off")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect('127.0.0.1', 1883, 60)

client.loop_forever()
