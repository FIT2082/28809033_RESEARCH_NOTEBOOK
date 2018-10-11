## Eddystone Data Format
Eddystone beacon defines three data formats (URL, Telementry and UID)
In our case we needed to figure out how to encode the selected sensor in one of the three available formats.

This is a solution which involves transmitting a URL which encodes the sensor pressed.

So in this project I decided to encode it as https://myp.me?sensorId

To do that there were a few steps involved.

Because we can have more sensors in the future (upto 26)

```
pressedSensor = ascii('sensorId') - ascii('A')
```

Transmitted | URL 
--- | ---
0 | https://myp.me?A
1 | https://myp.me?B
2 | https://myp.me?C

The other puzzle of the beacon is actually setting the advertising data.

To set the data to https://myp.me?A, the command used is 

```
sudo hcitool -i hci0 cmd 0x08 0x0008 16 02 01 06 03 03 aa fe 0e 16 aa fe 10 00 03 6d 79 70 2e 6d 65 3f 41 00 00 00 00 00 00 00 00 00
```

```
HEX_CODE_FOR_TRANSMISSION = hex (ord('A') + sensorIdTouched)

sudo hcitool -i hci0 cmd 0x08 0x0008 NUM_BYTES_TO_FOLLOW 02 01 06 03 03 EDDYSTONE_UUID 0e 16 EDDYSTONE_UUID FRAME_TYPE_URL 00 HTTPS (character in hex)... 79 70 2e 6d 65 3f HEX_CODE_FOR_TRANSMISSION 00 00 00 00 00 00 00 00 00
```


## Eddystone Scanning App
