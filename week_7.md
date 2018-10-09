## Eddystone Beacon Protocol
After much playing around with advertising packets it meant that I was developing my own protocol for the transmission of the data.

## Raspberry PI Advertise Mode
The raspberry PI advertising mode is a configuration of the bluetooth low energy adapter in which Raspberry PI cannot connect to other clients. It can only broadcast information to nearby device without feedback.

It can be enabled by the following command
```
 sudo hciconfig hci0 leadv 3
```
However in that command it sets the default interval to around 1000ms, which means the PI will transmit at a frequency of 1Hz, which can be too slow in our use case. To solve that issue, after some research on the BLE protocol, I enabled the frequency to somewhere between 100-160 milliseconds.

The protocol takes in a range of values rather than a single value *The Advertising_Interval_Min and Advertising_Interval_Max should not be the same value to enable the Controller to determine the best advertising interval given other activities.*

So therefore, the command below was used to set the advertising interval manually.

```
sudo hcitool -i hci0 cmd 0x08 0x0006 00 A0 00 FF 03 00 00 00 00 00 00 00 00 07 00
```


00A0 = 160 * 0.625 = 100 ms advertising interval
00FF = 255 * 0.625 = 160 ms advertising interval

The interval is specified as hex values after 0x0006 as (low bound) and (high bound)

The bound value is taken and multiplied by 0.625ms, to get the actual amount of advertising interval.

There fastest advertising possible without connection is 100ms, it could be much faster if the devices are paired however for the scope of the project it's not required and adds additional complexity to the application usage. 


## Data Encoding in Eddystone


## Eddystone Scanner App
