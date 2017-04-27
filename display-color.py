#!/usr/bin/env python3

#needed commands
#pip3 install paho-mqtt
#curl https://get.pimoroni.com/displayotron | bash

import paho.mqtt.client as mqtt
import dothat.backlight as backlight
import dothat.lcd as lcd  #import for display

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " +str(rc))
    client.subscribe('#')

def on_message(client, userdata, msg):  #triggers on an update
    def colours(value):  #changes whole backlight based on numeric values
        if value > 40:
            backlight.rgb(238, 0, 0)  #red
        elif value > 30:
            backlight.rgb(238, 154, 0)  #orange
        elif value > 20:
            backlight.rgb(238, 238, 0)  #yellow
        elif value > 10:
            backlight.rgb(0, 238, 118)  #green

    if msg.topic.find('/374586/') != -1:  #checks if the topic is the needed one
        if msg.topic.find('sensor1') != -1:
            lcd.set_cursor_position(0,0)
            value = str(msg.payload).strip("b")  #strips unneeded parts from the values
            value = value.strip("'")
            lcd.write('PM10: ' + value)

        if msg.topic.find('sensor2') != -1:
            lcd.set_cursor_position(0,1)
            value = str(msg.payload).strip("b")
            value = value.strip("'")
            lcd.set_cursor_position(0,1)  #writes the numerical value under the word
            colours(float(value))
            lcd.write('PM25: ' + value)

        if msg.topic.find('sensor3') != -1:
            lcd.set_cursor_position(0,2)
            value = str(msg.payload).strip("b")
            value = value.strip("'")
            lcd.write('Temp: ' + value)

backlight.off()  #clears colours
client = mqtt.Client()
client.connect("mqtt.unixweb.de",1883,60)  #connects to the broker

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
