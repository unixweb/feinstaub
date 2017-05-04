#!/usr/bin/env python3
# -*- coding: <utf-8> -*-

#Author: Callum Pritchard, Joachim Hummel
#Project Name: Display-o-Tron Weather
#Project Description: Getting weather sensor data from mqtt, parsing the data and then displaying it to the display
#Version Number: 0.8
#Date: 2/5/17
#Release State: Alpha testing
#Changes: Removing incorrect characters, also pushing values to the extreme right

#needed commands
#pip3 install paho-mqtt
#curl https://get.pimoroni.com/displayotron | bash

import paho.mqtt.client as mqtt
import dothat.backlight as backlight
import dothat.lcd as lcd  #import for display
import dothat.touch as nav  #import for buttons

global display_num
display_num = 0

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

    def replace_line(line_num, text):
        file = open('/tmp/values.txt', 'r')
        lines = file.readlines()
        print(lines)
        lines[line_num] = text + '\n'  #to save sensor values to call later
        out = open('/tmp/values.txt', 'w')
        out.writelines(lines)
        out.close()

    if msg.topic.find('/374586/') != -1:  #checks if the topic is the needed one
        value = str(msg.payload).strip("b")
        value = value.strip("'")

       # value = float("{0:.2f}".format(value)) # ensure value is to two d.p
       # value = str(value)

        if msg.topic.find('sensor1') != -1:
            replace_line(0, value)

        if msg.topic.find('sensor2') != -1:
            colours(float(value))
            replace_line(1, value)

        if msg.topic.find('sensor3') != -1:
            replace_line(2, value)

        if msg.topic.find('sensor4') != -1:
            replace_line(3, value)

        file = open('/tmp/values.txt', 'r')
        tempfile = file.readlines()

        if display_num == 0:
            lcd.clear()
            lcd.set_cursor_position(0, 0)
            lcd.write("PM10:")
            lcd.set_cursor_position(10, 0)
            lcd.write(str(tempfile[0]).strip('\n'))
            lcd.set_cursor_position(0, 1)
            lcd.write("PM25:")
            lcd.set_cursor_position(10, 1)
            lcd.write(str(tempfile[1]).strip('\n'))

        elif display_num == 1:
            lcd.clear()
            lcd.set_cursor_position(0, 0)
            lcd.write("Temp:")
            lcd.set_cursor_position(10, 0)
            lcd.write(str(tempfile[2]).strip('\n'))
            lcd.set_cursor_position(0, 1)
            lcd.write("Feuchte:")
            lcd.set_cursor_position(10, 1)
            lcd.write(str(tempfile[3]).strip('\n'))

        file.close()

@nav.on(nav.LEFT)
def handle_left(ch, evt):
    lcd.clear()
    file = open('/tmp/values.txt', 'r')
    tempfile = file.readlines()
    lcd.set_cursor_position(0, 0)
    lcd.write("PM10:")
    lcd.set_cursor_position(10, 0)
    lcd.write(str(tempfile[0]).strip('\n'))
    lcd.set_cursor_position(0, 1)
    lcd.write("PM25:")
    lcd.set_cursor_position(10, 1)
    lcd.write(str(tempfile[1]).strip('\n'))
    global display_num
    display_num = 0
    file.close()

@nav.on(nav.RIGHT)
def handle_right(ch, evt):
    lcd.clear()
    file = open('/tmp/values.txt', 'r')
    tempfile = file.readlines()
    lcd.set_cursor_position(0, 0)
    lcd.write("Temp:")
    lcd.set_cursor_position(10, 0)
    lcd.write(str(tempfile[2]).strip('\n'))
    lcd.set_cursor_position(0, 1)
    lcd.write("Feuchte:")
    lcd.set_cursor_position(10, 1)
    lcd.write(str(tempfile[3]).strip('\n'))
    global display_num
    display_num = 1
    file.close()

file = open('/tmp/values.txt', 'w')
file.write('0.0\n0.0\n0.0\n0.0')
file.close()

backlight.off()  #clears colours
client = mqtt.Client()
client.connect("mqtt.unixweb.de",1883,60)  #connects to the broker

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()



