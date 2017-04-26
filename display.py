#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import dothat.lcd as lcd  #import for display

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " +str(rc))
    client.subscribe('#')

def on_message(client, userdata, msg):  #triggers on an update
    #need to add a clear display
    #pls change the topic in your sensor id
    if msg.topic.find('/374586/') != -1:  #checks if the topic is the needed one

        if msg.topic.find('sensor1') != -1:
            lcd.set_cursor_position(0,0)
            value = str(msg.payload).strip("b")
            value = value.strip("'")
            lcd.write('10 ug: ' + value)

        if msg.topic.find('sensor2') != -1:
            lcd.set_cursor_position(0,1)
            value = str(msg.payload).strip("b")
            value = value.strip("'")
            lcd.write('2.5 ug: ' + value)

        if msg.topic.find('sensor3') != -1:
            lcd.set_cursor_position(0,2)
            value = str(msg.payload).strip("b")
            value = value.strip("'")
            lcd.write('Temp: ' + value)


client = mqtt.Client()
client.connect("mqtt.unixweb.de",1883,60)  #connects to the broker

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
