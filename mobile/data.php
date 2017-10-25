<?php
echo "it works";
$logURL="sensor.json";
$logToOrdner="/var/www/htdocs/luftdaten/sensor/".date('Ymd').".json";

$itime= time();//timestamp Januar 1 1970 00:00:00 GMT
$datum= date('Y-m-d');
$zeit=  date('G:i:s');

$daten = file_get_contents('php://input');

//aktuelles Messwert
$handle=fopen($logURL,'w');//Datei überschreiben
fwrite ($handle, "[{" );
fwrite ($handle, '"time":'.$itime.',');
fwrite ($handle, '"datum":"'.$datum.'",');
fwrite ($handle, '"zeit":"'.$zeit.'",');
fwrite ($handle, '"daten":'.$daten  );
fwrite ($handle, "}]".chr(10) );
fclose ($handle);

//als Datensätze in Ordner,
$add=file_exists($logToOrdner);
$handle=fopen($logToOrdner,'a');//Daten anhängen
if($add)fwrite ($handle, "," );
fwrite ($handle, "{" );
fwrite ($handle, '"time":'.$itime.',');
fwrite ($handle, '"datum":"'.$datum.'",');
fwrite ($handle, '"zeit":"'.$zeit.'",');
fwrite ($handle, '"daten":'.$daten  );
fwrite ($handle, "}".chr(10) );
fclose ($handle);
?>
