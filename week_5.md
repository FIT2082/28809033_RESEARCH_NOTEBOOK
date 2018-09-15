# Week 5

## Raspberry PI
Raspberry PI Model 3 is a very intersting device for a few reasons. The device features inbuilt Bluetooth and Wi-Fi modules. The PI has Bluetooth Low Energy capability that can be used in the project. 

![alt text](https://images-na.ssl-images-amazon.com/images/I/91zSu44%2B34L._SX355_.jpg "Raspberry PI 3")



The indended usage of the PI is as follows: 
* BLE: to act as a beacon and transmit values for the phone to recieve in real time (almost) 
* Wireless: to connect to internet to fetch and update software and use as fallback option if Bluetooth fails
* IO Pins: to communicate with a capacitive touch sensor to map touch points on the 3D model

![alt text](https://fit2082.github.io/28809033_RESEARCH_NOTEBOOK/images/BLE_PI_Beacon.png "Bluetooth Beacon PI Diagram")

The Bluetooth will be transmitting the touch sensor pressed. Each index on the touch sensor will map to a point on the 3D Model. The phone can decode the touch sensor pressed and will run an apprioprate action mapped to the touch on the model. 

## OS and Setup
Raspberry PI has an offical OS (Raspbian). The OS was installed by running the following command: 

```
sudo dd bs=1m if=path_of_your_image.img of=/dev/rdiskn conv=sync
```

The OS was written to the SD card and plugged in. The PI booted up alright but SSH connection failed initally and there way no way to connect to the PI. 

After looking around, an empty file called 'ssh' had to be added to the root directory of the SD card to enable SSH. After that, the following command was used to connect to PI.

```
ssh pi@__ip__
password: raspberry
```

After connecting to the PI, the following command scans for the nearby BLE (Bluetooth Low Energy) devices.
```
sudo hcitool lescan
```

## Transmitting Data
After a simple exploration there are a few options to transmit the data to the phone. 
* Change bluetooth name and poll constantly on the phone (FLE_*XX*) *XX* representing the touch sensor ID.
* Encode the data as part of the advertisement packet 
* Pair with nearby bluetooth device automatically with known characteristics

The above options will be explored in further detail next week. 




