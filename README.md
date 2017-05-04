Import with Copy/Paste the nodered-???.txt into the Node-Red as Flow and click Deploy

You must configure the http-node with your IP-Address and Port credentials 

and edit the MQTT Node and put in your sensor-id and replace "123456" its only a placeholder


nodered-mqtt.txt is the flow with mqtt, you can send your values to any dashboard's

nodered-twitter.txt is the flow with twitter, the flow send every 60 minutes 4 values

for using display.py or display-color.py please install depencies and hardware they need

- [Display O-Tron Hat](http://amzn.to/2p3lj7C)
```
pip3 install paho-mqtt
url https://get.pimoroni.com/displayotron | bash
```

Features of display.py
- if you press Left and right button displays different values
- Colour changes Green/Yellow/Orange/Red  if PM25 reached values 10/20/30/40 μg/m3
- If PM25 reached less then 10.00 the background light goes off

<img src="/PM25-10.jpg">
<img src="/PM25-40.jpg">
<img src="/TEMP-Display.jpg">

# feinstaub

<img src="/Luftdaten.jpg">


Credits and Copyright by luftdaten.info 

More Info<a href="http://luftdaten.info/"> http://luftdaten.info/</a>
