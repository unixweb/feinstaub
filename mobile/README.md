
Install File "data.php" on your webserver, its a simple PHP-Script and Webserver must be installed PHP-Support

Check the access and output if works 

http://www.example.com/data.php , if you see a blank website without errors it works<br>







Install Dashboard on the node-red 
```
npm install node-red-dashboard
```
<br>
<br>

# Config Sensor

Configuration Feinstaub-Sensor via Webbrowser http://sensor-ip-address/config


<img src="https://github.com/unixweb/feinstaub/blob/master/mobile/pictures/sensor-config-step-1.png"><br>

Go down to section "An eigene API senden"<br>
Fill field "Server" with your server full-qualifyed-domain-name (FQDN)<br>
Fill field "Pfad" with the path to the installed "data.php" php-script<br>
<img src="https://github.com/unixweb/feinstaub/blob/master/mobile/pictures/configuration-feinstaub-sensor.png"><br>

# Node-Red

Configure Node-Red

<img src="https://github.com/unixweb/feinstaub/blob/master/mobile/pictures/Node-RED-Flow.png"><br>

# Access Dashboard

Access to the dashboard via Webbrowser http://nodered-ip-address:1880/ui

<img src="https://github.com/unixweb/feinstaub/blob/master/mobile/pictures/Node-RED_Dashboard.png">

# feinstaub



<img src="https://blog.unixweb.de/wp-content/uploads/2017/05/Luftdaten.jpg">


Credits and Copyright by luftdaten.info 

More Info<a href="http://luftdaten.info/" target="_blank"> http://luftdaten.info/</a>
