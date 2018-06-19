import socket
import paho.mqtt.client as mqtt
 
def on_connect(client, userdata, flags, rc):
    print("error = "+str(rc))
 
    client.subscribe("/warsztaty/test")
 
def on_message(client, userdata, msg):
    print("msg!")
    print(msg.payload)
 
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect('127.0.0.1', 1883, 60)
 
client.loop_forever()