import paho.mqtt.client as mqtt
 
client = mqtt.Client()
client.connect("127.0.0.1")
 
client.publish("/warsztaty/test", "1" ,0)