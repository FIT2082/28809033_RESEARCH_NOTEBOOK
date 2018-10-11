## Eddystone Data Format
Eddystone beacon defines three data formats (URL, Telementry and UID)
In our case we needed to figure out how to encode the selected sensor in one of the three available formats.

This is a solution which involves transmitting a URL which encodes the sensor pressed.

So in this project I decided to encode it as https://myp.me/?*sensorId*

To do that there were a few steps involved.

Because we can have more sensors in the future (upto 26)

```
pressedSensor = ascii('sensorId') - ascii('A')
```

Transmitted | URL 
--- | ---
0 | https://myp.me?**A**
1 | https://myp.me?**B**
2 | https://myp.me?**C**



## Eddystone Scanning App
