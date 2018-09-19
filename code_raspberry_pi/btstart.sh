#!/bin/sh

#Turn on BT
sudo hciconfig hci0 up

#Sets advertising data to: https://myp.me?bleinit
sudo hcitool -i hci0 cmd 0x08 0x0008 1c 02 01 06 03 03 aa fe 14 16 aa fe 10 00 03 6d 79 70 2e 6d 65 3f 62 6c 65 69 6e 69 74 00 00 00

#Setting interval
sudo hcitool -i hci0 cmd 0x08 0x0006 00 A0 00 FF 03 00 00 00 00 00 00 00 00 07 00

#Turning on advertising
sudo hcitool -i hci0 cmd 0x08 0x000a 01

#Run python file
cd /home/pi/Documents/MyStation
sudo python combined.py &




#######DEFAULT SETTING TO TURN ON ADVERTISING
#sudo hciconfig hci0 leadv 3
#######
