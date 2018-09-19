# Raspberry PI Setup

## OS
Official Raspbian is used

## Setup
### Enable i2c
```
sudo raspi-config
```

### Script on boot
```
sudo crontab -e

# then append the following at the end
# ensure the sh script is 'executable'
# chmod +x my_start_script.sh
@reboot /home/pi/__my__start__script.sh
```

### Auto-connect Wi-Fi
The raspberry PI will autoconnect to a Wireless network with the following details
```
SSID: MyPlatform
Pass: password123.
```
This can be used for debugging using a mobile hotspot.

